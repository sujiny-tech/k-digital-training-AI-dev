## 밀도 추정(Density Estimation)

+ **밀도추정(Density Estimation)**
   > : N개의 관찰데이터(observations) <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}_1,\ldots\mathbf{x}_N" title="\mathbf{x}_1,\ldots\mathbf{x}_N" />가 주어졌을 때 분포함수 <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x})" title="p(\mathbf{x})" />를 찾는 것

1. <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x})" title="p(\mathbf{x})" />를 파라미터화된 분포로 가정. 회귀, 분류문제에서는 주로 <img src="https://latex.codecogs.com/gif.latex?p(t|\mathbf{x}),&space;p(\mathcal{C}|\mathbf{x})" title="p(t|\mathbf{x}), p(\mathcal{C}|\mathbf{x})" />를 추정


2. 그 다음 분포의 파라미터 찾기   
   - **빈도주의 방법(Frequentist's way)**    
      > 어떤 기준(예를 들어 likelihood)을 최적화시키는 과정을 통해 파라미터 값을 정하고, 파라미터의 하나의 값을 구하게됨.
   - **베이지언 방법(Bayesian way)**   
      > 먼저 파라미터의 사전확률(prior distribution)을 가정하고 Bayes' rule을 통해 파라미터의 사후확률(posterior distribution)을 구함.

3. 파라미터를 찾았다면(한 개의 값이든 분포든) 그것을 사용해 "예측"할 수 있다(t나 <img src="https://latex.codecogs.com/gif.latex?\mathcal{C}" title="\mathcal{C}" />).


+ 켤레사전분포(Conjugate Prior): 사후확률이 사전확률과 동일한 함수형태를 가지도록 해줌. (계산의 편리성을 위해 사용)

- - - - - - - - - - - - -
## 이항변수(Binary Variables): 빈도주의 방법

+ 이항 확률변수(binary random variable) <img src="https://latex.codecogs.com/gif.latex?x\in&space;\{0,&space;1\}" title="x\in \{0, 1\}" /> (예를 들어 동전던지기)가 다음을 만족한다고 하자.   

   > <img src="https://latex.codecogs.com/gif.latex?p(x=1&space;|&space;\mu)&space;=&space;\mu,&space;p(x=0&space;|&space;\mu)&space;=&space;1&space;-&space;\mu" title="p(x=1 | \mu) = \mu, p(x=0 | \mu) = 1 - \mu" />   

+ <img src="https://latex.codecogs.com/gif.latex?p(x)" title="p(x)" />는 베르누이 분포(Bernoulli distribution)로 표현될 수 있음.   
   
   > <img src="https://latex.codecogs.com/gif.latex?\mathrm{Bern}(x&space;|&space;\mu)&space;=&space;\mu^x&space;(1-\mu)^{1-x}" title="\mathrm{Bern}(x | \mu) = \mu^x (1-\mu)^{1-x}" />

+ 기댓값, 분산
   - <img src="https://latex.codecogs.com/gif.latex?\mathbb{E}[x]&space;=&space;\mu" title="\mathbb{E}[x] = \mu" />   
   
   - <img src="https://latex.codecogs.com/gif.latex?\mathrm{var}[x]&space;=&space;\mu(1-\mu)" title="\mathrm{var}[x] = \mu(1-\mu)" />   
   

+ 우도함수 (Likelihood Function)

   + <img src="https://latex.codecogs.com/gif.latex?\mathcal{D}&space;=&space;\{x_1,\ldots,x_N\}" title="\mathcal{D} = \{x_1,\ldots,x_N\}" />: x값을 N번 관찰한 결과   
   
   + 각 x가 독립적으로 <img src="https://latex.codecogs.com/gif.latex?p(x|\mu)" title="p(x|\mu)" />에서 뽑혀진다고 가정하면 다음과 같이 우도함수(<img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />의 함수인)를 만들 수 있음.   
   
      > <img src="https://latex.codecogs.com/gif.latex?p(\mathcal{D}|\mu)&space;=&space;\prod_{n=1}^N&space;p(x_n|\mu)&space;=&space;\prod_{n=1}^N&space;\mu^{x_n}&space;(1-\mu)^{1-x_n}" title="p(\mathcal{D}|\mu) = \prod_{n=1}^N p(x_n|\mu) = \prod_{n=1}^N \mu^{x_n} (1-\mu)^{1-x_n}" />   
      

   + **빈도주의 방법**에서는 $\mu$값을 이 우도함수를 최대화시키는 값으로 구할 수 있음. 또는 아래와 같이 로그우도함수를 최대화시킬 수도 있음.   
   
      > <img src="https://latex.codecogs.com/gif.latex?\ln&space;p(\mathcal{D}|\mu)&space;=&space;\sum_{n=1}^N&space;\ln&space;p(x_n|\mu)&space;=&space;\sum_{n=1}^N&space;\{x_n\ln&space;\mu&space;&plus;&space;(1-x_n)\ln(1-\mu)\}" title="\ln p(\mathcal{D}|\mu) = \sum_{n=1}^N \ln p(x_n|\mu) = \sum_{n=1}^N \{x_n\ln \mu + (1-x_n)\ln(1-\mu)\}" />   
      

   + 미분을 해서 정리하면, <img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />의 최대우도 추정치(maximum likelihood estimate) : <img src="https://latex.codecogs.com/gif.latex?\mu^{\mathrm{ML}}&space;=&space;\frac{m}{N}&space;~~\mathrm{with}~~&space;m&space;=&space;(\&hash;\mathrm{observations~of}~&space;x=1)" title="\mu^{\mathrm{ML}} = \frac{m}{N} ~~\mathrm{with}~~ m = (\#\mathrm{observations~of}~ x=1)" />   
   
   + **N이 작은 경우에 위 MLE는 과적합(overfitting)된 결과** 를 낳을 수 있음.   
      > <img src="https://latex.codecogs.com/gif.latex?N&space;=&space;m&space;=&space;3&space;\to&space;\mu^{\mathrm{ML}}&space;=&space;1" title="N = m = 3 \to \mu^{\mathrm{ML}} = 1" />   
      
      > 동일한 값이 나오는 경우가 존재함. 예를 들어 동전을 세번 던졌을 경우, 앞면이 세번 나온다면, MLE=1 (즉, 다음에 동전을 던지면 앞면이 나올 경우가 1이다?). 이는 관찰 데이터에 대해 존재하는 불확실성을 제대로 표현하지 못함
    
      > 따라서 불확실성을 잘 표현하기 위해 베이지언 방법을 사용함.   
      
      
## 이항변수(Binary Variables): 베이지언 방법

+ **이항분포 (Binomial Distribution)**
   > <img src="https://latex.codecogs.com/gif.latex?\mathcal{D}&space;=&space;\{x_1,\ldots,x_N\}" title="\mathcal{D} = \{x_1,\ldots,x_N\}" />일 때, 이항변수 x가 1인 경우를 $m$번 관찰할 확률   
   
   > <img src="https://latex.codecogs.com/gif.latex?\mathrm{Bin}(m|N,\mu)&space;=&space;{N&space;\choose&space;m}\mu^m(1-\mu)^{N-m}" title="\mathrm{Bin}(m|N,\mu) = {N \choose m}\mu^m(1-\mu)^{N-m}" />

   > <img src="https://latex.codecogs.com/gif.latex?{N&space;\choose&space;m}&space;=&space;\frac{N!}{(N-m)!m!}" title="{N \choose m} = \frac{N!}{(N-m)!m!}" />   
   
   + 기댓값, 분산
      + <img src="https://latex.codecogs.com/gif.latex?\mathbb{E}[m]&space;=&space;\sum_{m=0}^N&space;m\mathrm{Bin}(m|N,\mu)&space;=&space;N\mu" title="\mathbb{E}[m] = \sum_{m=0}^N m\mathrm{Bin}(m|N,\mu) = N\mu" />   
   
      + <img src="https://latex.codecogs.com/gif.latex?\mathrm{var}[m]&space;=&space;\sum_{m=0}^N&space;(m-\mathbb{E}[m])^2\mathrm{Bin}(m|N,\mu)&space;=&space;N\mu(1-\mu)" title="\mathrm{var}[m] = \sum_{m=0}^N (m-\mathbb{E}[m])^2\mathrm{Bin}(m|N,\mu) = N\mu(1-\mu)" />   
   
   + 데이터를 보는 관점
      - 베르누이 시행의 반복: <img src="https://latex.codecogs.com/gif.latex?x_1,\ldots,x_N" title="x_1,\ldots,x_N" /> 각각이 확률변수
      - x가 1인 경우를 몇 번 관찰했는가?: 하나의 확률변수 m

   + 베이지안 방법을 쓰기 위해서 데이터의 우도를 구해야 하는데 이항분포를 가정하면 우도함수가 하나의 변수 m으로(<img src="https://latex.codecogs.com/gif.latex?x_1,\ldots,x_N" title="x_1,\ldots,x_N" /> 대신) 표현가능하므로 간편해짐 ❗   


+ **베타분포 (Beta Distribution)**

   > 베이지언 방법으로 문제를 해결하기 위해 베타분포를 **켤레사전분포(conjugate prior)로 사용**함.

   > <img src="https://latex.codecogs.com/gif.latex?\mathrm{Beta}(\mu|a,b)&space;=&space;\frac{\Gamma(a&plus;b)}{\Gamma(a)\Gamma(b)}\mu^{a-1}(1-\mu)^{b-1}" title="\mathrm{Beta}(\mu|a,b) = \frac{\Gamma(a+b)}{\Gamma(a)\Gamma(b)}\mu^{a-1}(1-\mu)^{b-1}" />   
   

   + 감마함수 <img src="https://latex.codecogs.com/gif.latex?\Gamma(x)" title="\Gamma(x)" />의 정의   
      
      > <img src="https://latex.codecogs.com/gif.latex?\Gamma(x)&space;=&space;\int_0^{\infty}u^{x-1}e^{-u}\mathrm{d}u" title="\Gamma(x) = \int_0^{\infty}u^{x-1}e^{-u}\mathrm{d}u" />   
      

      + 감마함수는 계승(factorial)을 실수로 확장시킴.   
      
         > <img src="https://latex.codecogs.com/gif.latex?\Gamma(n)&space;=&space;(n-1)!" title="\Gamma(n) = (n-1)!" />   
         

         + <img src="https://latex.codecogs.com/gif.latex?\Gamma(x)&space;=&space;(x-1)\Gamma(x-1)" title="\Gamma(x) = (x-1)\Gamma(x-1)" /> 증명   
         
            + <img src="https://latex.codecogs.com/gif.latex?\int_0^{\infty}a\mathrm{d}b&space;=&space;\left.&space;ab\right\vert_0^{\infty}&space;-&space;\int_0^{\infty}b\mathrm{d}a" title="\int_0^{\infty}a\mathrm{d}b = \left. ab\right\vert_0^{\infty} - \int_0^{\infty}b\mathrm{d}a" />에 대해 미분   
            
               > <img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;a&space;&=&space;u^{x-1}&space;&\mathrm{d}b&space;&=&space;-e^{-u}\mathrm{d}u\\&space;b&space;&=&space;e^{-u}&space;&\mathrm{d}a&space;&=&space;(x-1)u^{x-2}\mathrm{d}u\\&space;\Gamma(x)&space;&=&space;\left.&space;u^{x-1}(-e^{-u})\right\vert_0^{\infty}&space;&plus;&space;\int_0^{\infty}&space;(x-1)u^{x-2}e^{-u}\mathrm{d}u\\&space;&=&space;0&space;&plus;&space;(x-1)\Gamma(x-1)&space;\end{align*}" title="\begin{align*} a &= u^{x-1} &\mathrm{d}b &= -e^{-u}\mathrm{d}u\\ b &= e^{-u} &\mathrm{d}a &= (x-1)u^{x-2}\mathrm{d}u\\ \Gamma(x) &= \left. u^{x-1}(-e^{-u})\right\vert_0^{\infty} + \int_0^{\infty} (x-1)u^{x-2}e^{-u}\mathrm{d}u\\ &= 0 + (x-1)\Gamma(x-1) \end{align*}" />   
            
   + 베타분포가 normalized임을 증명 ❗ 
      > 즉, <img src="https://latex.codecogs.com/gif.latex?\int_0^{1}\mathrm{Beta}(\mu|a,b)\mathrm{d}\mu&space;=&space;1" title="\int_0^{1}\mathrm{Beta}(\mu|a,b)\mathrm{d}\mu = 1" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\int_0^1&space;\mu^{a-1}(1-\mu)^{b-1}\mathrm{d}\mu&space;=&space;\frac{\Gamma(a)\Gamma(b)}{\Gamma(a&plus;b)}" title="\int_0^1 \mu^{a-1}(1-\mu)^{b-1}\mathrm{d}\mu = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}" />임을 증명   
      
      > <img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;\Gamma(a)\Gamma(b)&space;&=&space;\int_0^{\infty}&space;x^{a-1}e^{-x}\mathrm{d}x\int_0^{\infty}&space;y^{b-1}e^{-y}\mathrm{d}y\\&space;&=&space;\int_0^{\infty}\int_0^{\infty}e^{-x-y}x^{a-1}y^{b-1}\mathrm{d}y\mathrm{d}x\\&space;&=&space;\int_0^{\infty}\int_0^{\infty}e^{-t}x^{a-1}(t-x)^{b-1}\mathrm{d}t\mathrm{d}x&space;&\mathrm{by}~&space;t=y&plus;x,&space;\mathrm{d}t&space;=&space;\mathrm{d}y\\&space;&=&space;\int_0^{\infty}\int_0^{\infty}e^{-t}x^{a-1}(t-x)^{b-1}\mathrm{d}x\mathrm{d}t\\&space;&=&space;\int_0^{\infty}e^{-t}\int_0^{\infty}x^{a-1}(t-x)^{b-1}\mathrm{d}x\mathrm{d}t\\&space;&=&space;\int_0^{\infty}e^{-t}\int_0^1(t\mu)^{a-1}(t-t\mu)^{b-1}t\mathrm{d}\mu\mathrm{d}t&space;&\mathrm{by}~&space;x=t\mu,&space;\mathrm{d}x&space;=&space;t\mathrm{d}\mu\\&space;&=&space;\int_0^{\infty}e^{-t}t^{a-1}t^{b-1}t\left(\int_0^1&space;\mu^{a-1}(1-\mu)^{b-1}\mathrm{d}\mu\right)\mathrm{d}t\\&space;&=&space;\int_0^{\infty}e^{-t}t^{a&plus;b-1}\mathrm{d}t\int_0^1\mu^{a-1}(1-\mu)^{b-1}\mathrm{d}\mu\\&space;&=&space;\Gamma(a&plus;b)\int_0^1\mu^{a-1}(1-\mu)^{b-1}\mathrm{d}\mu&space;\end{align*}" title="\begin{align*} \Gamma(a)\Gamma(b) &= \int_0^{\infty} x^{a-1}e^{-x}\mathrm{d}x\int_0^{\infty} y^{b-1}e^{-y}\mathrm{d}y\\ &= \int_0^{\infty}\int_0^{\infty}e^{-x-y}x^{a-1}y^{b-1}\mathrm{d}y\mathrm{d}x\\ &= \int_0^{\infty}\int_0^{\infty}e^{-t}x^{a-1}(t-x)^{b-1}\mathrm{d}t\mathrm{d}x &\mathrm{by}~ t=y+x, \mathrm{d}t = \mathrm{d}y\\ &= \int_0^{\infty}\int_0^{\infty}e^{-t}x^{a-1}(t-x)^{b-1}\mathrm{d}x\mathrm{d}t\\ &= \int_0^{\infty}e^{-t}\int_0^{\infty}x^{a-1}(t-x)^{b-1}\mathrm{d}x\mathrm{d}t\\ &= \int_0^{\infty}e^{-t}\int_0^1(t\mu)^{a-1}(t-t\mu)^{b-1}t\mathrm{d}\mu\mathrm{d}t &\mathrm{by}~ x=t\mu, \mathrm{d}x = t\mathrm{d}\mu\\ &= \int_0^{\infty}e^{-t}t^{a-1}t^{b-1}t\left(\int_0^1 \mu^{a-1}(1-\mu)^{b-1}\mathrm{d}\mu\right)\mathrm{d}t\\ &= \int_0^{\infty}e^{-t}t^{a+b-1}\mathrm{d}t\int_0^1\mu^{a-1}(1-\mu)^{b-1}\mathrm{d}\mu\\ &= \Gamma(a+b)\int_0^1\mu^{a-1}(1-\mu)^{b-1}\mathrm{d}\mu \end{align*}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;\int_0^1&space;\mu^{a-1}(1-\mu)^{b-1}\mathrm{d}\mu&space;=&space;\frac{\Gamma(a)\Gamma(b)}{\Gamma(a&plus;b)}" title="\therefore \int_0^1 \mu^{a-1}(1-\mu)^{b-1}\mathrm{d}\mu = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}" />   
      
      
+ 기댓값, 분산
   + <img src="https://latex.codecogs.com/gif.latex?\mathbb{E}[\mu]&space;=&space;\frac{a}{a&plus;b}" title="\mathbb{E}[\mu] = \frac{a}{a+b}" />   
   
   + <img src="https://latex.codecogs.com/gif.latex?\mathrm{var}[\mu]&space;=&space;\frac{ab}{(a&plus;b)^2(a&plus;b&plus;1)}" title="\mathrm{var}[\mu] = \frac{ab}{(a+b)^2(a+b+1)}" />   
   

+ <img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />의 사후확률 (posterior)   

   > <img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;p(\mu&space;|&space;m,&space;l,&space;a,&space;b)&space;&=&space;\frac{\textrm{Bin}(m|N,\mu)\textrm{Beta}(\mu|a,b)}{\int_0^1&space;\textrm{Bin}(m|N,\mu)\textrm{Beta}(\mu|a,b)\textrm{d}\mu}\\&space;&=&space;\frac{\mu^{m&plus;a-1}(1-\mu)^{l&plus;b-1}}{\int_0^1&space;\mu^{m&plus;b-1}(1-\mu)^{l&plus;b-1}\textrm{d}\mu}\\&space;&=&space;\frac{\mu^{m&plus;a-1}(1-\mu)^{l&plus;b-1}}{\Gamma(m&plus;a)\Gamma(l&plus;b)/\Gamma(m&plus;a&plus;l&plus;b)}\\&space;&=&space;\frac{\Gamma(m&plus;a&plus;l&plus;b)}{\Gamma(m&plus;a)\Gamma(l&plus;b)}\mu^{m&plus;a-1}(1-\mu)^{l&plus;b-1}&space;\end{align*}" title="\begin{align*} p(\mu | m, l, a, b) &= \frac{\textrm{Bin}(m|N,\mu)\textrm{Beta}(\mu|a,b)}{\int_0^1 \textrm{Bin}(m|N,\mu)\textrm{Beta}(\mu|a,b)\textrm{d}\mu}\\ &= \frac{\mu^{m+a-1}(1-\mu)^{l+b-1}}{\int_0^1 \mu^{m+b-1}(1-\mu)^{l+b-1}\textrm{d}\mu}\\ &= \frac{\mu^{m+a-1}(1-\mu)^{l+b-1}}{\Gamma(m+a)\Gamma(l+b)/\Gamma(m+a+l+b)}\\ &= \frac{\Gamma(m+a+l+b)}{\Gamma(m+a)\Gamma(l+b)}\mu^{m+a-1}(1-\mu)^{l+b-1} \end{align*}" />   
   

+ 예측분포 (predictive distribution)

   > <img src="https://latex.codecogs.com/gif.latex?p(x=1&space;|&space;\mathcal{D})&space;=&space;\int_0^1&space;p(x=1|\mu)p(\mu|\mathcal{D})\mathrm{d}\mu&space;=&space;\int_0^1&space;\mu&space;p(\mu|\mathcal{D})\mathrm{d}\mu&space;=&space;\mathbb{E}[\mu|\mathcal{D}]" title="p(x=1 | \mathcal{D}) = \int_0^1 p(x=1|\mu)p(\mu|\mathcal{D})\mathrm{d}\mu = \int_0^1 \mu p(\mu|\mathcal{D})\mathrm{d}\mu = \mathbb{E}[\mu|\mathcal{D}]" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?p(x=1&space;|&space;\mathcal{D})&space;=&space;\frac{m&plus;a}{m&plus;a&plus;l&plus;b}" title="p(x=1 | \mathcal{D}) = \frac{m+a}{m+a+l+b}" />   
   
  
   + 빈도주의 방법보다 베이지안 방법을 통해 어느정도 불확실성을 남기게 됨 (빈도주의의 극단적인 값을 피할수 있음) ✨    

   + 빈도주의는 m,l을 통해 계산을 했지만, 베이지안 방법은 사전확률 ✨ 

   + 예) N=m=3인 경우, (즉, x=1인 경우가 3번 나온 경우) 
      > 구체적인 예로는 a=2, b=1, m=3(새로운 관찰값), l=0일 때 **빈도주의**는 <img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />가 1이라는 결과가 나왔지만, **베이지안 방법**을 사용한다면, <img src="https://latex.codecogs.com/gif.latex?P(x=1|D)=5/6" title="P(x=1|D)=5/6" /> 으로 극단적인 예측을 하기보다는 **어느정도 불확실성을 남겨두는 예측**을 하게 됨
      
      
- - - - - - - - - - - - - -      
## 다항변수(Multinomial Variables): 빈도주의 방법

+ K개의 상태를 가질 수 있는 확률변수를 K차원의 벡터 <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}" title="\mathbf{x}" /> (하나의 원소만 1이고 나머지는 0)로 나타냄. 이에 관해 베르누이 분포를 일반화하면 다음과 같음.   
   
   > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x}|\pmb&space;\mu)&space;=&space;\prod_{k=1}^K&space;\mu_k^{x_k}" title="p(\mathbf{x}|\pmb \mu) = \prod_{k=1}^K \mu_k^{x_k}" />   
   
   > 이때, <img src="https://latex.codecogs.com/gif.latex?\sum_k&space;\mu_k&space;=&space;1" title="\sum_k \mu_k = 1" />.

+ <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}" title="\mathbf{x}" />의 기댓값   

   > <img src="https://latex.codecogs.com/gif.latex?\mathbb{E}[\mathbf{x}|\pmb&space;\mu]&space;=&space;\sum_{\mathbf{x}}&space;p(\mathbf{x}|\pmb&space;\mu)&space;=&space;(\mu_1,\ldots,\mu_M)^T&space;=&space;\pmb&space;\mu" title="\mathbb{E}[\mathbf{x}|\pmb \mu] = \sum_{\mathbf{x}} p(\mathbf{x}|\pmb \mu) = (\mu_1,\ldots,\mu_M)^T = \pmb \mu" />   
   

+ 우도함수
   + <img src="https://latex.codecogs.com/gif.latex?{\bf&space;x}" title="{\bf x}" />값을 N번 관찰한 결과 <img src="https://latex.codecogs.com/gif.latex?\mathcal{D}&space;=&space;\{{\bf&space;x}_1,\ldots,{\bf&space;x}_N\}" title="\mathcal{D} = \{{\bf x}_1,\ldots,{\bf x}_N\}" />가 주어졌을 때, 우도함수는 다음과 같음.    
   
      > <img src="https://latex.codecogs.com/gif.latex?p(\mathcal{D}|\pmb&space;\mu)&space;=&space;\prod_{n=1}^N\prod_{k=1}^K&space;\mu_k^{x_{nk}}&space;=&space;\prod_{k=1}^K&space;\mu_k^{(\sum_n&space;x_{nk})}&space;=&space;\prod_{k=1}^K&space;\mu_k^{m_k}" title="p(\mathcal{D}|\pmb \mu) = \prod_{n=1}^N\prod_{k=1}^K \mu_k^{x_{nk}} = \prod_{k=1}^K \mu_k^{(\sum_n x_{nk})} = \prod_{k=1}^K \mu_k^{m_k}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?m_k&space;=&space;\sum_n&space;x_{nk}" title="m_k = \sum_n x_{nk}" />   
      
   
   + <img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />의 최대우도 추정치(maximum likelihood estimate)를 구하기 위해선 <img src="https://latex.codecogs.com/gif.latex?\mu_k" title="\mu_k" />**의 합이 1이 된다는 조건**하에서 <img src="https://latex.codecogs.com/gif.latex?\ln&space;p(\mathcal{D}|\pmb&space;\mu)" title="\ln p(\mathcal{D}|\pmb \mu)" />을 최대화시키는 <img src="https://latex.codecogs.com/gif.latex?\mu_k" title="\mu_k" />를 구해야 함 ❗❗    
   
      + 라그랑주 승수(Lagrange multiplier) <img src="https://latex.codecogs.com/gif.latex?\lambda" title="\lambda" />를 사용해서 다음을 최대화시키면 됨.   
      
         > <img src="https://latex.codecogs.com/gif.latex?\sum_{k=1}^K&space;m_k&space;\ln&space;\mu_k&space;&plus;&space;\lambda&space;\left(\sum_{k=1}^K&space;\mu_k&space;-1\right)" title="\sum_{k=1}^K m_k \ln \mu_k + \lambda \left(\sum_{k=1}^K \mu_k -1\right)" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?\mu_k^{ML}&space;=&space;\frac{m_k}{N}" title="\mu_k^{ML} = \frac{m_k}{N}" />   
         
         - - - - - - - - - - - - - -
         > <img src="https://latex.codecogs.com/gif.latex?\bigtriangledown&space;_{\mu_{k}}&space;lnP(D|\mu)=\frac{m_{k}}{\mu_{k}}&plus;\lambda=0" title="\bigtriangledown _{\mu_{k}} lnP(D|\mu)=\frac{m_{k}}{\mu_{k}}+\lambda=0" />이므로, <img src="https://latex.codecogs.com/gif.latex?\mu_{k}=-\frac{m_{k}}{\lambda}" title="\mu_{k}=-\frac{m_{k}}{\lambda}" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?\because&space;\sum&space;_{k=1}^{K}&space;\mu_{k}=1\Rightarrow&space;\sum_{k=1}^{K}\frac{-m_{k}}{\lambda}=\frac{-1}{\lambda}\sum_{k=1}^{K}m_{k}=\frac{-N}{\lambda}=1\Rightarrow&space;\lambda=-N" title="\because \sum _{k=1}^{K} \mu_{k}=1\Rightarrow \sum_{k=1}^{K}\frac{-m_{k}}{\lambda}=\frac{-1}{\lambda}\sum_{k=1}^{K}m_{k}=\frac{-N}{\lambda}=1\Rightarrow \lambda=-N" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?\mu_{k}=\frac{m_{k}}{N}" title="\mu_{k}=\frac{m_{k}}{N}" />   
         
         
         
## 다항변수(Multinomial Variables): 베이지언 방법

+ 다항분포 (Multinomial distribution)
   > 이항분포 일반화시킨 형태   

   > 파라미터 <img src="https://latex.codecogs.com/gif.latex?\pmb&space;\mu" title="\pmb \mu" />와 전체 관찰개수 N이 주어졌을 때 <img src="https://latex.codecogs.com/gif.latex?m_1,\ldots,m_K" title="m_1,\ldots,m_K" />의 분포를 다항분포(multinomial distribution)이라고 함.

   > <img src="https://latex.codecogs.com/gif.latex?\mathrm{Mult}(m_1,\ldots,m_K|\pmb&space;\mu,N)&space;=&space;{N&space;\choose&space;m_1m_2\ldots&space;m_K}&space;\prod_{k=1}^K&space;\mu_k^{m_k}" title="\mathrm{Mult}(m_1,\ldots,m_K|\pmb \mu,N) = {N \choose m_1m_2\ldots m_K} \prod_{k=1}^K \mu_k^{m_k}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?{N&space;\choose&space;m_1m_2\ldots&space;m_K}&space;=&space;\frac{N!}{m_1!m_2!\ldots&space;m_K!}" title="{N \choose m_1m_2\ldots m_K} = \frac{N!}{m_1!m_2!\ldots m_K!}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\sum_{k=1}^K&space;m_k=&space;N" title="\sum_{k=1}^K m_k= N" />   
   

+ **디리클레 분포(Dirichlet distribution)**: 다항분포를 위한 켤레사전분포

   > <img src="https://latex.codecogs.com/gif.latex?\mathrm{Dir}(\pmb&space;\mu|\mathbf{\alpha})&space;=&space;\frac{\Gamma{\alpha_0}}{\Gamma(\alpha_1)\ldots\Gamma(\alpha_K)}\prod_{k=1}^K&space;\mu_k^{\alpha_k-1}" title="\mathrm{Dir}(\pmb \mu|\mathbf{\alpha}) = \frac{\Gamma{\alpha_0}}{\Gamma(\alpha_1)\ldots\Gamma(\alpha_K)}\prod_{k=1}^K \mu_k^{\alpha_k-1}" />   
     
   > <img src="https://latex.codecogs.com/gif.latex?\alpha_0&space;=&space;\sum_{k=1}^K&space;\alpha_k" title="\alpha_0 = \sum_{k=1}^K \alpha_k" />   
   

   + 디리클레 분포의 **normalization 증명** (K=3)

      + 다음 결과를 사용한다.
      
         > <img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;\int_L^U(x-L)^{a-1}(U-x)^{b-1}\mathrm{d}x&space;&=&space;\int_0^1&space;(U-L)^{a-1}t^{a-1}(U-L)^{b-1}(1-t)^{b-1}(U-L)\mathrm{d}t&space;&\mathrm{by}~&space;t=\frac{x-L}{U-L}\\&space;&=&space;(U-L)^{a&plus;b-1}\int_0^1&space;t^{a-1}(1-t)^{b-1}\mathrm{d}t\\&space;&=&space;(U-L)^{a&plus;b-1}\frac{\Gamma(a)\Gamma(b)}{\Gamma(a&plus;b)}&space;\end{align*}" title="\begin{align*} \int_L^U(x-L)^{a-1}(U-x)^{b-1}\mathrm{d}x &= \int_0^1 (U-L)^{a-1}t^{a-1}(U-L)^{b-1}(1-t)^{b-1}(U-L)\mathrm{d}t &\mathrm{by}~ t=\frac{x-L}{U-L}\\ &= (U-L)^{a+b-1}\int_0^1 t^{a-1}(1-t)^{b-1}\mathrm{d}t\\ &= (U-L)^{a+b-1}\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)} \end{align*}" />   
         

      + K=3인 경우,   
      
         > <img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;\int_0^{1-\mu_1}\mu_1^{\alpha_1-1}\mu_2^{\alpha_2-1}(1-\mu_1-\mu_2)^{\alpha_3-1}\mathrm{d}\mu_2&space;&=&space;\mu_1^{\alpha_1-1}\int_0^{1-\mu_1}\mu_2^{\alpha_2-1}(1-\mu_1-\mu_2)^{\alpha_3-1}\mathrm{d}\mu_2&space;&&space;\textrm{by}~&space;L=0,&space;U=1-\mu_1\\&space;&=&space;\mu_1^{\alpha_1-1}(1-\mu_1)^{\alpha_2&plus;\alpha_3-1}\frac{\Gamma(\alpha_2)\Gamma(\alpha_3)}{\Gamma(\alpha_2&plus;\alpha_3)}&space;\end{align*}" title="\begin{align*} \int_0^{1-\mu_1}\mu_1^{\alpha_1-1}\mu_2^{\alpha_2-1}(1-\mu_1-\mu_2)^{\alpha_3-1}\mathrm{d}\mu_2 &= \mu_1^{\alpha_1-1}\int_0^{1-\mu_1}\mu_2^{\alpha_2-1}(1-\mu_1-\mu_2)^{\alpha_3-1}\mathrm{d}\mu_2 & \textrm{by}~ L=0, U=1-\mu_1\\ &= \mu_1^{\alpha_1-1}(1-\mu_1)^{\alpha_2+\alpha_3-1}\frac{\Gamma(\alpha_2)\Gamma(\alpha_3)}{\Gamma(\alpha_2+\alpha_3)} \end{align*}" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;\int_0^1\int_0^{1-\mu_1}\mu_1^{\alpha_1-1}\mu_2^{\alpha_2-1}(1-\mu_1-\mu_2)^{\alpha_3-1}\mathrm{d}\mu_2\mathrm{d}\mu_1&space;&=&space;\frac{\Gamma(\alpha_2)\Gamma(\alpha_3)}{\Gamma(\alpha_2&plus;\alpha_3)}&space;\int_0^1&space;\mu_1^{\alpha_1-1}(1-\mu_1)^{\alpha_2&plus;\alpha_3-1}\mathrm{d}\mu_1\\&space;&=&space;\frac{\Gamma(\alpha_2)\Gamma(\alpha_3)}{\Gamma(\alpha_2&plus;\alpha_3)}&space;\frac{\Gamma(\alpha_1)\Gamma(\alpha_2&plus;\alpha_3)}{\Gamma(\alpha_1&plus;\alpha_2&plus;\alpha_3)}\\&space;&=&space;\frac{\Gamma(\alpha_1)\Gamma(\alpha_2)\Gamma(\alpha_3)}{\Gamma(\alpha_1&plus;\alpha_2&plus;\alpha_3)}&space;\end{align*}" title="\begin{align*} \int_0^1\int_0^{1-\mu_1}\mu_1^{\alpha_1-1}\mu_2^{\alpha_2-1}(1-\mu_1-\mu_2)^{\alpha_3-1}\mathrm{d}\mu_2\mathrm{d}\mu_1 &= \frac{\Gamma(\alpha_2)\Gamma(\alpha_3)}{\Gamma(\alpha_2+\alpha_3)} \int_0^1 \mu_1^{\alpha_1-1}(1-\mu_1)^{\alpha_2+\alpha_3-1}\mathrm{d}\mu_1\\ &= \frac{\Gamma(\alpha_2)\Gamma(\alpha_3)}{\Gamma(\alpha_2+\alpha_3)} \frac{\Gamma(\alpha_1)\Gamma(\alpha_2+\alpha_3)}{\Gamma(\alpha_1+\alpha_2+\alpha_3)}\\ &= \frac{\Gamma(\alpha_1)\Gamma(\alpha_2)\Gamma(\alpha_3)}{\Gamma(\alpha_1+\alpha_2+\alpha_3)} \end{align*}" />   
         
   + 일반적인 경우(K=M) : 귀납법(induction)으로 증명

      > <img src="https://latex.codecogs.com/gif.latex?\int&space;_{0}^{1}&space;\int_{0}^{1-\mu_{1}}...&space;\int_{0}^{1-\left&space;(&space;\mu_{1}&plus;...&plus;\mu_{M-2}&space;\right&space;)}&space;\mu_{1}^{\alpha_{1}-1}\times&space;...\times&space;\mu_{M-1}^{\alpha_{M-1}-1}\left&space;\{&space;1-\left&space;(&space;\mu_{1}&plus;...&plus;\mu_{M-1}&space;\right&space;)&space;\right&space;\}^{\alpha_{M}-1}d\mu_{M-1}...d\mu_{2}d\mu_{1}" title="\int _{0}^{1} \int_{0}^{1-\mu_{1}}... \int_{0}^{1-\left ( \mu_{1}+...+\mu_{M-2} \right )} \mu_{1}^{\alpha_{1}-1}\times ...\times \mu_{M-1}^{\alpha_{M-1}-1}\left \{ 1-\left ( \mu_{1}+...+\mu_{M-1} \right ) \right \}^{\alpha_{M}-1}d\mu_{M-1}...d\mu_{2}d\mu_{1}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?=\frac{\Gamma&space;(\alpha_{1})&space;\times&space;...&space;\times&space;\Gamma&space;(\alpha_{M})}{\Gamma&space;(\alpha_{1}&plus;...&plus;\alpha_{M})}" title="=\frac{\Gamma (\alpha_{1}) \times ... \times \Gamma (\alpha_{M})}{\Gamma (\alpha_{1}+...+\alpha_{M})}" />   


      + Base : M=2 -> Beta 분포를 따름    

      + 가정 : M-1개의 변수에 대해 normalized !   
      
         > <img src="https://latex.codecogs.com/gif.latex?\int_{0}^{1-\left&space;(&space;\mu_{1}&plus;...&plus;\mu_{M-2}&space;\right&space;)}&space;\mu_{1}^{\alpha_{1}-1}\times&space;...\times&space;\mu_{M-2}^{\alpha_{M-2}-1}\mu_{M-1}^{\alpha_{M-1}-1}\left&space;\{&space;1-\left&space;(&space;\mu_{1}&plus;...&plus;\mu_{M-2}&plus;\mu_{M-1}&space;\right&space;)&space;\right&space;\}^{\alpha_{M}-1}d\mu_{M-1}" title="\int_{0}^{1-\left ( \mu_{1}+...+\mu_{M-2} \right )} \mu_{1}^{\alpha_{1}-1}\times ...\times \mu_{M-2}^{\alpha_{M-2}-1}\mu_{M-1}^{\alpha_{M-1}-1}\left \{ 1-\left ( \mu_{1}+...+\mu_{M-2}+\mu_{M-1} \right ) \right \}^{\alpha_{M}-1}d\mu_{M-1}" />   
         

         > 위의 디리클레 분포 증명에서 사용된 사실을 이용. <img src="https://latex.codecogs.com/gif.latex?U=1-\left&space;(&space;\mu_{1}&plus;...&plus;\mu_{M-2}&space;\right&space;),&space;L=0" title="U=1-\left ( \mu_{1}+...+\mu_{M-2} \right ), L=0" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?\int&space;_{0}^{1}...&space;\int_{0}^{1-\left&space;(&space;\mu_{1}&plus;...&plus;\mu_{M-3}&space;\right&space;)}&space;\mu_{1}^{\alpha_{1}-1}\times&space;...\times&space;\mu_{M-2}^{\alpha_{M-2}-1}\left&space;\{&space;1-\left&space;(&space;\mu_{1}&plus;...&plus;\mu_{M-2}&space;\right&space;)&space;\right&space;\}^{\alpha_{M-1}&plus;\alpha_{M}-1}d\mu_{M-2}...d\mu_{1}" title="\int _{0}^{1}... \int_{0}^{1-\left ( \mu_{1}+...+\mu_{M-3} \right )} \mu_{1}^{\alpha_{1}-1}\times ...\times \mu_{M-2}^{\alpha_{M-2}-1}\left \{ 1-\left ( \mu_{1}+...+\mu_{M-2} \right ) \right \}^{\alpha_{M-1}+\alpha_{M}-1}d\mu_{M-2}...d\mu_{1}" /> <img src="https://latex.codecogs.com/gif.latex?\times&space;\frac{\Gamma&space;(\alpha_{M-1})\Gamma&space;(\alpha_{M})}{\Gamma&space;(\alpha_{M-1}&plus;\alpha_{M})}" title="\times \frac{\Gamma (\alpha_{M-1})\Gamma (\alpha_{M})}{\Gamma (\alpha_{M-1}+\alpha_{M})}" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?=\frac{\Gamma&space;(\alpha_{1})&space;\times&space;...&space;\times&space;\Gamma&space;(\alpha_{M-2})\Gamma&space;(\alpha_{M-1}&plus;\alpha_{M})}{\Gamma&space;(\alpha_{1}&plus;...&plus;\alpha_{M-2}&plus;\alpha_{M-1}&plus;\alpha_{M})}\times&space;\frac{\Gamma&space;(\alpha_{M-1})\Gamma&space;(\alpha_{M})}{\Gamma&space;(\alpha_{M-1}&plus;\alpha_{M})}" title="=\frac{\Gamma (\alpha_{1}) \times ... \times \Gamma (\alpha_{M-2})\Gamma (\alpha_{M-1}+\alpha_{M})}{\Gamma (\alpha_{1}+...+\alpha_{M-2}+\alpha_{M-1}+\alpha_{M})}\times \frac{\Gamma (\alpha_{M-1})\Gamma (\alpha_{M})}{\Gamma (\alpha_{M-1}+\alpha_{M})}" />   
            
         > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;\frac{\Gamma&space;(\alpha_{1})&space;\times&space;...&space;\times&space;\Gamma&space;(\alpha_{M})}{\Gamma&space;(\alpha_{1}&plus;...&plus;\alpha_{M})}" title="\therefore \frac{\Gamma (\alpha_{1}) \times ... \times \Gamma (\alpha_{M})}{\Gamma (\alpha_{1}+...+\alpha_{M})}" />   
         
         
      + 모든 M에 대해서 normalized !   

      
+ <img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />의 사후확률 (posterior)

   > <img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;p(\pmb&space;\mu|\mathcal{D},\mathbf{\alpha})&space;&=&space;\mathrm{Dir}(\pmb&space;\mu|\mathbf{\alpha}&plus;\mathbf{m})\\&space;&=&space;\frac{\Gamma(\alpha_0&plus;N)}{\Gamma(\alpha_1&plus;m_1)\ldots\Gamma(\alpha_K&plus;m_K)}\prod_{k=1}^K&space;\mu_k^{\alpha_k&plus;m_k-1}&space;\end{align*}" title="\begin{align*} p(\pmb \mu|\mathcal{D},\mathbf{\alpha}) &= \mathrm{Dir}(\pmb \mu|\mathbf{\alpha}+\mathbf{m})\\ &= \frac{\Gamma(\alpha_0+N)}{\Gamma(\alpha_1+m_1)\ldots\Gamma(\alpha_K+m_K)}\prod_{k=1}^K \mu_k^{\alpha_k+m_k-1} \end{align*}" />

   > <img src="https://latex.codecogs.com/gif.latex?\mathbf{m}&space;=&space;(m_1,\ldots,m_K)^T" title="\mathbf{m} = (m_1,\ldots,m_K)^T" />   
   

   + <img src="https://latex.codecogs.com/gif.latex?x_k=1" title="x_k=1" />에 대한 사전관찰 개수 : <img src="https://latex.codecogs.com/gif.latex?\alpha_k" title="\alpha_k" />     


   
   
