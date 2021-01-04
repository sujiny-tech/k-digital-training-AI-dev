# Intro


## Machine Learning
+ **경험** 을 통해 자동으로 개선하는 컴퓨터 알고리즘의 연구
+ 학습 데이터 : 입력벡터들 <img src="https://latex.codecogs.com/gif.latex?\mathbf{x_{1}},&space;...&space;,&space;\mathbf{x_{N}}" title="\mathbf{x_{1}}, ... , \mathbf{x_{N}}" />, 목표값들 <img src="https://latex.codecogs.com/gif.latex?t_{1},&space;...&space;,&space;t_{N}" title="t_{1}, ... , t_{N}" />   
+ 일반적인 머신러닝 알고리즘의 결과는 목표값을 예측하는 함수 <img src="https://latex.codecogs.com/gif.latex?y(\mathbf{x})" title="y(\mathbf{x})" />    

## 핵심 개념
+ **학습단계(training or learning phase)** : 함수 <img src="https://latex.codecogs.com/gif.latex?y(\mathbf{x})" title="y(\mathbf{x})" />를 학습데이터에 기반해 결정하는 단계
+ **시험 데이터 셋(test set)** : 모델 평가를 위해 사용하는 새로운 데이터
+ **일반화(generalization)** : 모델에서 학습에 사용된 데이터가 아닌 이전에 접하지 못한 새로운 데이터에 대해 올바른 예측을 수행하는 역량
+ **지도학슴(supervised learning)** : target 존재
   + 분류(classification)
   + 회귀(regression)
+ **비지도학습(unsupervised learning)** : target 존재 x
   + 군집(clustering)
   
   
## 다항식 곡선 근사(Polynomial Curve Fitting)
+ 입력벡터 <img src="https://latex.codecogs.com/gif.latex?\mathbf{X}=&space;\left&space;(&space;\mathbf{x_{1}},&space;...&space;,&space;\mathbf{x_{N}}&space;\right&space;)^{T}" title="\mathbf{X}= \left ( \mathbf{x_{1}}, ... , \mathbf{x_{N}} \right )^{T}" />, <img src="https://latex.codecogs.com/gif.latex?\mathbf{t}=&space;\left&space;(t_{1},&space;...&space;,&space;t_{N}&space;\right&space;)^{T}" title="\mathbf{t}= \left (t_{1}, ... , t_{N} \right )^{T}" />   
+ **목표** : 새로운 입력벡터 <img src="https://latex.codecogs.com/gif.latex?\hat{x}" title="\hat{x}" />가 주어졌을 때 목표값 <img src="https://latex.codecogs.com/gif.latex?\hat{t}" title="\hat{t}" />을 예측하는 것
+ **확률이론(probability theory)** : 예측값의 불확실성을 정량화시켜 표현할 수 있는 수학적인 프레임워크를 제공
+ **결정이론(decision theory)** : 확률적 표현을 바탕으로 최적의 예측을 수행할 수 있는 방법론 제공
   
   
  <img src="https://latex.codecogs.com/gif.latex?y(x,\mathbf{w})=w_{0}&plus;w_{1}x&plus;w_{2}x^{2}&plus;&space;...&space;&plus;&space;w_{M}x^{M}=\sum_{j=0}^{M}w_{j}x^{j}" title="y(x,\mathbf{w})=w_{0}+w_{1}x+w_{2}x^{2}+ ... + w_{M}x^{M}=\sum_{j=0}^{M}w_{j}x^{j}" />   
  
   + x : 데이터에서 주어지는 값 (입력)
   + w : 고정되어있는 모델 파라미터 (찾고자하는 값)
   
+ 오차함수(Error Function)   

  <img src="https://user-images.githubusercontent.com/72974863/103495499-50994580-4e7e-11eb-9b91-11f19ecfd285.png" width="30%" height="30%">   
  
+ **과소적합(Under-fitting)** : 학습 대상(훈련 데이터셋)을 충분히 학습하지 못함, 훈련 데이터셋과 시험 데이터셋 모두 성능 저하
   + 모델링을 너무 간단하게 해서 성능이 제대로 나오지 않음
+ **과대적합(Over-fitting)** : 학습 대상(훈련 데이터셋)에 너무 맞춰져있어서 시험 대상(시험 데이터셋)의 성능 저하 
   + 너무 상세하고 복잡한 모델링을 해서 훈련 데이터셋에만 과도하게 정확히 동작함
   + [모델 복잡도](https://ko.d2l.ai/chapter_deep-learning-basics/underfit-overfit.html)

