## ✍ 5번째 튜토리얼 "Semi-Supervised Learning"

  ✔ 적은 labeled data가 있으면서 추가로 활용할 수 있는 대용량의 unlabeled data가 있을 때

  ✔ 소량의 labeled data에는 supervised learning을 적용하고 unlabeled data에는 unsupervised learning을 적용해 추가적인 성능향상을 목표로 함.

  ✔ 데이터 자체의 본질적인 특성이 모델링 된다면 소량의 labeled data를 통한 약간의 가이드로 일반화 성능을 끌어올릴 있음. 

![image](https://user-images.githubusercontent.com/67623921/209644289-622ed290-b74a-4d6e-a6c9-e0832ca7c189.png)
출처: https://blog.est.ai/2020/11/ssl/


## 1️⃣ Proxy-label method 

  - Labeled set으로 학습된 모델을 이용해 unlabeled data point들에 label을 달아주는 기법


  - 만약 Labeled set의 분포를 벗어나는 샘플들에는 제대로 된 label을 달아주기 어렵기 때문에 성능향상에 한계가 있다는 단점이 있음. 


  - 그래도 Labeled set 분포 내의 샘플들에 대해 interpolation하는 효과가 있기때문에 아직도 많이 사용되는 기법임. 

  ### 📌 Method 1. Pseudo Label (13')
  ![image-2.png](attachment:image-2.png)
