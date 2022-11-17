#!/usr/bin/env python
# coding: utf-8

# In[2]:


import torch.nn as nn


# In[4]:


## AutoEncoder
class AutoEncoder(nn.Module):
    def __init__(self,args):
        super(AutoEncoder, self).__init__()
        self.Encoder = nn.Sequential(
            nn.Linear(args.AE_channels[0],args.AE_channels[1]),
            nn.BatchNorm1d(args.AE_channels[1]),
            nn.LeakyReLU(),
            nn.Linear(args.AE_channels[1],args.AE_channels[2]),
            nn.BatchNorm1d(args.AE_channels[2]),
            nn.LeakyReLU(),
        )
        self.Decoder = nn.Sequential(
            nn.Linear(args.AE_channels[2],args.AE_channels[1]),
            nn.BatchNorm1d(args.AE_channels[1]),
            nn.LeakyReLU(),
            nn.Linear(args.AE_channels[1],args.AE_channels[0]),
        )
        
    def forward(self, x):
        x = self.Encoder(x)
        x = self.Decoder(x)
        return x


# In[5]:


## 1D CNN AutoEncoder
class ConvAutoencoder(nn.Module): # 신경망 모델을 정의할 때는 nn.Module을 상속해야 함.
    '''PyTorch의 nn라이브러리는 Neural Network의 모든 것을 포괄하는 모든 신경망 모델의 Base Class'''
    '''참고-https://anweh.tistory.com/m/21'''
    def __init__(self, args):
        super(ConvAutoencoder, self).__init__() # nn.Module을 사용하면 이 코드 필요함. 
        self.args = args
    
        self.encoder = nn.Sequential(
            nn.Conv1d(self.args.CAE_channels[0],self.args.CAE_channels[1],self.args.CAE_kernel_size[0]),
            nn.BatchNorm1d(self.args.CAE_channels[1]),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Conv1d(self.args.CAE_channels[1],self.args.CAE_channels[2],self.args.CAE_kernel_size[1]),
            nn.BatchNorm1d(self.args.CAE_channels[2]),
            nn.LeakyReLU(0.2, inplace=True))
        
        self.decoder = nn.Sequential(
            nn.ConvTranspose1d(self.args.CAE_channels[2],self.args.CAE_channels[1],self.args.CAE_kernel_size[1]),
            nn.BatchNorm1d(self.args.CAE_channels[1]),
            nn.LeakyReLU(0.2, inplace=True),
            nn.ConvTranspose1d(self.args.CAE_channels[1],self.args.CAE_channels[0],self.args.CAE_kernel_size[0]))
          
    def forward(self,x):
            f = self.encoder(x)
            output = self.decoder(f)
            return output


# In[ ]:

## AE_DeepSVDD_network
class AE_DeepSVDD_network(nn.Module):
    def __init__(self,args):
        super(AE_DeepSVDD_network, self).__init__()
        self.Encoder = nn.Sequential(
            nn.Linear(args.AE_channels[0],args.AE_channels[1]),
            nn.BatchNorm1d(args.AE_channels[1]),
            nn.LeakyReLU(),
            nn.Linear(args.AE_channels[1],args.AE_channels[2]),
            nn.BatchNorm1d(args.AE_channels[2]),
            nn.LeakyReLU()
        )
       
        
    def forward(self, x):
        f = self.Encoder(x)
        return f

