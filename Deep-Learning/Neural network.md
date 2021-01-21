# 신경망 기초

## 인공신경망(Artificial neural network, ANN)
+ 생물학의 신경망에서 영감을 얻은 통계학적 학습 알고리즘
   + 사람 뇌의 정보처리(뉴런)를 모방   
   
      → 퍼셉트론 고안

+ ANN 구조
   + 노드들의 그룹으로 연결되어있음.
   + 여기서 노드(원)은 인공 뉴런을 나타내고, 화살표는 하나의 뉴런의 출력에서 다른 하나의 뉴런으로의 입력을 나타냄.   
   
      > <img src="https://user-images.githubusercontent.com/72974863/105278335-911bf180-5be8-11eb-9a10-11c14604d6d8.png">   

      > [그림 출처](https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B3%B5_%EC%8B%A0%EA%B2%BD%EB%A7%9D)

+ 다양한 모델이 존재함
   + 전방(forward) 신경망, 순환(recurrent) 신경망, 얕은(shallow) 신경망, 깊은(deep) 신경망
   
   + 결정론적(deterministic) 신경망 : **모델의 매개변수와 조건**에 의해 **출력이 완전히 결정**되는 신경망
   + 확률론적(stochastic) 신경망 : 고유의 임의성을 가지며 매개변수와 조건이 같더라도 **다른 출력**을 가지는 신경망

## 퍼셉트론(Perceptron)
+ 구조 : node, weight, layer과 같은 새로운 개념의 구조 도입
   > <img src="https://user-images.githubusercontent.com/72974863/105280727-d131a300-5bed-11eb-9c2e-57cdbd438758.png">   
   
   > [그림 출처](https://en.wikipedia.org/wiki/Perceptron) 

+ 동작 
   + 선형 연산 → 비선형 연산
      + **선형** : 입력(특징)값과 가중치를 곱하고 더해서 s를 구함
      + **비선형** : 활성함수를 적용
      
+ 원시적 신경망으로, 현대 인공신경망의 중요한 구성 요소가 됨.

+ 일반적인 분류기의 학습과정 ✨
   + 1단계 : **과업 정의**와 분류 과정의 수학적 정의(**가설 설정**)   
      > 퍼셉트론 이용한다면   
      
   + 2단계 : 해당 분류기의 **목적함수 정의**   
      + 목적함수 <a href="https://www.codecogs.com/eqnedit.php?latex=J(\mathbf{w})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(\mathbf{w})" title="J(\mathbf{w})" /></a> 상세 설계
         + 조건 1 : <a href="https://www.codecogs.com/eqnedit.php?latex=J(\mathbf{w})\geq&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(\mathbf{w})\geq&space;0" title="J(\mathbf{w})\geq 0" /></a>   
         + 조건 2 : **w**가 최적이면(모든 샘플을 맞추면) <a href="https://www.codecogs.com/eqnedit.php?latex=J(\mathbf{w})=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(\mathbf{w})=&space;0" title="J(\mathbf{w})= 0" /></a>   
         + 조건 3 : 틀리는 샘플이 많은 **w**일수록 <a href="https://www.codecogs.com/eqnedit.php?latex=J(\mathbf{w})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(\mathbf{w})" title="J(\mathbf{w})" /></a>는 큰 값을 가짐    
                  
                  
          > <a href="https://www.codecogs.com/eqnedit.php?latex=J(\mathbf{w})=\sum_{x_k&space;\in&space;Y}-y_k&space;(\mathbf{w}^T&space;\mathbf{x}_k)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?J(\mathbf{w})=\sum_{x_k&space;\in&space;Y}-y_k&space;(\mathbf{w}^T&space;\mathbf{x}_k)" title="J(\mathbf{w})=\sum_{x_k \in Y}-y_k (\mathbf{w}^T \mathbf{x}_k)" /></a>   
      
          > Y는 **w**가 틀리는 샘플의 집합
         
          > 상세 조건 1,2,3 모두 만족 → 퍼셉트론의 목적함수로 적합    
      
   + 3단계 : **목적함수를 최소화하는 파라미터**를 찾기 위한 **최적화 방법 수행**   
      > 경사하강법을 통해 반복 탐색해서 극값을 찾음
   





