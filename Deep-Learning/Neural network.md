# 신경망 기초

## 인공신경망(Artificial neural network, ANN)

<details>
<summary>자세히</b></summary>   
<div markdown="1">   

+ 생물학의 신경망에서 영감을 얻은 통계학적 학습 알고리즘
   + 사람 뇌의 정보처리(뉴런)를 모방   
   
      → 퍼셉트론 고안

+ 구조
   + 노드들의 그룹으로 연결되어있음.
   + 여기서 노드(원)은 인공 뉴런을 나타내고, 화살표는 하나의 뉴런의 출력에서 다른 하나의 뉴런으로의 입력을 나타냄.   
   
      > <img src="https://user-images.githubusercontent.com/72974863/105278335-911bf180-5be8-11eb-9a10-11c14604d6d8.png">   

      > [그림 출처](https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B3%B5_%EC%8B%A0%EA%B2%BD%EB%A7%9D)

+ 다양한 모델이 존재함
   + 전방(forward) 신경망, 순환(recurrent) 신경망, 얕은(shallow) 신경망, 깊은(deep) 신경망
   
   + 결정론적(deterministic) 신경망 : **모델의 매개변수와 조건**에 의해 **출력이 완전히 결정**되는 신경망
   + 확률론적(stochastic) 신경망 : 고유의 임의성을 가지며 매개변수와 조건이 같더라도 **다른 출력**을 가지는 신경망

</div>
</details>


## 퍼셉트론(Perceptron)

<details>
<summary> 자세히 </summary>   
<div markdown="1"> 
   
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
   

+ 퍼셉트론 학습 알고리즘
   + stochastic version
      + 샘플 순서 섞고, 틀린 샘플 발생하는 즉시 매개변수 갱신  
   
      + 실험으로 더 좋은 성능이 입증 → 현대 기계학습은 이 버전을 채택하였음.
      
   + batch version
      + batch로 확장해도 동일(틀린샘플을 모두 모아 한꺼번에 매개변수 갱신)
   
   
   + 선형 분류기(linear classifier) 한계
      > 즉, 직선 하나로 나눈 영역만 표현가능함.
      
      > 예를 들어, XOR 문제에서 75% 정확도 한계가 존재 (퍼셉트론으로 XOR 게이트 표현 X) ❗

</div>
</details>

## 다층 퍼셉트론
+ 쉽게 생각하면, **여러 퍼셉트론을 쌓은 것** 

+ **핵심 아이디어** ✨
   + **은닉층** (= 특징 추출기)
      > 원래 특징 공간을 분류하는 데 훨씬 **유리한 새로운 특징 공간**으로 변환 ❗   
      
      > 은닉 노드가 너무 크면 과잉적합, 너무 작으면 과소적합 → 따라서 적절히 조절해줘야함 (hyper-parameter 최적화 필요) ⭐   
      
      > 현대 기계학습에서는 **특징학습**(feature learning or data-driven features)이라 부름   
      
      
   + **시그모이드 활성함수** 도입
      > 퍼셉트론에서 경성(hard) 의사결정에 해당하는 계단함수를 활성함수로 사용하였음 ❗   
      
      > 반면, 다층 퍼셉트론은 연성(soft) 의사결정이 가능한 시그모이드 함수를 사용. (더 융통성있게 의사결정 가능 ❗)
      
   + **오류 역전파 알고리즘** 사용
      > 역방향으로 진행하면서 한번에 한 층씩 gradient 계산하고 가중치 갱신하는 알고리즘 ❗  
      
+ 퍼셉트론 2개의 병렬 결합을 통해 XOR 문제 해결 가능 ❗
   > 원래 공간을 **새로운 특징 공간으로 변환** (새로운 특징 공간에서 선형 분리 가능)
      
   > 단층 퍼셉트론으로 표현하지 못한 것을 층을 하나 늘려 구현할 수 있음.
   
   > 즉, **펴셉트론의 병렬결합**을 통해 **선형 분리** 
      
   + 다층 퍼셉트론의 용량
      > **p개의 퍼셉트론을 결합**하면, **P차원 공간으로 변환** 
      
      > <img src="https://user-images.githubusercontent.com/72974863/105579024-37255280-5dc7-11eb-8baf-3392ffb81a24.png" width="70%" height="70%">   
            
      > [그림 출처 & 참고하기 👍](http://www.aistudy.com/neural/MLP_kim.htm) 
      
+ 기본 구조 
   + 범용적 근사 이론(universal approximation theorem)
      + 하나의 은닉층은 함수의 근사를 표현
      + 따라서, 다층 퍼셉트론도 **공간을 변환하는 근사함수**로 생각 ⭐
      
      + Hornik 주장[1989] - **은닉노드가 충분히 많다면**, 어떤 활성함수를 사용하든 표준 다층 퍼셉트론은 **어떤 함수**라도 원하는 정확도만큼 **근사화**할 수 있다고 주장 
      
   
   + 얕은 은닉층의 구조
      + 지수적으로 더 넓은 폭이 필요할수 있음
      + 더 과잉적합 되기 쉬움 
      + 따라서, 일반적으로 **깊은 은닉층의 구조**가 **좋은 성능**을 가짐 ⭐   
      
   
   > <img src="https://user-images.githubusercontent.com/72974863/105579782-f419ae00-5dcb-11eb-943c-5c42f7b2080d.png">   
   
   
   > [이미지 출처](https://zetawiki.com/wiki/%EB%8B%A4%EC%B8%B5_%ED%8D%BC%EC%85%89%ED%8A%B8%EB%A1%A0)
   
 
+ **활성함수**       
   + **활성함수**에 따른 **다층 퍼셉트론의 공간 분할 능력 변화** (경성 부분 변화) ⭐   
   
   + 다양한 활성함수 ✨   
   
   > <img src="https://user-images.githubusercontent.com/72974863/105579188-4f49a180-5dc8-11eb-8795-4b1cb658216a.png" width="120%" height="120%">   
   
   > [참고하기 - wiki](https://en.wikipedia.org/wiki/Activation_function)   
   
   + 대표적인 비선형 함수로 **s자 모양의 sigmoid**를 사용
   + logistic sigmoid, tanh : 위의 그림 기준으로 x의 계수가 커질수록 계단함수에 가까워짐
   
   + 활용 예 
      + 퍼셉트론 - 계단함수
      + 다층 퍼셉트론 - logistic sigmoid & tanh (logistic sigmoid 많이 사용)
         > s자 모양의 넓은 포화곡선은 오류역전파(경사도 기반 학습)를 어렵게 함 💥   
         
         > 따라서, 깊은 신경망에서 ReLU 활용 ⭐   
         
      + 심층학습 - ReLU(Rectified Linear Activation)
   
+ 다층 퍼셉트론 시각화
   > [playground.tensorflow.org - 아주 좋은 사이트 👍](http://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.53349&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)   
   
+ 오류 역전파 알고리즘의 빠른 속도 ✨
   + 오류역전파 : 전방 계산 대비 약 1.5~2배의 시간요소 (비교적 빠름) 
      
   + 오류 역전파를 **반복**하여 **점근적 시간 복잡도**는 **Θ((cp+dp))nq)**
      > c : 분류 수, d : 특징 차원, p : 은닉층 차원, n : 훈련 집합 크기, q: epoch 수
      
+ **성능 향상을 위한 경험의 중요성** 💫 
   + 순수한 최적화 알고리즘으로는 높은 성능 불가능함.
   
   + 중요 쟁점 ⭐
      + **아키텍처** : 은닉층과 은닉 노드 개수 정해야함.
      + **초깃값** : 가중치 초기화 (일반적으로 난수 생성해서 사용하는데 이때 범위와 분포가 중요)
      + **학습률** : adaptive하게 learning rate를 조절하는 방법도 사용하기도 함
      + **활성함수** : 초창기 다층 퍼셉트론은 logistic sigmoid or tanh 사용하였지만, 은닉층 개수 증가에 따라 가중치 소멸과 같은 문제 발생. 따라서 깊은 신경망은 주로 ReLU 사용 (여러가지 ReLU 함수가 있음)  
      
