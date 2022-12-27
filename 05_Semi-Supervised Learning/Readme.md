## ✍ 5번째 튜토리얼 "Semi-Supervised Learning"

  ✔ 적은 labeled data가 있으면서 추가로 활용할 수 있는 대용량의 unlabeled data가 있을 때

  ✔ 소량의 labeled data에는 supervised learning을 적용하고 unlabeled data에는 unsupervised learning을 적용해 성능향상을 목표로 함.

  ✔ 데이터 자체의 본질적인 특성이 모델링 된다면 소량의 labeled data를 통한 약간의 가이드로 일반화 성능을 끌어올릴 있음. 

![image](https://user-images.githubusercontent.com/67623921/209644289-622ed290-b74a-4d6e-a6c9-e0832ca7c189.png)
출처: https://blog.est.ai/2020/11/ssl/


### 1️⃣ Proxy-label method 

  - Labeled set으로 학습된 모델을 이용해 unlabeled data point들에 label을 달아주는 기법


  - 만약 Labeled set의 분포를 벗어나는 샘플들에는 제대로 된 label을 달아주기 어렵기 때문에 성능향상에 한계가 있다는 단점이 있음. 


  - 그래도 Labeled set 분포 내의 샘플들에 대해 interpolation하는 효과가 있기때문에 아직도 많이 사용되는 기법임. 

  #### 📌 Method 1. Pseudo Label (13')
  ![image](https://user-images.githubusercontent.com/67623921/209645395-273502dc-389f-4c1c-a29f-5c8441e0bdf2.png)
  출처: https://sanghyu.tistory.com/177


### 2️⃣ Consistency regularization

  - 이 방법은 unlabeled data point에 작은 perturbation을 주어도 예측의 결과에는 일관성이 있을 거라고 가정함. 


  - unlabeled data에 data augmentation을 통해 class가 바뀌지 않을 정도의 변화를 줬을 때, 원 데이터와의 예측결과가 같아지도록 unsupervised loss를 주어 학습하게 됨. 


  - 이를 통해 약간 헷갈리는 샘플들에 대해 class를 유연하게 예측할 수 있도록 해줌. 


  - 성능이 좋은 semi-supervised learning 모델들은 대체로 consistency regularization을 사용하고 있음. 


  #### 📌 Method 2. PI model (16')
  ![image](https://user-images.githubusercontent.com/67623921/209645936-254931a4-4b02-4496-9ef5-089c52d4cc8a.png)
  출처: https://amitness.com/2020/07/semi-supervised-learning/
  
  
  #### 📌 Method 3. VAT(17')
  ![image](https://user-images.githubusercontent.com/67623921/209646055-166bc795-a250-416f-9357-8afd04d3824b.png)
  출처: https://sh-tsang.medium.com/review-virtual-adversarial-training-vat-4b3d8b7b2e92
    
  
  #### 📌 Method 4. Mean Teacher (17')
  ![image](https://user-images.githubusercontent.com/67623921/209646198-4661e185-e44c-4d23-af9f-8960e1eb6f13.png)
  출처: https://velog.io/@injokim/%EC%99%95%EC%B4%88%EA%B8%89-Semi-supervised-learning-%EC%9E%85%EB%AC%B8


  #### 📌 Method 5. ICT (19')
  ![image](https://user-images.githubusercontent.com/67623921/209646639-8695ddbc-e433-4a9f-9884-c1e03f1c245a.png)
  출처: Verma, V., Kawaguchi, K., Lamb, A., Kannala, J., Bengio, Y., & Lopez-Paz, D. (2019). Interpolation consistency training for semi-supervised learning. arXiv preprint arXiv:1903.03825.
  
  
  
### 3️⃣ Holistic methods

  - 여러 semi-supervised learning 기법들을 통합하고 Mixup data augmentatino을 적용하여 성능을 더 끌어 올림.

  #### 📌 Method 6. MixMatch (19')
  ![image](https://user-images.githubusercontent.com/67623921/209646904-61c6481e-7192-4495-9139-a8ed37d9ae9b.png)
  출처: https://rain-bow.tistory.com/entry/Semi-Supervised-Learning-SSL-%EC%86%8C%EA%B0%9C-%EB%B0%8F-%EB%8F%99%ED%96%A5


  
