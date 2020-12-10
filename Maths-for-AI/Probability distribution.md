# 확률 분포(Probability distribution)

+ 확률 변수(random variable)
   + 랜덤한 실험 결과에 의존하는 실수로, 표본공간의 부분집합에 대응하는 실수
   + 예) 주사위 2개를 던지는 실험
      + 주사위 숫자의 합, 차, 두 주사위 숫자 중 같거나 큰 수... 등 : 확률 변수
   + 보통 표본 공간에서 실수로 대응되는 함수로 정의함 (표기는 <img src="https://latex.codecogs.com/gif.latex?X" title="X" />, <img src="https://latex.codecogs.com/gif.latex?Y" title="Y" />처럼 대문자로)
   
   + 값이 이산이나 연속이냐에 따라 **이산확률변수(discrete random variable)** 와 **연속확률변수(continuous random variable)** 로 나눔
   
+ 확률 분포 : 확률변수가 가질 수 있는 값에 대해 확률을 대응시켜주는 관계(그 값들이 어떻게 분배가 되는지)
   + 예) 어떤 확률변수 X가 가질 수 있는 값이 0, 1, 3, 8이라 하면, 각 값이 나올 확률은 다음과 같다.
      + P(X=0)=0.2
      + P(X=1)=0.1
      + P(X=3)=0.5
      + P(X=8)=0.2
      
   + 표, 그래프, 함수... 등으로 확률 분포를 표현
   
   + 예) 주사위 2개를 던지는 실험
      + 확률 변수 X : 주사위 숫자의 합
         + X가 가질 수 있는 값 : 2,3,...,12
         + P(X=12)=1/36
         
      + 확률 변수 Y : 주사위 숫자의 차
         + Y가 가질 수 있는 값 : 0,1,2,...,5
         + P(Y=5)=2/36=1/18
         
      + 주사위를 던질 때마다 확률 변수 값이 달라질 수 있음
      + n번 실험하면, n개의 숫자가 나옴
      + 확률 변수 X도 평균과 분산을 가짐
         + 이를 모집단의 평균과 분산이라 할 수 있음
         
## 이산확률변수
+ 이산확률변수의 확률분포
   + 보통 함수로 주어지며, 확률변수 X가 x라는 값을 가질 확률 => P(X=x)=f(x) : 확률질량함수
   + 예) 확률변수 X가 가질 수 있는 값 : 0,2,5
      + P(X=x)=f(x)=(x+1)/10
         + P(X=0)=0.1
         + P(X=2)=0.3
         + P(X=5)=0.6
         
+ 이산확률변수의 평균(=기대값(expected value))   

   > <img src="https://latex.codecogs.com/gif.latex?E(X)=\sum&space;_{x}xP(X=x)=\sum&space;_{x}xf(x)" title="E(X)=\sum _{x}xP(X=x)=\sum _{x}xf(x)" />   
   
   + 위의 예에서 기대값 <img src="https://latex.codecogs.com/gif.latex?E(X)=0\times&space;0.1&plus;2\times&space;0.3&plus;5\times&space;0.6=3.6" title="E(X)=0\times 0.1+2\times 0.3+5\times 0.6=3.6" />   
   
+ 이산확률변수의 분산   
   + <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;X-\mu&space;\right&space;)^{2}" title="\left ( X-\mu \right )^{2}" />의 평균=<img src="https://latex.codecogs.com/gif.latex?Var(X)" title="Var(X)" />   
   
   + <img src="https://latex.codecogs.com/gif.latex?\sigma&space;^{2}=E\left&space;[&space;(X-\mu)^{2}&space;\right&space;]=\sum&space;_{x}\left&space;(&space;x-\mu&space;\right&space;)^{2}P(X=x)=E\left&space;(&space;X^{2}&space;\right&space;)-\left&space;\{&space;E\left&space;(&space;X&space;\right&space;)&space;\right&space;\}^2" title="\sigma ^{2}=E\left [ (X-\mu)^{2} \right ]=\sum _{x}\left ( x-\mu \right )^{2}P(X=x)=E\left ( X^{2} \right )-\left \{ E\left ( X \right ) \right \}^2" />     
   
     > 중간에 제곱부분 풀어서 써보면 마지막 수식이 나옴.   
   
   + 실험을 할 때마다 확률변수의 값이 달라지는데, 그 변동의 정도인 분산을 계산할 수 있음   
      
      > <img src="https://latex.codecogs.com/gif.latex?\sigma&space;^{2}=\frac{1}{N}\sum_{i=1}^{N}\left&space;(&space;x_{i}-\mu&space;\right&space;)^{2}" title="\sigma ^{2}=\frac{1}{N}\sum_{i=1}^{N}\left ( x_{i}-\mu \right )^{2}" />   
      
      + 위의 예에서 100,000번의 실험을 했다면, 분산 <img src="https://latex.codecogs.com/gif.latex?\sigma&space;^{2}" title="\sigma ^{2}" />은 다음과 같다.   
      
         > <img src="https://latex.codecogs.com/gif.latex?\sigma&space;^{2}" title="\sigma ^{2}" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?=\frac{(0-3.6)^{2}\times&space;10,000&space;&plus;&space;(2-3.6)^{2}\times&space;10,000&space;&plus;&space;(5-3.6)^{2}\times&space;10,000}{100,000}" title="=\frac{(0-3.6)^{2}\times 10,000 + (2-3.6)^{2}\times 10,000 + (5-3.6)^{2}\times 10,000}{100,000}" />    
         
         > <img src="https://latex.codecogs.com/gif.latex?=3.24" title="=3.24" />   
         
+ 이산확률분포의 표준편차  
   + 분산의 양의 제곱근 <img src="https://latex.codecogs.com/gif.latex?\sqrt{\sigma&space;^{2}}=\sigma" title="\sqrt{\sigma ^{2}}=\sigma" />, <img src="https://latex.codecogs.com/gif.latex?SD(X)" title="SD(X)" />라고 표현   
  
- - - - - - - -
## 결합확률 분포(Joint probability distribution)
+ 두 개 이상의 확률 변수가 동시에 취하는 값들에 대해 확률을 대응시켜주는 관계
  > 두 개 이상의 사건이 동시에 일어날 확률
     
+ 이를 통해 각 확률변수의 확률분포를 도출 가능 => 주변확률분포(marginal probability distribution)
   
- - - - - - - -
## 공분산(Covariance) 
+ 두 개 이상의 확률변수가 어떤 관계를 갖고 있는지(결합확률을 분석하기 위해)   
      + <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;X-\mu_{X}&space;\right&space;)\left&space;(&space;Y-\mu_{Y}&space;\right&space;)" title="\left ( X-\mu_{X} \right )\left ( Y-\mu_{Y} \right )" />의 평균   
      
      + <img src="https://latex.codecogs.com/gif.latex?Cov(X,Y)=E\left&space;[&space;(X-\mu_{X})(Y-\mu_{Y})&space;\right&space;]=E(XY)-\mu_{X}\mu_{Y}" title="Cov(X,Y)=E\left [ (X-\mu_{X})(Y-\mu_{Y}) \right ]=E(XY)-\mu_{X}\mu_{Y}" /><img src="https://latex.codecogs.com/gif.latex?=E[XY]-E[X]E[Y]" title="=E[XY]-E[X]E[Y]" />    
      
         > 0에 가까우면 서로 관계 X, 양수나 음수가 나오면 관계 O   
         
      + 예) 고등학년 1학년 학생들
         + 확률변수 X : 키
         + 확률변수 Y : 몸무게
         + 확률변수 Z : 수학성적
         + <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;X-\mu_{X}&space;\right&space;)\left&space;(&space;Y-\mu_{Y}&space;\right&space;)" title="\left ( X-\mu_{X} \right )\left ( Y-\mu_{Y} \right )" /> : 양수일 가능성 높음    
         
         + <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;X-\mu_{X}&space;\right&space;)\left&space;(&space;Z-\mu_{Z}&space;\right&space;)" title="\left ( X-\mu_{X} \right )\left ( Z-\mu_{Z} \right )" /> : 양수, 음수가 될 가능성 반반   
         
           > 위의 두 값이 확률변수이므로 평균과 분산 계산 가능
         
- - - - - - - -
## 상관계수(Correlation coefficient)
+ 공분산은 각 확률 변수의 절대적인 크기에 영향을 받기 때문에, 단위에 관한 영향을 없앨 필요가 있음   
   
   <img src="https://latex.codecogs.com/gif.latex?\rho&space;=Corr(X,Y)=\frac{Cov(X,Y)}{\sigma&space;_{X}\sigma&space;_{Y}}" title="\rho =Corr(X,Y)=\frac{Cov(X,Y)}{\sigma _{X}\sigma _{Y}}" />   
   
   + -1에서 1사이의 값을 가짐
   + -1인 경우 반비례관계이고 1인 경우 비례 관계
   + 0 이면 연관성 X (공분산에서도 마찬가지)   
      
