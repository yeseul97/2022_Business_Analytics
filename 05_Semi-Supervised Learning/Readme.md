## ✍ 5번째 튜토리얼 "Semi-Supervised Learning"
 
### <목차>
#### 1. Proxy-label method : `Pseudo Label`
#### 2. Consistency regularization : `PI model`, `VAT`, `Mean Teacher`, `ICT`
#### 3. Holistic methods : `MixMatch`
#### 4. 실험

---

## 1️. Proxy-label method 

  : Labeled set으로 학습된 모델을 이용해 unlabeled data point들에 label을 달아주는 기법


  #### 📌 Method 1. `Pseudo Label` (13')
  ![image](https://user-images.githubusercontent.com/67623921/209647081-9874fab0-5f36-43a4-91d9-a224ca76e1ef.png)
  
  출처: https://sanghyu.tistory.com/177


## 2️. Consistency regularization

  : Unlabeled data에 data augmentation을 통해 class가 바뀌지 않을 정도의 변화를 줬을 때, 원 데이터와의 예측결과가 같아지도록 unsupervised loss를 주어 학습하게 됨. 



  #### 📌 Method 2. `PI model` (16')
  ![image](https://user-images.githubusercontent.com/67623921/209645936-254931a4-4b02-4496-9ef5-089c52d4cc8a.png)
  
  출처: https://amitness.com/2020/07/semi-supervised-learning/
  
  
  #### 📌 Method 3. `VAT` (17')
  ![image](https://user-images.githubusercontent.com/67623921/209646055-166bc795-a250-416f-9357-8afd04d3824b.png)
  
  출처: https://sh-tsang.medium.com/review-virtual-adversarial-training-vat-4b3d8b7b2e92
    
  
  #### 📌 Method 4. `Mean Teacher` (17')
  ![image](https://user-images.githubusercontent.com/67623921/209646198-4661e185-e44c-4d23-af9f-8960e1eb6f13.png)
  
  출처: https://velog.io/@injokim/%EC%99%95%EC%B4%88%EA%B8%89-Semi-supervised-learning-%EC%9E%85%EB%AC%B8


  #### 📌 Method 5. `ICT` (19')
  ![image](https://user-images.githubusercontent.com/67623921/209646639-8695ddbc-e433-4a9f-9884-c1e03f1c245a.png)
  
  출처: Verma, V., Kawaguchi, K., Lamb, A., Kannala, J., Bengio, Y., & Lopez-Paz, D. (2019). Interpolation consistency training for semi-supervised learning. arXiv preprint arXiv:1903.03825.
  
  
  
## 3️. Holistic methods

  : 여러 semi-supervised learning 기법들을 통합하고 Mixup data augmentation을 적용하여 성능을 더 끌어 올림.

  #### 📌 Method 6. `MixMatch` (19')
  ![image](https://user-images.githubusercontent.com/67623921/209646904-61c6481e-7192-4495-9139-a8ed37d9ae9b.png)
  
  출처: https://rain-bow.tistory.com/entry/Semi-Supervised-Learning-SSL-%EC%86%8C%EA%B0%9C-%EB%B0%8F-%EB%8F%99%ED%96%A5


  
## 4. 실험

#### `"Loss를 변경해 가며 성능 변화를 확인하자"`
기존 Loss: `MSE` → 실험할 Loss: `L1 Loss`, `KL divergence`, `JS divergence`

- Semi-Supervised Learning의 목적함수는 supervised Loss $L_s$와 unsupervised Loss $L_u$의 합을 최소화하는 것으로 표현할 수 있음. 

- 이 점은 2-stage로 학습하는 self-supervised learning, transfer learning 등과의 차이점임. 

- 따라서, Semi-Supervised Learning에서는 대용량 unlabeled data에 주는 unsupervised task를 어떻게 정하는지가 중요함. 

- 하지만, 대부분의 모델들이 MSE로 Loss를 계산함. 

Kim, T., Oh, J., Kim, N., Cho, S., & Yun, S. Y. (2021). Comparing kullback-leibler divergence and mean squared error loss in knowledge distillation. arXiv preprint arXiv:2105.08919.

- 위 논문을 보면, 



