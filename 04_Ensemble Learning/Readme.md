## ✍ 4번째 튜토리얼 "Ensemble Learning"

### <목차>
1. Ensemble Learning
2. Bagging : `DecisionTreeClassifier`,  `BaggingClassifier`
4. Boosting : `AdaBoostClassifier`,  `GradientBoostingClassifier`,  `XGBClassifier`

## 1. Ensemble Learning
![image](https://user-images.githubusercontent.com/67623921/204856410-36153ee9-868f-43f6-bf83-e511167efb8d.png)

## 2. Bagging
: 데이터를 가방(bag)에 쓸어 담아 복원 추출하여 여러 개의 표본을 만들어 이를 기반으로 각각의 모델을 개발한 후에 결과를 하나로 합쳐 하나의 모델을 만들어 내는 것

![image](https://user-images.githubusercontent.com/67623921/204858446-dee5014d-4414-4b4c-bb78-b107db978a7f.png)


✔ `DecisionTreeClassifier`의 hyper-parameter : min_samples_split, min_samples_leaf, max_features, max_depth ...

→ 최적의 hyper-parameter 조합

![image](https://user-images.githubusercontent.com/67623921/204857385-a8b1363b-62e5-4d1b-aff0-56504a6a4433.png)

✔ `BaggingClassifier`의 hyper-parameter : n_estimators, max_samples, bootstrap ...

→ 최적의 hyper-parameter 조합

![image](https://user-images.githubusercontent.com/67623921/204858551-2aaa6437-5d69-4e60-97f1-79ffb3599db9.png)



## 3. Boosting
: 부스팅은 틀린 문제를 노트에 적고 이것들에 집중을 하는 목적의 오답노트와 비슷한 개념으로 생각하면 되는데 즉, 틀린 케이스에 가중치를 줌으로써 이를 해결하는 것에 초점을 맞추는 모델

![image](https://user-images.githubusercontent.com/67623921/204859577-fa5915e3-ea56-4c49-8ad8-6ef88d8f2b21.png)


✔ `AdaBoostClassifier`의 hyper-parameter : n_estimators, learning_rate ...

→ 최적의 hyper-parameter 조합

![image](https://user-images.githubusercontent.com/67623921/204859882-8ae71714-3010-4400-91cc-b42769508551.png)


✔ `GradientBoostingClassifier`의 hyper-parameter : n_estimators, learning_rate, max_depth ...

→ 최적의 hyper-parameter 조합

![image](https://user-images.githubusercontent.com/67623921/204860153-32075633-6006-464d-9d4c-c7885386ee2a.png)

✔ `XGBClassifier`의 hyper-parameter : max_depth, min_child_weight, gamma, subsample, colsample_bytree, reg_alpha...

→ 최적의 hyper-parameter 조합 (5단계)

![image](https://user-images.githubusercontent.com/67623921/204860782-fb4fe93a-b030-45cc-945b-2f97ece46ebe.png)

--------------------------------

😊 자세한 결과 해석 및 출처 tutorial 파일에 있습니다!
