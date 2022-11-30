## ✍ 4번째 튜토리얼 "Ensemble Learning"

### 목차
1. Ensemble Learning
2. Bagging : `DecisionTreeClassifier`,  `BaggingClassifier`
4. Boosting : `AdaBoostClassifier`,  `GradientBoostingClassifier`,  `XGBClassifier`

#### 1. Ensemble Learning
![image](https://user-images.githubusercontent.com/67623921/204856410-36153ee9-868f-43f6-bf83-e511167efb8d.png)

#### 2. Bagging
: 데이터를 가방(bag)에 쓸어 담아 복원 추출하여 여러 개의 표본을 만들어 이를 기반으로 각각의 모델을 개발한 후에 결과를 하나로 합쳐 하나의 모델을 만들어 내는 것

`DecisionTreeClassifier` 하이퍼 파라미터

: min_samples_split, min_samples_leaf, max_features, max_depth

→ 최적의 하이퍼 파라미터 
![image](https://user-images.githubusercontent.com/67623921/204857385-a8b1363b-62e5-4d1b-aff0-56504a6a4433.png)

