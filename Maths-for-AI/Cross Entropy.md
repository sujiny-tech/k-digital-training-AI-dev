# 교차 엔트로피(Cross Entropy)

+ 자기정보(Self-information)   

   <img src="https://latex.codecogs.com/gif.latex?i(A)=log_{b}\left&space;(&space;\frac{1}{P(A)}&space;\right&space;)=-log_{b}P(A)" title="i(A)=log_{b}\left ( \frac{1}{P(A)} \right )=-log_{b}P(A)" />   
   
   + Shannon은 확률이 낮은 사건이 정보가 많다고 생각
      > 도둑이 들었는데 개가 짖는 경우보다 도둑이 들었는데 개가 안 짖는 경우 더 많은 정보를 포함
      
      + b=2 :bits
      + b=e :nats
      + b=10 :hartleys  
   
   + 특성
      
      <img src="https://latex.codecogs.com/gif.latex?i(AB)=log_{b}\left&space;(&space;\frac{1}{P(A)P(B)}&space;\right&space;)=log_{b}\frac{1}{P(A)}&plus;log_{b}\frac{1}{P(B)}=i(A)&plus;i(B)" title="i(AB)=log_{b}\left ( \frac{1}{P(A)P(B)} \right )=log_{b}\frac{1}{P(A)}+log_{b}\frac{1}{P(B)}=i(A)+i(B)" />   
      
      + 예) 동전 앞 나올확률 1/8, 뒤 나올확률 7/8
         + i(H) = 3비트, i(T) = 0.193비트
 
   
## 엔트로피(entropy)
+ **자기정보의 평균**   

    <img src="https://latex.codecogs.com/gif.latex?H(X)=\sum_{j}P(A_{j})i(A_{j})=-\sum_{j}&space;P(A_{j})log_{2}P(A_{j})" title="H(X)=\sum_{j}P(A_{j})i(A_{j})=-\sum_{j} P(A_{j})log_{2}P(A_{j})" />   
   
+ 특성  
   
   <img src="https://latex.codecogs.com/gif.latex?0\leq&space;H(X)\leq&space;log_{2}K" title="0\leq H(X)\leq log_{2}K" />    
   
    > 이때 K는 사건의 수
       
+ 활용
   + **평균 비트 수** 표현
   + **데이터 압축**에 사용 가능
   
   
   + 예) 4가지 정보를 표현하는데 필요한 비트 수
      X | P(X) | i(X) | Code
      -- | -- | -- | --
      A | 1/2 | 1 | 0
      B | 1/4 | 2 | 10
      C | 1/8 | 3 | 110
      D | 1/8 | 3 | 111
      > 일반적으로 2비트

      + i(X)를 활용하면, 좀 더 비트 수를 줄일 수 있음
         + 평균 비트 수   
         
            > 1x0.5 + 2x0.25 + 3x0.125 + 3x0.125 = 1.75비트
   

## 교차 엔트로피(Cross Entropy)
+ 학습에 필요한 **손실함수** 로 쓰임

+ 잘못된 확률분포를 사용하게 되면, 실제 최적의 비트수를 사용하지 못하게 됨
   
+ 집합 S상에서 확률분포 P에 대한 확률분포 Q의 교차 엔트로피 <img src="https://latex.codecogs.com/gif.latex?H(P,Q)" title="H(P,Q)" />   
+ 확률분포 P에서 각 사건의 자기정보의 평균   

   <img src="https://latex.codecogs.com/gif.latex?H(P,Q)=\sum_{j}P(A_{j})i(A_{j})=-\sum_{j}log_{2}Q(A_{j})=-\sum_{x\in&space;X}P(x)log_{2}Q(x)" title="H(P,Q)=\sum_{j}P(A_{j})i(A_{j})=-\sum_{j}log_{2}Q(A_{j})=-\sum_{x\in X}P(x)log_{2}Q(x)" />   
    
   + 이 값은 정확한 확률분포 P를 사용했을 때의 비트수(확률P의 엔트로피)보다 크게 됨   
   
      <img src="https://latex.codecogs.com/gif.latex?H(P,Q)=-\sum_{x\in&space;X}P(x)log_{2}Q(x)\geq&space;-\sum_{x\in&space;X}P(x)log_{2}P(x)=H(P)" title="H(P,Q)=-\sum_{x\in X}P(x)log_{2}Q(x)\geq -\sum_{x\in X}P(x)log_{2}P(x)=H(P)" />   
      
      + 같으면 H(P,Q)=H(P)
      + 다르면 H(P,Q)>H(P) 

+ 교차 엔트로피를 이용하면 **두 확률 분포가 얼마나 다른지** 판단 가능
   + 기계학습에서는 주어진 대상이 각 그룹에 속할 확률을 제공
      + 예) 그룹에 속할 확률 [0.8, 0.2]와 정답인 [1.0, 0.0]이 얼마나 다른지 측정

   + 분류문제에서의 손실함수로 활용
      + 제곱 합 : 확률이 다를수록 큰 값을 가짐, (단점) 학습속도가 느림
      + 교차 엔트로피 : 확률이 다를수록 큰 값을 가짐, (장점) 학습속도가 빠름 -> 분류문제에서 이를 많이 사용
      
+ 예) 사건 A,B에 대해 P=[1,0] 인 경우 (A의 확률 1, B의 확률 0)
    + 예측 Q(X)
       + 예측 1. [0.8, 0.2]라는 예측이 되었을 때, (잘 예측한 경우) 
       
          <img src="https://latex.codecogs.com/gif.latex?H(P,Q)=-\sum_{x\in&space;X}P(x)log_{2}Q(x)=-1&space;\times&space;log_{2}0.8=0.3219" title="H(P,Q)=-\sum_{x\in X}P(x)log_{2}Q(x)=-1 \times log_{2}0.8=0.3219" />   
          
       + 예측 2. [0.5, 0.5]라는 예측이 되었을 때, (거의 예측한 게 없는 경우)  
          
          <img src="https://latex.codecogs.com/gif.latex?H(P,Q)=-\sum_{x\in&space;X}P(x)log_{2}Q(x)=-1&space;\times&space;log_{2}0.5=1" title="H(P,Q)=-\sum_{x\in X}P(x)log_{2}Q(x)=-1 \times log_{2}0.5=1" />   
          
       + 예측 3. [0.2, 0.8]라는 예측이 되었을 때, (완전히 다르게 예측한 경우) 
          
          <img src="https://latex.codecogs.com/gif.latex?H(P,Q)=-\sum_{x\in&space;X}P(x)log_{2}Q(x)=-1&space;\times&space;log_{2}0.2=2.32" title="H(P,Q)=-\sum_{x\in X}P(x)log_{2}Q(x)=-1 \times log_{2}0.2=2.32" />   
          
   + 따라서 교차엔트로피 값이 **0에 가까울수록** 잘 예측 
    
   
+ A1, A2, A3, A4 사건에 대한 예측 확률값이 [0.7, 0.1, 0.1, 0.1]이며, 정답이 A1인 경우에 대한 교차엔트로피 값 계산    

   ![cross_entropy_1](https://user-images.githubusercontent.com/72974863/101900848-833f7d80-3bf3-11eb-8757-3a8dbfb88b78.png)   
    
