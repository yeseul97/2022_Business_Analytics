## 2️⃣ Support Vector Machine (SVM)



  ✅ **실험은 총 6가지 세팅으로 진행한다** ✅

    ✔ 1,2,3번 실험 : 원본 데이터에 서로 다른 3가지 kernel 함수를 적용한 모델 3가지 

    ✔ 4,5,6번 실험 : 원본 데이터에 PCA를 적용하여 차원을 축소한 뒤 3가지 kernel 함수를 적용한 모델 3가지
    
 
 
 [<실험 1>] (https://github.com/yeseul97/2022_Business_Analytics/blob/main/02_Support%20Vector%20Machine/%EC%8B%A4%ED%97%98%201)%20Cancer%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20.ipynb)
      
      - 사용한 데이터셋
        ➡ Cancer Data
      - 데이터 구조 
        ➡ Shape: (569,30), Target: 양성/음성 ( binary class)


    <실험 2>
    
https://github.com/yeseul97/2022_Business_Analytics/blob/main/02_Support%20Vector%20Machine/%EC%8B%A4%ED%97%98%202)%20fetch_lfw_people%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20.ipynb
      - 사용한 데이터셋
        ➡ Fetch 이미지 Data
      - 데이터 구조 
        ➡ Shape: (1348,2914), Target: 8가지 ➡ 변수도 많고 타겟도 많은 경우


    
 
 
 
  ✔ **예상**
  
    - RBF kernel이 가장 성능이 좋을 것이다. (데이터가 많고 튜닝을 했기 때문에)

    - PCA를 적용하면 아무래도 정보가 손실되기 때문에, PCA를 적용하지 않은 SVM 모델이 성능면에서는 더 좋을 것이다. 

    - 이미지처럼 차원수가 많은 경우 PCA가 성능 향상 또는 속도에 영향을 줄 것이다. 
  
  
  
  ✔ **결과**
  
  **<실험 1>**
  
    ![image](https://user-images.githubusercontent.com/67623921/199640720-3e938c2f-2d58-47fb-b84b-8c48e004fe72.png)  
  
    - ACC, Precision, F1_score 측면에서는 모두 RBF가 좋은 성능을 보였다.
    
    - 테이블 데이터의 경우 변수가 많지 않아 차원 축소(PCA)를 하지 않은 데이터들이 더 성능이 좋음을 입증했다.
    
    - 다만 Recall 측면에서 Polynomial이 가장 좋은 성능을 보였다.
    
    - 이를 시각화해서 보면 RBF가 학습 데이터에 너무 overfitting 되어서 그런게 아닐까 추측한다. 
    
      ![image](https://user-images.githubusercontent.com/67623921/199641216-01fb78f2-e23f-4ab0-9236-a214cd21fecf.png)

  
  **<실험 2>**
  
    ![image](https://user-images.githubusercontent.com/67623921/199640733-177ec7e0-e122-441c-a787-832f96d15ec7.png)

    - Precision, Recall, F1_score 측면에서 모두 RBF가 좋은 성능을 보였다.
    
    - 이미지 데이터의 경우 차원 수가 많아 PCA 한 것과 기본 SVM을 적용한 것의 성능 차이는 유사했다.
    
    - 그러므로 이미지 데이터처럼 차원 수가 많은 경우, PCA를 적용한 후 SVM을 적용하는 것도 유의미할 것이라 생각한다. 
