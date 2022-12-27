#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader
import numpy as np

import argparse, math, time, json, os

from lib import wrn, transform, datasets, train_and_test

import warnings
warnings.filterwarnings( 'ignore' )

# cuda 연결
if torch.cuda.is_available():
    device = "cuda"
    torch.backends.cudnn.benchmark = True
else:
    device = "cpu"

def Main(args, model, alg_cfg, shared_cfg, ssl_obj, optimizer, l_loader, u_loader, val_loader, val_dataset, test_loader, test_dataset):
    iteration = 0
    maximum_val_acc = 0
    s = time.time()
    for l_data, u_data in zip(l_loader, u_loader):
        iteration += 1
        l_input, target = l_data # labeled data
        l_input, target = l_input.to(device).float(), target.to(device).long()

        if args.alg != "supervised": # for ssl algorithm
            u_input, dummy_target = u_data # unlabeled data
            u_input, dummy_target = u_input.to(device).float(), dummy_target.to(device).long()

            target = torch.cat([target, dummy_target], 0) # label+unlabeled target
            unlabeled_mask = (target == -1).float() #??

            inputs = torch.cat([l_input, u_input], 0)
            outputs = model(inputs)

            # ramp up exp(-5(1 - t)^2)
            coef = alg_cfg["consis_coef"] * math.exp(-5 * (1 - min(iteration/shared_cfg["warmup"], 1))**2)
            ssl_loss = ssl_obj(inputs, outputs.detach(), model, unlabeled_mask) * coef # 목적함수

        else:
            outputs = model(l_input)
            coef = 0
            ssl_loss = torch.zeros(1).to(device)

        # supervised loss
        cls_loss = F.cross_entropy(outputs, target, reduction="none", ignore_index=-1).mean()

        loss = cls_loss + ssl_loss # '''최종 손실함수'''

        if args.em > 0:
            loss -= args.em * ((outputs.softmax(1) * F.log_softmax(outputs, 1)).sum(1) * unlabeled_mask).mean()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if args.alg == "MT" or args.alg == "ICT":
            # parameter update with exponential moving average
            ssl_obj.moving_average(model.parameters())
        # display
        if iteration == 1 or (iteration % 100) == 0:
            wasted_time = time.time() - s
            rest = (shared_cfg["iteration"] - iteration)/100 * wasted_time / 60
            print("iteration [{}/{}] cls loss : {:.6e}, SSL loss : {:.6e}, coef : {:.5e}, time : {:.3f} iter/sec, rest : {:.3f} min, lr : {}".format(
                iteration, shared_cfg["iteration"], cls_loss.item(), ssl_loss.item(), coef, 100 / wasted_time, rest, optimizer.param_groups[0]["lr"]),
                "\r", end="")
            s = time.time()

        # validation
        if (iteration % args.validation) == 0 or iteration == shared_cfg["iteration"]:
            with torch.no_grad():
                model.eval()
                print()
                print("### validation ###")
                sum_acc = 0.
                s = time.time()
                for j, data in enumerate(val_loader):
                    input, target = data
                    input, target = input.to(device).float(), target.to(device).long()

                    output = model(input)

                    pred_label = output.max(1)[1]
                    sum_acc += (pred_label == target).float().sum()
                    if ((j+1) % 10) == 0:
                        d_p_s = 10/(time.time()-s)
                        print("[{}/{}] time : {:.1f} data/sec, rest : {:.2f} sec".format(
                            j+1, len(val_loader), d_p_s, (len(val_loader) - j-1)/d_p_s
                        ), "\r", end="")
                        s = time.time()
                acc = sum_acc/float(len(val_dataset))
                print()
                print("varidation accuracy : {}".format(acc))
                # test
                if maximum_val_acc < acc:
                    print("### test ###")
                    maximum_val_acc = acc
                    sum_acc = 0.
                    s = time.time()
                    for j, data in enumerate(test_loader):
                        input, target = data
                        input, target = input.to(device).float(), target.to(device).long()
                        output = model(input)
                        pred_label = output.max(1)[1]
                        sum_acc += (pred_label == target).float().sum()
                        if ((j+1) % 10) == 0:
                            d_p_s = 100/(time.time()-s)
                            print("[{}/{}] time : {:.1f} data/sec, rest : {:.2f} sec".format(
                                j+1, len(test_loader), d_p_s, (len(test_loader) - j-1)/d_p_s
                            ), "\r", end="")
                            s = time.time()
                    print()
                    test_acc = sum_acc / float(len(test_dataset))
                    print("test accuracy : {}".format(test_acc))
                    # torch.save(model.state_dict(), os.path.join(args.output, "best_model.pth"))
            model.train()
            s = time.time()
        # lr decay
        if iteration == shared_cfg["lr_decay_iter"]:
            optimizer.param_groups[0]["lr"] *= shared_cfg["lr_decay_factor"]

    print("test acc : {}".format(test_acc))

