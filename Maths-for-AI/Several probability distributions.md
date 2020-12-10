# 몇 가지 확률분포

## 이항분포(Binomial distribution)
+ 베르누이 시행(Bernoulli trial)
   + **2개의 결과(성공, 실패)** 로 구분하는 실험
      > 예) 동전 던지기
   + 성공의 확률을 p, 실패는 1-p
   + 확률변수 X : n번의 베르누이 시행에서 성공의 횟수
      > =이항확률변수
   + 해당 확률변수(이학확률변수)가 따르는 분포가 이항분포
      
      <img src="https://latex.codecogs.com/gif.latex?f(x)=P[X=x]=\begin{bmatrix}&space;n\\&space;x&space;\end{bmatrix}p^{x}(1-p)^{n-x}" title="f(x)=P[X=x]=\begin{bmatrix} n\\ x \end{bmatrix}p^{x}(1-p)^{n-x}" />   
   
   + 예) 랜덤박스의 뽑기 성공확률이 0.2이다. 3개를 뽑았을 때, 적어도 하나 이상의 성공이 발생학 확률?
      + 1개 이상 성공일 확률 = P[X>=1] = 1-P[X=0]  
      + <img src="https://latex.codecogs.com/gif.latex?P[X\geqslant&space;1]=1-P[X=0]=1-\binom{3}{0}(0.2)^{0}(1-0.2)^{3-0}=1-0.512=0.488" title="P[X\geqslant 1]=1-P[X=0]=1-\binom{3}{0}(0.2)^{0}(1-0.2)^{3-0}=1-0.512=0.488" />   
         
         ```python
         >>> from scipy import stats
         >>> 1-stats.binom.cdf(0, n=3, p=0.2)
         0.4879999999999999
         ```
   
   + 평균 : <img src="https://latex.codecogs.com/gif.latex?E(X)=np" title="E(X)=np" />   
   + 분산 : <img src="https://latex.codecogs.com/gif.latex?Var(X)=np(1-p)" title="Var(X)=np(1-p)" />   
   + 표준편차 : <img src="https://latex.codecogs.com/gif.latex?SD(X)=\sqrt{np(1-p)}" title="SD(X)=\sqrt{np(1-p)}" />   
   
      ```python
      >>> stats.binom.stats(n=3, p=0.2)
      (array(0.6), array(0.48))
      ```

## 정규분포(Normal distribution)
+ **연속확률변수의 확률분포** 
   
   + <img src="https://latex.codecogs.com/gif.latex?P[a\leq&space;X\leq&space;b]=\int_{a}^{b}f(x)dx" title="P[a\leq X\leq b]=\int_{a}^{b}f(x)dx" />   
   
      > 그래프 아래 부분의 넓이가 확률
      
   + 정규분포의 확률밀도함수(probability density function)   
   
      <img src="https://latex.codecogs.com/gif.latex?f(x)=\frac{1}{\sqrt{2\pi&space;\sigma&space;}}e^{\frac{-1}{2}\left&space;(&space;\frac{x-\mu}{\sigma}&space;\right&space;)^{2}}" title="f(x)=\frac{1}{\sqrt{2\pi \sigma }}e^{\frac{-1}{2}\left ( \frac{x-\mu}{\sigma} \right )^{2}}" />   
      
      + 확률변수 X가 정규분포를 따른다 = <img src="https://latex.codecogs.com/gif.latex?X\sim&space;N(\mu,&space;\sigma^{2})" title="X\sim N(\mu, \sigma^{2})" />으로 표현   
   
   
   + <img src="https://latex.codecogs.com/gif.latex?X\sim&space;N(4,3^{2})" title="X\sim N(4,3^{2})" />   
     
      + <img src="https://latex.codecogs.com/gif.latex?P[X\leq&space;4]=P[\frac{X-\mu}{\sigma}\leq&space;\frac{4-\mu}{\sigma}]=P[Z\leq&space;\frac{4-4}{3}]=P[Z\leq&space;0]=0.5" title="P[X\leq 4]=P[\frac{X-\mu}{\sigma}\leq \frac{4-\mu}{\sigma}]=P[Z\leq \frac{4-4}{3}]=P[Z\leq 0]=0.5" />   
        
       ```python
       >>> stats.norm.cdf(4, loc=4, scale=3) #loc:평균, scale:표준편차
       0.5
       ```
             
   + 표준정규확률변수(Standard normal random variable)   
         
      <img src="https://latex.codecogs.com/gif.latex?Z=\frac{X-\mu}{\sigma}" title="Z=\frac{X-\mu}{\sigma}" />   
         
      + 확률변수 Z가 표준정규분포를 따른다 =<img src="https://latex.codecogs.com/gif.latex?Z\sim&space;N(0,1)" title="Z\sim N(0,1)" />으로 표현   
   
   + 예) 어떤 종목의 주가는 전날 종가를 평균으로 하고, 표준편차가 50인 정규분포를 따른다고 한다.
      + 오늘 종가가 1,000원일 때, 내일 주가가 1,100원이상이 될 확률은?
         <img src="https://latex.codecogs.com/gif.latex?P[X\geq&space;1100]=P[Z\geq&space;\frac{1100-1000}{50}]=P[Z\geq&space;2]" title="P[X\geq 1100]=P[Z\geq \frac{1100-1000}{50}]=P[Z\geq 2]" />    
           
         <img src="https://latex.codecogs.com/gif.latex?=1-P[Z\leq&space;2]=1-0.9772=0.0228" title="=1-P[Z\leq 2]=1-0.9772=0.0228" />   
         
         ```python
         >>> 1- stats.norm.cdf(1100, loc=1000, scale=50)
         0.02275013194817921
         ```
         
## 포아송 분포(Poisson distribution) 
+ **일정한 시간 단위 또는 공간 단위** 에서 발생하는 이벤트의 수의 확률분포   
   > 하루 동안 파리바게트를 방문하는 방문자의 수, 어떤 미용실에 한 시간동안 방문하는 손님 수, 어떤 전기선 100미터당 발생하는 결함의 수 등 
         
+ 확률분포함수(확률질량함수)   

   + <img src="https://latex.codecogs.com/gif.latex?P[X=x]=f(x)=\lambda&space;^{x}\frac{e^{-\lambda}}{x!}" title="P[X=x]=f(x)=\lambda ^{x}\frac{e^{-\lambda}}{x!}" /> (x=0,1,2,...)   
   + 평균도 분산도 <img src="https://latex.codecogs.com/gif.latex?\lambda" title="\lambda" />   
   
   + 예) 어떤 웹사이트에 시간당 접속자 수는 평균이 3<img src="https://latex.codecogs.com/gif.latex?(\lambda=3)" title="(\lambda=3)" />인 포아송 분포를 따른다고 한다.
      + 앞으로 1시간 동안 접속자 수가 2명 이하일 확률?
      + x가 0,1,2인 경우의 확률들을 대해 더해주면 0.42319
   
   ```python
   >>> stats.poisson.cdf(2, mu=3) #mu:평균
   0.42319008112684364
   ```

## 지수분포(Exponential distribution)
+ **포아송분포에서 어떤 사건이 발생** 할 때, 어느 한 시점으로부터 이 사건이 발생할 때까지 **걸리는 시간** 에 대한 확률 분포
+ 확률밀도 함수   

   <img src="https://latex.codecogs.com/gif.latex?f(t)=\lambda&space;e^{-\lambda&space;t}" title="f(t)=\lambda e^{-\lambda t}" />   
   
   + 포아송분포의 평균 : <img src="https://latex.codecogs.com/gif.latex?\lambda" title="\lambda" />   
   + 평균   
   
      <img src="https://latex.codecogs.com/gif.latex?E(T)=\frac{1}{\lambda}" title="E(T)=\frac{1}{\lambda}" />
      
   + 분산   
   
      <img src="https://latex.codecogs.com/gif.latex?Var(T)=\frac{1}{\lambda&space;^{2}}" title="Var(T)=\frac{1}{\lambda ^{2}}" />   
   
   
   + 예) 어느 웹사이트에 시간당 접속자 수는 <img src="https://latex.codecogs.com/gif.latex?(\lambda=3)" title="(\lambda=3)" />인 포아송 분포를 따른다.
      + 지금부터 시작하여 첫 번째 접속자가 30분 이내에 나올 확률?   
         
         <img src="https://latex.codecogs.com/gif.latex?P[T\leq&space;0.5]=\int_{0}^{0.5}\lambda&space;e^{-\lambda&space;t}dt=\int_{0}^{0.5}3&space;e^{-3t}dt" title="P[T\leq 0.5]=\int_{0}^{0.5}\lambda e^{-\lambda t}dt=\int_{0}^{0.5}3 e^{-3t}dt" />   
         
         <img src="https://latex.codecogs.com/gif.latex?\left&space;[&space;-e^{-3t}\right&space;]&space;_{0}^{0.5}=1-e^{-1.5}=1-0.2231=0.7769" title="\left [ -e^{-3t}\right ] _{0}^{0.5}=1-e^{-1.5}=1-0.2231=0.7769" />   
   
   ```python
   >>> stats.expon.cdf(0.5, scale=1/3) #표준편차=1/lambda
   0.7768698398515702
   ```

