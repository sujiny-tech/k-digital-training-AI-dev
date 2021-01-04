# 확률 이론(Probability Theory)
> 머신러닝에 관련된 확률이론 심화내용

## 확률변수(Random Variable)
+ 확률변수 X는 표본의 집합 S의 원소 e를 실수값 X(e)=x에 대응시키는 함수
   + X, Y, ... : 확률변수
   + x, y, ... : 확률변수가 가질 수 있는 값  
   
+ 확률 P는 집합 S의 부분집합을 실수값에 대응시키는 함수
   + P[X=x]
   + P[X<x] ...
   + X=x, X<x 는 집합 S의 부분집합을 정의함.
+ [이전에 정리한 내용 참고 ✨](https://github.com/sujiny-tech/k-digital-training-AI-dev/blob/main/Maths-for-AI/Probability%20distribution.md)

### 연속확률변수(Continuous Random Variables)
+ 누적분포함수(cumulative distribution function, CDF) 
   > <img src="https://latex.codecogs.com/gif.latex?F(x)=P[X\in&space;\left&space;(&space;-\infty,x&space;\right&space;)]" title="F(x)=P[X\in \left ( -\infty,x \right )]" />   
   
+ [확률밀도함수](https://ko.wikipedia.org/wiki/%ED%99%95%EB%A5%A0_%EB%B0%80%EB%8F%84_%ED%95%A8%EC%88%98)(probability density function, pdf) : 확률변수의 분포를 나타내는 함수   
   + 아래의 식을 만족한다면, X는 연속확률변수, f(x)는 X의 확률밀도함수   
   
      > <img src="https://latex.codecogs.com/gif.latex?F(x)=\int_{-\infty&space;}^{x}f(t)dt" title="F(x)=\int_{-\infty }^{x}f(t)dt" />   
   + 확률변수를 명확히 하기 위해 다음과 같이 표기하기도 함   
   
      > <img src="https://latex.codecogs.com/gif.latex?F_{X}(x),&space;f_{X}(x)" title="F_{X}(x), f_{X}(x)" />   
   + 혼란이 없을 경우 <img src="https://latex.codecogs.com/gif.latex?f_{X}(x)" title="f_{X}(x)" /> 대신 <img src="https://latex.codecogs.com/gif.latex?p_{X}(x),&space;p_{x}(x),&space;p(x)" title="p_{X}(x), p_{x}(x), p(x)" /> 사용하기도 함.
   + 확률밀도함수는 0보다 크거나 같은 값을 가지며, 음의 무한대부터 양의 무한대부터 적분했을때 값이 1임
   
### 확률변수의 성질(The Rules of Probability)
+ 덧셈 법칙(sum rule), 곱셈 법칙(product rule), 베이즈 확률(Baeys)...
+ [이전에 정리한 내용 참고✨](https://github.com/sujiny-tech/k-digital-training-AI-dev/blob/main/Maths-for-AI/Probability.md)

👉 **예제** ) <img src="https://latex.codecogs.com/gif.latex?p_{x_{1},x_{2}}\left&space;(&space;x_{1},x_{2}&space;\right&space;)=e^{-&space;\left&space;(&space;x_{1}&plus;x_{2}&space;\right&space;)}" title="p_{x_{1},x_{2}}\left ( x_{1},x_{2} \right )=e^{- \left ( x_{1}+x_{2} \right )}" />, <img src="https://latex.codecogs.com/gif.latex?x_{1}>0,&space;x_{2}>0" title="x_{1}>0, x_{2}>0" />이라고 하자. <img src="https://latex.codecogs.com/gif.latex?y_{1}=x_{1},&space;y_{2}=x_{1}&plus;x_{2}" title="y_{1}=x_{1}, y_{2}=x_{1}+x_{2}" />에 의해서 정의되는 <img src="https://latex.codecogs.com/gif.latex?\mathbf{y}" title="\mathbf{y}" />의 pdf는?   
   + 추가하기 ✏
   
- - - - - - - - - - - - - - - -

### 기댓값(Expectations)
+ 확률분포 p(x)하에서 함수 f(x)의 평균값
+ 이산확률분포(discrete distribution) 
   > <img src="https://latex.codecogs.com/gif.latex?E[f]=\sum_{x}&space;p(x)f(x)" title="E[f]=\sum_{x} p(x)f(x)" />   
   
+ 연속확률분포(continous distribution)
   > <img src="https://latex.codecogs.com/gif.latex?E[f]=\int&space;p(x)f(x)dx" title="E[f]=\int p(x)f(x)dx" />   
   
+ 확률분포로부터 N개의 샘플을 추출해서 기댓값을 근사할 수 있음
   > <img src="https://latex.codecogs.com/gif.latex?E[f]\approx&space;\frac{1}{N}\sum_{n=1}^{N}&space;f(x_{n})" title="E[f]\approx \frac{1}{N}\sum_{n=1}^{N} f(x_{n})" />   

+ 여러개 변수들의 함수 (결합확률분포)
   > <img src="https://latex.codecogs.com/gif.latex?E_{x,y}[f(x,y)]=\sum_{y}&space;\sum_{x}&space;f(x,y)&space;p(x,y)" title="E_{x,y}[f(x,y)]=\sum_{y} \sum_{x} f(x,y) p(x,y)" />   
   
+ 조건부 기댓값(conditional expectation)
   > <img src="https://latex.codecogs.com/gif.latex?E_{x}[f|y]=\sum_{x}&space;f(x)&space;p(x|y)" title="E_{x}[f|y]=\sum_{x} f(x) p(x|y)" />   
   
 ### 분산(variance) & 공분산(covariance)
 + f(x)의 분산 : f(x)의 값들이 기댓값으로부터 흩어져있는 정도
    > <img src="https://latex.codecogs.com/gif.latex?var[f]=E[\left&space;(&space;f(x)-E[f(x)]&space;\right&space;)^{2}]=E[f(x)^{2}]-E[f(x)]^{2}" title="var[f]=E[\left ( f(x)-E[f(x)] \right )^{2}]=E[f(x)^{2}]-E[f(x)]^{2}" />   
    
    > <img src="https://latex.codecogs.com/gif.latex?var[x]=E[x^{2}]-E[x]^{2}" title="var[x]=E[x^{2}]-E[x]^{2}" />   
    
+ 두개의 확률변수 x,y에 관한 공분산(covariance)
   > <img src="https://latex.codecogs.com/gif.latex?cov[x,y]=E_{x,y}[\left&space;\{&space;x-E[x]&space;\right&space;\}\left&space;\{&space;y-E[y]&space;\right&space;\}]=E_{x,y}[xy]-E[x]E[y]" title="cov[x,y]=E_{x,y}[\left \{ x-E[x] \right \}\left \{ y-E[y] \right \}]=E_{x,y}[xy]-E[x]E[y]" />   
       
+ 벡터로 표현하면
   > <img src="https://latex.codecogs.com/gif.latex?cov[\mathbf{x},\mathbf{y}]=E_{\mathbf{x}}[\left&space;\{&space;\mathbf{x}-E[\mathbf{x}]&space;\right&space;\}&space;\left&space;\{&space;\mathbf{y}&space;^{T}-E[\mathbf{y}&space;^{T}]&space;\right&space;\}]=E_{\mathbf{x},\mathbf{y}}[\mathbf{x}\mathbf{y}]-E[\mathbf{x}]E[\mathbf{y}]" title="cov[\mathbf{x},\mathbf{y}]=E_{\mathbf{x}}[\left \{ \mathbf{x}-E[\mathbf{x}] \right \} \left \{ \mathbf{y} ^{T}-E[\mathbf{y} ^{T}] \right \}]=E_{\mathbf{x},\mathbf{y}}[\mathbf{x}\mathbf{y}]-E[\mathbf{x}]E[\mathbf{y}]" />   
   
+ <img src="https://latex.codecogs.com/gif.latex?cov[\mathbf{x}]&space;\equiv&space;cov[\mathbf{x},\mathbf{x}]" title="cov[\mathbf{x}] \equiv cov[\mathbf{x},\mathbf{x}]" />   

- - - - - - - - - 
### 빈도주의(Frequentist) vs 베이지안(Bayesian)
+ 확률 해석의 두 가지 관점
+ **빈도주의(Frequentist)** : 반복가능한 사건들의 빈도수에 기반
+ **베이지안(Bayesian)** : 불확실성을 정량적으로 표현
   + 반복이 불가능한 사건인 경우, 베이지안 관점에서는 이미 알고 있는 정보를 정량적으로 표현하고 관찰 결과들을 바탕으로 해서 불확실성에 대해 업데이트함.
      + 반복하지 않은 사건에 대해서도 확률로 나타낼 수 있음
      
   + **베이지안 입장에서 모델의 파라미터를 어떻게 구할까?** 
      + w에 대한 사전지식 p(w) : **사전확률**
      + 새로운 데이터 D={t1, ... , tn}을 관찰하고 난 뒤의 **조건부확률 p(D|W)** : **우도함수** (likelihood function)
         + 특정 w값에 대해 D의 관찰값이 얼마나 가능성이 있는가
         
      + 새로운 데이터를 관찰하고 난 뒤의 w에 대한 불확실성 : **p(w|D)** 
         > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{w}|D)=\frac{p(D|\mathbf{w})&space;p(\mathbf{w})}&space;{p(D)}" title="p(\mathbf{w}|D)=\frac{p(D|\mathbf{w}) p(\mathbf{w})} {p(D)}" />   
         
      + 사후확률(posterior) ∝ 우도(likelihood) X 사전확률(prior)
      
      + 반면, 빈도주의는 w가 고정된 파라미터이며 최대우도와 같은 '추정자(estimator)'를 사용해서 값을 구함. 구해진 파라미터의 불확실성은 부트스트랩(bootstrap)방법을 써서 구할 수 있음.
      
   + 베이지안 관점의 장점✨      
      + **사전확률을 모델에 포함시킬 수 있음**
      + 극단적인 확률을 피할 수 있음
         + 예) 동전을 던져서 세번 다 앞면이 나올 경우
            + 빈도주의 : 앞면이 나올 확률은 1
            + 베이지안 : 사전 확률을 활용할 수 있기 때문에, 극단적인 확률 피할 수 있음. 
      
- - - - - - - - - - - - - 
### 정규분포(Gaussian Distribution)
+ 단일변수 x를 위한 가우시안 분포
   > <img src="https://latex.codecogs.com/gif.latex?N\left&space;(&space;x|\mu,&space;\sigma^{2}&space;\right&space;)=\frac{1}{\sigma\sqrt{2&space;\pi}}&space;exp&space;\left&space;\{&space;\frac{-1}{2&space;\sigma^{2}}\left&space;(&space;x&space;-&space;\mu&space;\right&space;)^{2}&space;\right&space;\}" title="N\left ( x|\mu, \sigma^{2} \right )=\frac{1}{\sigma\sqrt{2 \pi}} exp \left \{ \frac{-1}{2 \sigma^{2}}\left ( x - \mu \right )^{2} \right \}" />   

+ 정규화(normalization) 증명
   > <img src="https://latex.codecogs.com/gif.latex?I=\int_{\infty}^{-\infty}&space;exp\left&space;(&space;\frac{-1}{2\sigma^{2}}&space;x^{2}&space;\right&space;)dx" title="I=\int_{\infty}^{-\infty} exp\left ( \frac{-1}{2\sigma^{2}} x^{2} \right )dx" />   
   
   > ✏
   
+ 기댓값(Expectation)
   > E[x]=μ ✏

+ 분산(Variance)
   > var[x]=σ^2 ✏

+ 최대우도해(Maximum Likelihood solution)
   + <img src="https://latex.codecogs.com/gif.latex?\mathbf{X}=\left&space;(&space;x_{1},&space;...&space;,&space;x_{N}&space;\right&space;)^{T}" title="\mathbf{X}=\left ( x_{1}, ... , x_{N} \right )^{T}" />가 독립적으로 같은 가우시안분포로부터 추출된 N개의 샘플들이라고 할 때, 
      > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{X}|\mu,&space;\sigma^{2})=p(x_{1},&space;...,&space;x_{N}|\mu,&space;\sigma^{2})=\prod_{n=1}^{N}&space;N(x|\mu,&space;\sigma^{2})" title="p(\mathbf{X}|\mu, \sigma^{2})=p(x_{1}, ..., x_{N}|\mu, \sigma^{2})=\prod_{n=1}^{N} N(x|\mu, \sigma^{2})" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\textup{ln}&space;p(\mathbf{X}|\mu,&space;\sigma^{2})=\frac{-1}{2\sigma^{2}}\sum_{n=1}^{N}&space;\left&space;(&space;x_{n}&space;-&space;\mu&space;\right&space;)&space;^{2}&space;-&space;\frac{N}{2}&space;\textup{ln}\sigma^{2}-\frac{N}{2}&space;\textup{ln}\left&space;(&space;2\pi&space;\right&space;)" title="\textup{ln} p(\mathbf{X}|\mu, \sigma^{2})=\frac{-1}{2\sigma^{2}}\sum_{n=1}^{N} \left ( x_{n} - \mu \right ) ^{2} - \frac{N}{2} \textup{ln}\sigma^{2}-\frac{N}{2} \textup{ln}\left ( 2\pi \right )" />   
      
      > 최대우도해 구하는 부분 추가하기✏   
      
      > <img src="https://latex.codecogs.com/gif.latex?\mu_{ML}=\frac{1}{N}\sum_{n=1}^{N}x_{n}" title="\mu_{ML}=\frac{1}{N}\sum_{n=1}^{N}x_{n}" />   
      
- - - - - - - - - - - - - - - -
### 곡선근사(curve Fitting) : 확률적 관점
+ 학습 데이터
   > <img src="https://latex.codecogs.com/gif.latex?X=\left&space;(&space;x_{1},...,&space;x_{n}&space;\right&space;)^{T},&space;t=\left&space;(&space;t_{1},...,&space;t_{n}&space;\right&space;)^{T}" title="X=\left ( x_{1},..., x_{n} \right )^{T}, t=\left ( t_{1},..., t_{n} \right )^{T}" />   

+ 목표값 t의 불확실성을 다음과 같이 확률분포로 나타냄
   >  <img src="https://latex.codecogs.com/gif.latex?p(t|x,w,\beta)=N(t|y(x,w),&space;\beta&space;^{-1})" title="p(t|x,w,\beta)=N(t|y(x,w), \beta ^{-1})" />   
   
+ 파라미터 
   > <img src="https://latex.codecogs.com/gif.latex?w,&space;\beta" title="w, \beta" />   
   
   + 파라미터들의 최대우도해 구하기
      + 우도 함수
         > <img src="https://latex.codecogs.com/gif.latex?p(t|X,w,\beta)=\prod_{n=1}^{N}N(t_{n}|y(x_{n},&space;w),&space;\beta^{-1})" title="p(t|X,w,\beta)=\prod_{n=1}^{N}N(t_{n}|y(x_{n}, w), \beta^{-1})" />   
         
      + 로그우도함수
         > <img src="https://latex.codecogs.com/gif.latex?\textup{ln}&space;p(t|X,w,&space;\beta)=\frac{-\beta}{2}&space;\sum_{n=1}^{N}&space;\left&space;(&space;y(x_{n},&space;w)&space;-&space;t_{n}&space;\right&space;)&space;^{2}&space;-&space;\frac{N}{2}&space;\textup{ln}\beta-\frac{N}{2}&space;\textup{ln}\left&space;(&space;2\pi&space;\right&space;)" title="\textup{ln} p(t|X,w, \beta)=\frac{-\beta}{2} \sum_{n=1}^{N} \left ( y(x_{n}, w) - t_{n} \right ) ^{2} - \frac{N}{2} \textup{ln}\beta-\frac{N}{2} \textup{ln}\left ( 2\pi \right )" />   
         
   + w에 관해서 우도함수를 최대화시키는 것은 제곱합 오차함수(sum-of-squares error function)을 최소화시키는 것과 동일   
   
   + β의 최대우도해
      > <img src="https://latex.codecogs.com/gif.latex?\frac{1}{\beta_{ML}}=\frac{1}{N}\sum_{n=1}^{N}\left&space;\{&space;y(x_{n},&space;\mathbf{w}_{ML})-t_{n}&space;\right&space;\}^{2}" title="\frac{1}{\beta_{ML}}=\frac{1}{N}\sum_{n=1}^{N}\left \{ y(x_{n}, \mathbf{w}_{ML})-t_{n} \right \}^{2}" />   
      
   + 예측분포(predictive distribution)
      + w, β 대신 최대우도해를 대입해서 확률 구함
         > <img src="https://latex.codecogs.com/gif.latex?p(t|x,&space;\mathbf{w_{ML}},\beta_{ML})=N(t|y(x,\mathbf{w_{ML}}),&space;\beta_{ML}^{-1})" title="p(t|x, \mathbf{w_{ML}},\beta_{ML})=N(t|y(x,\mathbf{w_{ML}}), \beta_{ML}^{-1})" />   
      

   + **다음단계 : 사전 확률** 을 포함해서 ❗
      + 파라미터 w의 사전확률이 주어졌을때, **w의 사후 확률** 은 **우도함수와 사전확률의 곱** 에 비례
         > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{w}|\alpha)=N(\mathbf{w}|\mathbf{0},&space;\alpha^{-1}&space;\mathbf{I})=\left&space;(&space;\frac{\alpha}{2\pi}^{(M&plus;1)/2&space;}&space;\right&space;)exp\left&space;\{&space;\frac{-\alpha}{2}\mathbf{w}^{T}\mathbf{w}&space;\right&space;\}" title="p(\mathbf{w}|\alpha)=N(\mathbf{w}|\mathbf{0}, \alpha^{-1} \mathbf{I})=\left ( \frac{\alpha}{2\pi}^{(M+1)/2 } \right )exp\left \{ \frac{-\alpha}{2}\mathbf{w}^{T}\mathbf{w} \right \}" />   
            
      + 즉, **우도함수와 사전확률의 곱을 최소화** 시키는 것이 **w의 사후확률을 최대화** 시키는 것과 동일
         > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{w}|\mathbf{X},&space;\mathbf{t},&space;\alpha,&space;\beta)\propto&space;p(\mathbf{t}|\mathbf{X},\mathbf{w},&space;\beta)p(\mathbf{w}|\alpha)" title="p(\mathbf{w}|\mathbf{X}, \mathbf{t}, \alpha, \beta)\propto p(\mathbf{t}|\mathbf{X},\mathbf{w}, \beta)p(\mathbf{w}|\alpha)" />   
      
      + 이는 **규제화된 제곱합 오차함수를 최소화** 시키는 것과 동일(λ=α/β)
         > <img src="https://latex.codecogs.com/gif.latex?\frac{\beta}{2}\sum_{n=1}^{N}\left&space;\{&space;y(x_{n},&space;\mathbf{w})-t_{n}&space;\right&space;\}^{2}&space;&plus;&space;\frac{&space;\alpha&space;}{2}&space;\mathbf{w}^{T}&space;\mathbf{w}" title="\frac{\beta}{2}\sum_{n=1}^{N}\left \{ y(x_{n}, \mathbf{w})-t_{n} \right \}^{2} + \frac{ \alpha }{2} \mathbf{w}^{T} \mathbf{w}" />   
      
      
   + **최종단계 : 완전한 베이지안 곡선근사** 
      + 이제까지의 t의 예측분포를 구하기 위해 여전히 **w의 점추정에 의존해왔음** 
      + **완전한 베이지안 방법**은 **w의 분포로부터 확률의 기본법칙만을 사용** 해서 **t의 예측분포를 유도** 함.
        > <img src="https://latex.codecogs.com/gif.latex?\textup{ln}&space;p(t|X,w,t)=\int&space;p(t|x,w)p(w|X,t)dw" title="\textup{ln} p(t|X,w,t)=\int p(t|x,w)p(w|X,t)dw" />   
     
        > 이 예측분포도 가우시안 분포라는 점과 그 분포의 평균벡터와 공분산행렬을 구하는 방법은 다음 강의에 ❗


