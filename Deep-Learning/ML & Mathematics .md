# 머신러닝(기계학습)과 수학

> 확률, 선형대수학 - 이전 배움 기록에 부족한 내용 추가하기 ✨

## 정보이론(Information Theory)

+ 정보이론 관점에서도 기계학습 접근 가능
   + **불확실성을 정량화**하여 정보이론 방법을 기계학습에 활용한 예
      > ex) **엔트로피(Entropy), 교차엔트로피(Cross-Entropy), KL 발산(Kullback-Leibler divergence)**
      
      > 어떤 사건이 가지는 불확실성을 정량화시켜서 얼마만큼 엔트로피를 가지느냐 (정보를 얼마나 가질수있는지) 판단 
      
   + 정보이론의 핵심 : **잘 일어나지 않는 사건(unlikely event)의 정보량이 자주 발생하는 사건의 정보량보다 많다(informative).** ‼
      + **확률이 작을수록 많은 정보를 가짐** 
         > ex) ```"아침에 해가 뜬다"```  vs **```"오늘 아침에 일식이 있었다"```** : 잘 일어나지 않는 사건의 정보량이 많음
        
        
+ 정보의 단위(크기)를 측정하는 방법
   
   + 자기 정보(self information)
      + 한 사건의 정보량
         
         > <img src="https://latex.codecogs.com/gif.latex?I(x)=-\textup{log}_2&space;P(x)" title="I(x)=-\textup{log}_2 P(x)" />      
            
         > 단위 : 밑이 2 → 비트(bit) / 자연상수 e → 나츠(nat)    
            
   + 엔트로피(=Shannon entropy)
      + **모든 사건의 정보량의 기대값**(확률변수 x의 불확실성을 나타냄)
         > <img src="https://latex.codecogs.com/gif.latex?H(P)=H(x)=E_{X\sim&space;P}[I(x)]=E_{X\sim&space;P}[-\textup{log}_2&space;P(x)]" title="H(P)=H(x)=E_{X\sim P}[I(x)]=E_{X\sim P}[-\textup{log}_2 P(x)]" />   
            
         > 전체 사건의 확률분포의 불확실성의 양을 나타낼 때 쓰임, 즉 해당하는 확률변수가 얼마만큼의 정보량을 가질 수 있는지 판단하는 지표 ❗
            
      + 모든 사건이 동일한 확률을 가질 때, 불확실성이 가장 높음 (엔트로피 ↑)   
       
   + 교차 엔트로피
      + **두 확률분포 P와 Q가 얼마나 정보를 공유하고 있는가**  
            
         > <img src="https://latex.codecogs.com/gif.latex?H(P,Q)=H(P)&plus;\sum_{x}&space;P(x)\textup{log}_2\frac{P(x)}{Q(x)}" title="H(P,Q)=H(P)+\sum_{x} P(x)\textup{log}_2\frac{P(x)}{Q(x)}" />   
           
         > = P의 엔트로피 + P와 Q의 KL 발산(```KL(P||Q)```)
            
         > 실제 데이터 분포 P(x)는 학습과정에서 변하지 않음.   
            
      + 즉, 실제 데이터 분포 P(x)와 추정한 데이터 분포 Q(x) 간의 거리(차이)를 최소화 = 교차 엔트로피 최소화 ⭐   
            
      + deep learning의 손실함수로 많이 사용 
         
---------------------------------

## 최적화

+ 기계학습의 최적화 : 훈련집합에 따라 정해지는 **목적함수의 최저점에 도달하게하는 모델의 매개변수**를 찾는 것 

   + 주로 **확률론적 경사하강법(Stochastic gradient descent, SGD)** 사용
   
   + **적절한 모델(가설) 선택**과 **목적함수를 정의**하고 **모델의 매개변수 공간을 탐색**하여 **목적함수가 최저가 되는 최적점**을 찾는 전략 

      > 목적합수를 최소로 하는 최적해 찾는 것 
      
      > <img src="https://latex.codecogs.com/gif.latex?\hat{\bf{\Theta}}&space;=&space;\textup{argmin}_{\bf&space;\Theta}&space;J(\bf&space;\Theta)" title="\hat{\bf{\Theta}} = \textup{argmin}_{\bf \Theta} J(\bf \Theta)" />    
         
      > <img src="https://latex.codecogs.com/gif.latex?\Theta&space;,&space;J(\Theta)" title="\Theta , J(\Theta)" /> : 매개변수, 목적함수

+ 최적화 문제 해결

   + 낱낱탐색(exhaustive search) 알고리즘
      + 차원 조금만 높아져도 적용 불가능
      
   + 무작위탐색(random search) 알고리즘
      + 아무 전략 없는 알고리즘
      
   + 미분에 의한 최적화 ⭐
      + 목적함수의 최저점(작아지는 방향)을 미분으로 찾아냄 - **경사 하강 알고리즘의 핵심 원리**
      + 매개변수가 많으니까 편미분 사용
      
         + 행렬 1차 편도 미분 -> 야코비언 행렬(Jacobian matrix)
         + 행렬 2차 편도 미분 -> 헤세 행렬(Hessian matrix)
      
+ 경사 하강 알고리즘
   + 경사 하강법(gradient descent)
      + 함수의 기울기(경사)를 구해서 기울기 낮은쪽으로 반복적으로 이동 → 최소값 도달   
      
   + 집단(batch) 경사 하강 알고리즘
      + 샘플의 기울기 구해서 평균해서 **한꺼번에 갱신**
      + 훈련집합 전체를 다 봐야 갱신이 일어나므로, 정확한 방향으로 수렴하지만 학습 과정이 오래 걸림 
         
   + 확률론적 경사 하강 알고리즘(SGD)
      + **한 샘플(mini-batch)의 경사도** 계산한 후 **즉시 갱신**
      + 한 샘플 뽑아서 경사도 구해서 갱신한게 1 epoch
      + 수렴하는데에 좀 헤맬수 있으나 빠름
      
   + 확률론적 경사 하강법 + 추가 제어 알고리즘
      + optimizer 종류 : Momentum, Adam, Adagrad...
         <details>
         <summary>자세히</summary>   
         <div markdown="1"> 
         
         + SGD : 기울어진 방향으로 일정 거리만 가겠다는 단순한 방법
            > hypter parameter : lr(learning rate)   
            
            + 무작정 기울어진 방향으로 진행해서 비효율적으로 탐색 
            
         + Momentum : 경사 하강법 + 관성
            > hypter parameter : lr, momentum 계수(default 0.9)
            
            + 기울기 방향에 이전 이동을 고려해 탐색(SGD에 비해 지그재그 정도가 덜함)
            + 즉, 기울기 방향이 변경되어도 이전 방향과 크기에 영향을 받음
            
         + Adagrad : 각각의 매개변수에 대해 adaptive하게 학습률(lr) 조정하면서 학습진행
            > hypter parameter : lr
            
            + 학습을 진행할수록 갱신 강도가 약해짐. 학습이 진행됨에 따라 변화폭이 눈에 띄게 줄어 움직이지 않게 됨(이를 개선한 기법-RMSProp)
            
         + Adam : AdaGrad + Momentum
            > hypter parameter : lr, beta1, beta2 (1,2차 모멘텀용 게수 default : 0.9, 0.999)   
            
            > beta1:momentum term / beta2:adaptive term
            
         </div>
         </details>
         
      > <img src="https://user-images.githubusercontent.com/72974863/105182462-65f5bb80-5b70-11eb-9012-c4d7a74e0e29.png" width="70%" height="70%">    
      
      > 출처 : https://www.slideshare.net/yongho/ss-79607172 
      


