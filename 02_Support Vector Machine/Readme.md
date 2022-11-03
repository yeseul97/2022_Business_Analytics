## 2️⃣ Support Vector Machine (SVM)



  ✅ **실험은 총 6가지 세팅으로 진행한다** ✅

    ✔ 1,2,3번 실험 : 원본 데이터에 서로 다른 3가지 kernel 함수를 적용한 모델 3가지 

    ✔ 4,5,6번 실험 : 원본 데이터에 PCA를 적용하여 차원을 축소한 뒤 3가지 kernel 함수를 적용한 모델 3가지
    
    
    
    <실험 1>
    - 사용한 데이터셋
      ➡ Cancer Data
    - 데이터 구조 
      ➡ Shape: (569,30), Target: 양성/음성 ( binary class)


    <실험 2> 
    - 사용한 데이터셋
      ➡ Fetch 이미지 Data
    - 데이터 구조 
      ➡ Shape: (1348,2914), Target: 8가지 ➡ 변수도 많고 타겟도 많은 경우


    
 
 
 
  ✔ 예상
  
    - RBF kernel이 가장 성능이 좋을 것이다. (데이터가 많고 튜닝을 했기 때문에)

    - PCA를 적용하면 아무래도 정보가 손실되기 때문에, PCA를 적용하지 않은 SVM 모델이 성능면에서는 더 좋을 것이다. 

    - 이미지처럼 차원수가 많은 경우 PCA가 성능 향상 또는 속도에 영향을 줄 것이다. 
  
  
  
  ✔ 결과
  
  <실험 1>
  
  ![image](https://user-images.githubusercontent.com/67623921/199640397-5e76082c-d038-4840-913a-b9f1ac0d8179.png)
  
  
  
  <실험 2>
  
  ![image](https://user-images.githubusercontent.com/67623921/199640432-47df5bed-2962-475a-9977-eee55c20cd77.png)

  
  
