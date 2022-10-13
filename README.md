2022_Business_Analytics

# Ch1. 차원 축소 
![image](https://user-images.githubusercontent.com/67623921/195076458-b650b386-e4d5-4da8-98fe-46119ec53ba0.png)


### 1. 특성 선택 (feature selection)
**: 원본 특성에서 일부 선택**


- <u>순차 특성 선택</u> (sequential feature selection) 또는 <u>탐욕적 탐색 알고리즘</u> (greedy search algorithm)

    : 초기 d차원의 특성 공간을 k<d인 k차원의 특성 부분 공간으로 축소
    
    
- [순차 후진 선택](https://github.com/yeseul97/2022_Business_Analytics/blob/main/Code/1.%20%ED%9B%84%EC%A7%84%20%EC%A0%9C%EA%B1%B0%EB%B2%95.ipynb) (Sequential Backward Selection, SBS)

    : 모델 성능을 최대한 희생하면서 초기 특성의 부분 공간으로 차원 축소 
    
    
    
    
### 2. 특성 추출 (feature extraction)
**: 일련의 특성에서 얻은 정보로 새로운 특성 만듦**

- [PCA](https://github.com/yeseul97/2022_Business_Analytics/blob/main/Code/2.%20PCA.ipynb) (Principle Component Analysis)


- [LDA](https://github.com/yeseul97/2022_Business_Analytics/blob/main/Code/3.%20LDA.ipynb) (Linear Discriminant Analysis)


- [ISOMAP](https://github.com/yeseul97/2022_Business_Analytics/blob/main/Visualization/2.%20ISOMAP%20-%20MNIST%20data.ipynb) 


- [LLE](https://github.com/yeseul97/2022_Business_Analytics/blob/main/Visualization/3.%20LLE%20-%20swiss%20roll.ipynb) (Locally Linear Embedding)


- [t-SNE](https://github.com/yeseul97/2022_Business_Analytics/blob/main/Visualization/4.%20t-SNE%20-%20MNIST%20dataset.ipynb) (t-distributed stochastic neighbor embedding)


- [UMAP](https://github.com/yeseul97/2022_Business_Analytics/blob/main/Visualization/5.%20UMAP%20-%20MNIST%20dataset.ipynb) (Unifom Manifold Approximation and Projection)
