## ✍ 3번째 튜토리얼 "Anomaly Detection"

#### 🔆 사용한 데이터셋 : CWRU Bearing dataset

### 1️⃣ Anomaly Detection과 Classification 비교
![image](https://user-images.githubusercontent.com/67623921/202409299-0221d96f-e280-4e10-9d6e-9ab107dda0d5.png)


#### → 이상 탐지와 분류 방법의 차이점을 train dataset에서의 각 클래스별 비율을 다르게 하여 실험적으로 증명하였습니다. 

[Classification]
◾ Accuracy: 0.9924631723192874
  
[Anomaly Detection]
◾ Accuracy: 0.2692702980472765
  


### 2️⃣ Anomaly Detection - Autoencoder
![image](https://user-images.githubusercontent.com/67623921/202410130-f8dcf002-b257-423f-bef5-f8ff9686b269.png)
  
#### → 비지도 학습 방법이며 재구성 오차를 통해 이상을 탐지하는 Autoencoder를 사용했습니다.

  ![image](https://user-images.githubusercontent.com/67623921/202410624-a09acb1d-1596-43a1-81c1-1904202c5cd4.png)

  
### 1. Linear Autoencoder
  : Linear 함수로 layer를 구성한 모델
  
  ![image](https://user-images.githubusercontent.com/67623921/202412248-c5a59442-b528-4ac6-9106-abf8eac5c132.png)

  ◾ Accuracy: 0.2692702980472765
  
### 2. Recurrent Autoencoder
  : Recurrent Autoencoder는 시계열 예측에 사용되는 LSTM 모델로 layer를 구성한 모델
  
  ![image](https://user-images.githubusercontent.com/67623921/202412643-9119063e-d592-4e98-bb2f-685516f32ffa.png)

   ◾ F1 Score: 0.9639  |  AUROC: 0.9661 

