# 선형회귀(Linear Models for Regression)

## 선형 기저 함수 모델

+ 가장 단순한 모델

   > <img src="https://latex.codecogs.com/gif.latex?y(\mathbf{x,w})=w_{0}&plus;w_{1}x_{1}&plus;...w_{D}x_{D}" title="y(\mathbf{x,w})=w_{0}+w_{1}x_{1}+...w_{D}x_{D}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}=\left&space;(&space;x_{1},&space;...,&space;x_{D}&space;\right&space;)^{T}" title="\mathbf{x}=\left ( x_{1}, ..., x_{D} \right )^{T}" />   
   
   + x에 관한 비선형 함수는 다음과 같다.
   
      > <img src="https://latex.codecogs.com/gif.latex?y(\mathbf{x},&space;\mathbf{w})=w_{0}&plus;\sum_{j=1}^{M-1}&space;w_{j}\phi&space;_{j}(\mathbf{x})=\sum_{j=0}^{M-1}&space;w_{j}\phi&space;_{j}(\mathbf{x})=\mathbf{w}^{T}\phi&space;(\mathbf{x})" title="y(\mathbf{x}, \mathbf{w})=w_{0}+\sum_{j=1}^{M-1} w_{j}\phi _{j}(\mathbf{x})=\sum_{j=0}^{M-1} w_{j}\phi _{j}(\mathbf{x})=\mathbf{w}^{T}\phi (\mathbf{x})" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\phi_{0}(\mathbf{x})=1" title="\phi_{0}(\mathbf{x})=1" />   
      
      > 기저함수(basis function) : <img src="https://latex.codecogs.com/gif.latex?\phi_{j}(\mathbf{x})" title="\phi_{j}(\mathbf{x})" />   
      
+ 몇가지 기저 함수

   + 다항식(polynomial) 기저함수
      
      > <img src="https://latex.codecogs.com/gif.latex?\phi_{j}({x})={x}^{j}" title="\phi_{j}({x})={x}^{j}" />   
      
      > <img src="https://user-images.githubusercontent.com/72974863/104307316-6a87f780-5512-11eb-9d2d-1a3c82db97ee.png" width="30%" height="30%">   
      
   
   + 가우시안 기저함수
      
      > <img src="https://latex.codecogs.com/gif.latex?\phi_{j}({x})=\textup{exp}&space;\left&space;\{&space;-\frac{\left&space;(x-\mu&space;\right&space;)^{2}}{2s^{2}}&space;\right&space;\}" title="\phi_{j}({x})=\textup{exp} \left \{ -\frac{\left (x-\mu \right )^{2}}{2s^{2}} \right \}" />   
      
      > <img src="https://user-images.githubusercontent.com/72974863/104307472-9b682c80-5512-11eb-852c-7ca024de7ba7.png" width="30%" height="30%">   
            
      
   + 시그모이드(sigmoid) 기저함수
      
      > <img src="https://latex.codecogs.com/gif.latex?\phi_{j}({x})=\sigma&space;\left&space;(&space;\frac{x-\mu_{j}}{s}&space;\right&space;)" title="\phi_{j}({x})=\sigma \left ( \frac{x-\mu_{j}}{s} \right )" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\sigma(a)=\frac{1}{1&plus;\textup{exp}(-a)}" title="\sigma(a)=\frac{1}{1+\textup{exp}(-a)}" />   
      
      > <img src="https://user-images.githubusercontent.com/72974863/104307493-a0c57700-5512-11eb-84e4-c19a42a8701e.png" width="30%" height="30%">   
               
   
## 최대우도와 최소제곱법(Maximum Likelihood and Least Squares)

+ 가우시안 노이즈가 포함된 타겟 t

   > <img src="https://latex.codecogs.com/gif.latex?t=y({\bf&space;x},{\bf&space;w})&plus;e" title="t=y({\bf x},{\bf w})+\epsilon " />   
   
   > <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;x},{\bf&space;w})" title="y({\bf x},{\bf w})" /> : 결정론적 함수(deterministic)
   
   > <img src="https://latex.codecogs.com/gif.latex?\epsilon&space;\sim&space;N(\epsilon&space;|0,&space;\beta^{-1})" title="\epsilon \sim N(\epsilon |0, \beta^{-1})" /> : 노이즈 확률변수   
   
+ t의 분포

   > <img src="https://latex.codecogs.com/gif.latex?p(t|{\bf&space;x},&space;{\bf&space;w},&space;\beta)=N(t|y({\bf&space;x},&space;{\bf&space;w}),&space;\beta^{-1})&space;\" title="p(t|{\bf x}, {\bf w}, \beta)=N(t|y({\bf x}, {\bf w}), \beta^{-1}) \" />   
   
   + 제곱합이 손실함수로 쓰이는 경우, 새로운 x가 주어졌을때 t의 최적 예측 값은 t의 조건부 기댓값 (이전 강의)
      
      > t가 위의 분포를 따르는 경우 조건부 기댓값 
      
      > <img src="https://latex.codecogs.com/gif.latex?E[t|{\bf&space;x}]&space;=&space;\int&space;tp(t|{\bf&space;x})dt&space;=&space;y({\bf&space;x},&space;{\bf&space;w})" title="E[t|{\bf x}] = \int tp(t|{\bf x})dt = y({\bf x}, {\bf w})" />   
      
      
+ 최대우도추정법을 통한 최적의 w 구하기

   + 입력 값 : <img src="https://latex.codecogs.com/gif.latex?\mathbf{X}=\bf&space;x_{1},&space;...&space;\bf&space;x_N" title="\mathbf{X}=\bf x_{1}, ... \bf x_N" />   
      
   + 출력 값 : <img src="https://latex.codecogs.com/gif.latex?\mathbf{t}=t_{1},&space;...,&space;t_{N}" title="\mathbf{t}=t_{1}, ..., t_{N}" />   
   
   + 우도함수
      > <img src="https://latex.codecogs.com/gif.latex?p({\bf&space;t}|{\bf&space;X},&space;{\bf&space;w},&space;\beta)=\prod_{n=1}^{N}N(t_n|{\bf&space;w}^T\phi(x_n),&space;\beta^{-1})" title="p({\bf t}|{\bf X}, {\bf w}, \beta)=\prod_{n=1}^{N}N(t_n|{\bf w}^T\phi(x_n), \beta^{-1})" />   
      
   + 로그 우도함수   
      > <img src="https://latex.codecogs.com/gif.latex?\ln{p({\bf&space;t}|{\bf&space;w},&space;\beta)}&space;=&space;\sum_{n=1}^{N}\ln{N(t_n|{\bf&space;w}^T\phi(x_n),&space;\beta^{-1})}\&space;=\dfrac{1}{2}\ln{\beta}-\dfrac{1}{2}\ln{2\pi}-\beta{E_D({\bf&space;w})}" title="\ln{p({\bf t}|{\bf w}, \beta)} = \sum_{n=1}^{N}\ln{N(t_n|{\bf w}^T\phi(x_n), \beta^{-1})}\ =\dfrac{1}{2}\ln{\beta}-\dfrac{1}{2}\ln{2\pi}-\beta{E_D({\bf w})}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?E_D({\bf&space;w})=\dfrac{1}{2}\sum_{n=1}^{N}{t_n-{\bf&space;w}^T\phi(x_n)}^2&space;\" title="E_D({\bf w})=\dfrac{1}{2}\sum_{n=1}^{N}{t_n-{\bf w}^T\phi(x_n)}^2 \" />   
            
      > 로그우도함수 최대화시키는 w값 = <img src="https://latex.codecogs.com/gif.latex?E_D({\bf&space;w})" title="E_D({\bf w})" />로 주어진 제곱합 에러함수 최소화시키는 값 ❗   
      
   + w에 대한 기울기 벡터
      > <img src="https://latex.codecogs.com/gif.latex?\nabla\ln{p({\bf&space;t}|{\bf&space;w},&space;\beta)}&space;=\beta\sum_{n=1}^{N}{t_n-{\bf&space;w}^T\phi(x_n)}\phi(x_n)^T&space;\" title="\nabla\ln{p({\bf t}|{\bf w}, \beta)} =\beta\sum_{n=1}^{N}{t_n-{\bf w}^T\phi(x_n)}\phi(x_n)^T \" />   
      
      > w의 최적값 : <img src="https://latex.codecogs.com/gif.latex?{\bf&space;w}_{ML}&space;=&space;(\Phi^T\Phi)^{-1}\Phi^T{\bf&space;t}&space;\" title="{\bf w}_{ML} = (\Phi^T\Phi)^{-1}\Phi^T{\bf t} \" /> (**normal equations**)    
      
      > <img src="https://latex.codecogs.com/gif.latex?\Phi" title="\Phi" />의 Moore-Penrose pseudo-inverse : <img src="https://latex.codecogs.com/gif.latex?\Phi^{\dagger}\equiv(\Phi^T\Phi)^{-1}\Phi^T&space;\" title="\Phi^{\dagger}\equiv(\Phi^T\Phi)^{-1}\Phi^T \" />   
      
      > 디자인 행렬(design matrix)
      
      > <img src="https://latex.codecogs.com/gif.latex?\Phi=\begin{pmatrix}&space;\phi_0(\bf&space;x_1)&space;&&space;\phi_1(\bf&space;x_1)&space;&&space;\cdots&space;&&space;\phi_{M-1}(\bf&space;x_1)&space;\\&space;\phi_0(\bf&space;x_2)&space;&&space;\phi_1(\bf&space;x_2)&space;&&space;\cdots&space;&&space;\phi_{M-1}(\bf&space;x_2)&space;\\&space;\vdots&space;&&space;\vdots&space;&&space;\ddots&space;&&space;\vdots&space;\\&space;\phi_0(\bf&space;x_N)&space;&&space;\phi_1(\bf&space;x_N)&space;&&space;\cdots&space;&&space;\phi_{M-1}(\bf&space;x_N)\&space;\end{pmatrix}" title="\Phi=\begin{pmatrix} \phi_0(\bf x_1) & \phi_1(\bf x_1) & \cdots & \phi_{M-1}(\bf x_1) \\ \phi_0(\bf x_2) & \phi_1(\bf x_2) & \cdots & \phi_{M-1}(\bf x_2) \\ \vdots & \vdots & \ddots & \vdots \\ \phi_0(\bf x_N) & \phi_1(\bf x_N) & \cdots & \phi_{M-1}(\bf x_N)\ \end{pmatrix}" />   
      
   + normal equations 유도하기 
   
      > <img src="https://latex.codecogs.com/gif.latex?\Phi&space;\bf&space;w\approx&space;t" title="\Phi \bf w\approx t" />   
      
      >  <img src="https://latex.codecogs.com/gif.latex?\frac{1}{2}\left&space;\|&space;\Phi&space;\bf&space;w-&space;t&space;\right&space;\|^{2}_{2}=\frac{1}{2}\left&space;(&space;\Phi&space;\bf&space;w-&space;t&space;\right&space;)^{T}\left&space;(&space;\Phi&space;\bf&space;w-&space;t&space;\right&space;)" title="\frac{1}{2}\left \| \Phi \bf w- t \right \|^{2}_{2}=\frac{1}{2}\left ( \Phi \bf w- t \right )^{T}\left ( \Phi \bf w- t \right )" />   
      
      > 전개하면,
      
      > <img src="https://latex.codecogs.com/gif.latex?\frac{1}{2}\mathbf{w^{T}}\Phi^{T}&space;\Phi&space;\mathbf{w}-\mathbf{t}^{T}\Phi&space;\mathbf{w}" title="\frac{1}{2}\mathbf{w^{T}}\Phi^{T} \Phi \mathbf{w}-\mathbf{t}^{T}\Phi \mathbf{w}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\bigtriangledown&space;_{\mathbf{w}}E(\mathbf{w})=\Phi^{T}&space;\Phi&space;\mathbf{w}-\Phi&space;\mathbf{t}=0" title="\bigtriangledown _{\mathbf{w}}E(\mathbf{w})=\Phi^{T} \Phi \mathbf{w}-\Phi \mathbf{t}=0" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;{\bf&space;w}_{ML}&space;=&space;(\Phi^T\Phi)^{-1}\Phi^T{\bf&space;t}&space;\" title="\therefore {\bf w}_{ML} = (\Phi^T\Phi)^{-1}\Phi^T{\bf t} \" />   
      
      + design matrix의 모든 열이 선형 독립이면, <img src="https://latex.codecogs.com/gif.latex?(\Phi^T\Phi)^{-1}" title="(\Phi^T\Phi)^{-1}" /> 존재 ❗ (항상성립하진 않지만 많은 경우에 성립하며, 성립하지 않은 경우에 대해 성립하도록 데이터 조절 가능)
      
   + 구한 에러함수를 편향 파라미터(bias parameter) <img src="https://latex.codecogs.com/gif.latex?w_{0}" title="w_{0}" />로 표현하면
   
      > <img src="https://latex.codecogs.com/gif.latex?E_D({\bf&space;w})=\dfrac{1}{2}\sum_{n=1}^{N}\left&space;\{&space;t_n-w_0-\sum_{j=1}^{M-1}{w_j\phi_j({\bf&space;x_n})}&space;\right&space;\}^2&space;\" title="E_D({\bf w})=\dfrac{1}{2}\sum_{n=1}^{N}\left \{ t_n-w_0-\sum_{j=1}^{M-1}{w_j\phi_j({\bf x_n})} \right \}^2 \" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?w_0=\bar{t}-\sum_{j=1}^{M-1}{w_j\bar{\phi_j}}" title="w_0=\bar{t}-\sum_{j=1}^{M-1}{w_j\bar{\phi_j}}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\bar{t}=\frac{1}{N}\sum_{n=1}^{N}t_{n},&space;\bar{\Phi}_{j}=\frac{1}{N}\sum_{n=1}^{N}&space;\Phi_{j}(\bf&space;x_n)" title="\bar{t}=\frac{1}{N}\sum_{n=1}^{N}t_{n}, \bar{\Phi}_{j}=\frac{1}{N}\sum_{n=1}^{N} \Phi_{j}(\bf x_n)" />   
      
      > 이때 <img src="https://latex.codecogs.com/gif.latex?\bar{\Phi}_{j}" title="\bar{\Phi}_{j}" />는 <img src="https://latex.codecogs.com/gif.latex?\sum&space;w_{j},&space;\bar{t}" title="\sum w_{j}, \bar{t}" />의 차이를 보정해주는 역할 ❗   
      
      > 위의 로그우도함수 식에서 β에 대해 편미분을 통해 최적값을 구할수 있음  
      
      > <img src="https://latex.codecogs.com/gif.latex?\dfrac{1}{\beta_{ML}}=\dfrac{1}{N}\sum_{n=1}^{N}{(t_n-{\bf&space;w_{ML}^T\phi(x_n)})}^2&space;\" title="\dfrac{1}{\beta_{ML}}=\dfrac{1}{N}\sum_{n=1}^{N}{(t_n-{\bf w_{ML}^T\phi(x_n)})}^2 \" />
      
+ 기하학적 의미

   + span, range, projection 복습 > 선형대수
   
   + 행렬 A에 관한 사영 
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{Proj}(\bf&space;t;|\left&space;\{&space;\bf&space;x_{1},&space;\bf&space;x_{2},&space;...,&space;\bf&space;x_{n}&space;\right&space;\})=argmin_{v&space;\&space;in&space;\mathit{R}(\mathbf{A})}\left&space;\|&space;\mathbf{t}-\mathbf{v}&space;\right&space;\|_{2}=A(A^{T}A)^{-1}A^{T}t" title="\mathbf{Proj}(\bf t;|\left \{ \bf x_{1}, \bf x_{2}, ..., \bf x_{n} \right \})=argmin_{v \ in \mathit{R}(\mathbf{A})}\left \| \mathbf{t}-\mathbf{v} \right \|_{2}=A(A^{T}A)^{-1}A^{T}t" />   
      
      > <img src="https://user-images.githubusercontent.com/72974863/104315357-2dc1fd80-551e-11eb-87d0-734a7ee3afe5.png" width="30%" height="30%">   
      
           
## 온라인 학습 (Sequential Learning)

+ 데이터의 사이즈가 너무 크면 계산이 어려움 -> 여러 대안이 존재, 그 중 하나
+ 갖고있는 학습데이터를 조금 나눠서 조금씩 업데이터 진행
+ 데이터가 아무리 크더라도 어느정도 모델 학습 가능

+ 그 중 많이 쓰이는 Stochastic gradient decent 
   
   + 에러함수가 <img src="https://latex.codecogs.com/gif.latex?E=\sum_{n}&space;E_{n}" title="E=\sum_{n} E_{n}" />라 할때, <img src="https://latex.codecogs.com/gif.latex?\mathbf{w}^{\tau&plus;1}=\mathbf{w}^{\tau}-\eta&space;\bigtriangledown&space;E_{n}" title="\mathbf{w}^{\tau+1}=\mathbf{w}^{\tau}-\eta \bigtriangledown E_{n}" />으로  학습 진행
   
      > 제곱합 에러함수인 경우,

      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{w}^{\left&space;(\tau&plus;1&space;\right&space;)}=\mathbf{w}^{\tau}&plus;\eta&space;\left&space;(&space;t_{n}-{\mathbf{w}^{\left&space;(\tau&space;\right&space;)}}^{T}&space;\mathbf{\phi}_{n}&space;\right&space;)\mathbf{\phi}_{n}" title="\mathbf{w}^{\left (\tau+1 \right )}=\mathbf{w}^{\tau}+\eta \left ( t_{n}-{\mathbf{w}^{\left (\tau \right )}}^{T} \mathbf{\phi}_{n} \right )\mathbf{\phi}_{n}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{\phi}_{n}=\mathbf{\phi}\left&space;(&space;\mathbf{x}_{n}&space;\right&space;)" title="\mathbf{\phi}_{n}=\mathbf{\phi}\left ( \mathbf{x}_{n} \right )" />으로 표현
   
+ 시간은 많이 걸리더라도, 메모리에 대한 부담은 ↓   
+ [관련 실습 ✨](https://github.com/sujiny-tech/k-digital-training-AI-dev/blob/main/Machine-Learning-basics/Linear_Models_for_Reression_example.ipynb)   


## 규제화된 최소제곱법(Regularized Least Squares)

+ 에러함수의 가장 단순한 형태

   > <img src="https://latex.codecogs.com/gif.latex?E({\bf&space;w})=E_D({\bf&space;w})&plus;{\lambda}E_{W}({\bf&space;w})&space;\" title="E({\bf w})=E_D({\bf w})+{\lambda}E_{W}({\bf w}) \" />   
   
   > lambda에 의해 규제화 컨트롤
   
   > <img src="https://latex.codecogs.com/gif.latex?E_W({\bf&space;w})=\dfrac{1}{2}{\bf&space;w^Tw}" title="E_W({\bf w})=\dfrac{1}{2}{\bf w^Tw}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?E_D({\bf&space;w})=\dfrac{1}{2}\sum_{n=1}^{N}{t_n-{\bf&space;w}^T\phi({\bf&space;x}_n)}^2" title="E_D({\bf w})=\dfrac{1}{2}\sum_{n=1}^{N}{t_n-{\bf w}^T\phi({\bf x}_n)}^2" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?E({\bf&space;w})=\dfrac{1}{2}\sum_{n=1}^{N}{t_n-{\bf&space;w}^T\phi({\bf&space;x}_n)}^2&plus;\dfrac{1}{2}{\bf&space;w^Tw}" title="E({\bf w})=\dfrac{1}{2}\sum_{n=1}^{N}{t_n-{\bf w}^T\phi({\bf x}_n)}^2+\dfrac{1}{2}{\bf w^Tw}" />   
   
   > w에 대해 미분하고, 정리하면 w의 최적값 -> <img src="https://latex.codecogs.com/gif.latex?{\bf&space;w}=({\lambda}I&plus;\Phi^T\Phi)^{-1}\Phi^T{\bf&space;t}" title="{\bf w}=({\lambda}I+\Phi^T\Phi)^{-1}\Phi^T{\bf t}" />   
   
  
+ 일반화된 규제화 
   
   > <img src="https://latex.codecogs.com/gif.latex?E({\bf&space;w})=\dfrac{1}{2}\sum_{n=1}^{N}{t_n-{\bf&space;w}^T\phi({\bf&space;x}n)}^2&plus;\dfrac{1}{2}{\sum_{j=1}^{M}\left&space;|&space;\mathbf{w}_j&space;\right&space;|^{q}}" title="E({\bf w})=\dfrac{1}{2}\sum_{n=1}^{N}{t_n-{\bf w}^T\phi({\bf x}n)}^2+\dfrac{1}{2}{\sum_{j=1}^{M}\left | \mathbf{w}_j \right |^{q}}" />   
   
   + 이때, 제약조건을 두어 생각하면 (constrained minimization 문제로 나타내면),
   
      > <img src="https://latex.codecogs.com/gif.latex?\dfrac{1}{2}{\sum_{j=1}^{M}\left&space;|&space;\mathbf{w}_j&space;\right&space;|^{q}}&space;\leq&space;\eta" title="\dfrac{1}{2}{\sum_{j=1}^{M}\left | \mathbf{w}_j \right |^{q}} \leq \eta" />를 만족하면서 <img src="https://latex.codecogs.com/gif.latex?E({\bf&space;w})=\dfrac{1}{2}\sum_{n=1}^{N}{t_n-{\bf&space;w}^T\phi({\bf&space;x}_n)}^2" title="E({\bf w})=\dfrac{1}{2}\sum_{n=1}^{N}{t_n-{\bf w}^T\phi({\bf x}_n)}^2" />를 최소화시키는 해 찾기 !   
   
      > <img src="https://user-images.githubusercontent.com/72974863/104318041-33214700-5522-11eb-93dc-13fc4c6cd2c9.png" width="50%" height="50%">   
   
## 편향-분산 분해(Bias-Variance Decomposition)

+ **모델 과적합에 대한 이론적인 분석**

+ 제곱합 손실함수가 주어졌을때의 최적 예측값

   > <img src="https://latex.codecogs.com/gif.latex?h(\mathbf{x})=E[t|\mathbf{x}]=\int&space;t&space;p(t|\mathbf{x})dt" title="h(\mathbf{x})=E[t|\mathbf{x}]=\int t p(t|\mathbf{x})dt" />   
   
   
+ 손실함수의 기댓값
   
   > <img src="https://latex.codecogs.com/gif.latex?E[L]=\int&space;\left&space;\{&space;y(\mathbf{x}-h(\mathbf{x}))&space;\right&space;\}^{2}p(\mathbf{x})d\mathbf{x}=\int&space;\int&space;\left&space;\{&space;h(\mathbf{x}-t)&space;\right&space;\}^{2}d\mathbf{x}dt" title="E[L]=\int \left \{ y(\mathbf{x}-h(\mathbf{x})) \right \}^{2}p(\mathbf{x})d\mathbf{x}=\int \int \left \{ h(\mathbf{x}-t) \right \}^{2}d\mathbf{x}dt" />   
   
   > 제한된 데이터셋만 알아서는 최적 예측값 h(x)를 알수 없다.
   
   > 따라서 모델의 불확실성을 표현하기 위해서는 베이지안/빈도주의 방법이 있음
   
   + 베이지안 방법은 모델 파라미터 w의 사후확률분포를 계산
   
   + 빈도주의 방법은 w의 점추정값을 구하고, 여러 데이터셋에 대해 발생하는 평균적인 손실을 계산하는 **가상 실험**을 통해 점추정값의 불확실성을 해석 ❗

/ 빈도주의 방법... 

+ 특정 데이터 셋 D에 대한 손실

   > <img src="https://latex.codecogs.com/gif.latex?L(D)=\left&space;\{&space;y(\mathbf{x};D)-h(\mathbf{x})&space;\right&space;\}^{2}" title="L(D)=\left \{ y(\mathbf{x};D)-h(\mathbf{x}) \right \}^{2}" />   
   
   
+ 손실 함수의 기댓값
   > <img src="https://latex.codecogs.com/gif.latex?E[L(D)]=\int&space;\left&space;\{&space;y(\mathbf{x};D)-h(\mathbf{x})&space;\right&space;\}^{2}&space;p(\mathbf{x})d\mathbf{x}&plus;\textup{noise}" title="E[L(D)]=\int \left \{ y(\mathbf{x};D)-h(\mathbf{x}) \right \}^{2} p(\mathbf{x})d\mathbf{x}+\textup{noise}" />   
   
+ 여러 개(L개)의 데이터셋이 주어졌을 떄, 이 값들의 평균?

   > <img src="https://latex.codecogs.com/gif.latex?\frac{1}{L}\sum_{l=1}^{L}\left&space;[&space;\int&space;\left&space;\{&space;y(\mathbf{x};D)-h(\mathbf{x})&space;\right&space;\}^{2}&space;p(\mathbf{x})d\mathbf{x}&plus;\textup{noise}&space;\right&space;]" title="\frac{1}{L}\sum_{l=1}^{L}\left [ \int \left \{ y(\mathbf{x};D)-h(\mathbf{x}) \right \}^{2} p(\mathbf{x})d\mathbf{x}+\textup{noise} \right ]" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?=\int&space;E[D]\left&space;[&space;\left&space;\{&space;y(\mathbf{x};D)-h(\mathbf{x})&space;\right&space;\}^{2}&space;\right&space;]p(\mathbf{x})d\mathbf{x}&plus;\textup{noise}" title="=\int E[D]\left [ \left \{ y(\mathbf{x};D)-h(\mathbf{x}) \right \}^{2} \right ]p(\mathbf{x})d\mathbf{x}+\textup{noise}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\left&space;\{&space;y(\mathbf{x};D)-h(\mathbf{x})&space;\right&space;\}^{2}" title="\left \{ y(\mathbf{x};D)-h(\mathbf{x}) \right \}^{2}" />에 대해 변형하면
   
   > <img src="https://latex.codecogs.com/gif.latex?\because&space;\left&space;\{&space;y(\mathbf{x};D)-E_D[y(\mathbf{x};D)]&plus;E_D[y(\mathbf{x};D)]-h(\mathbf{x})&space;\right&space;\}^2&space;\\&space;=\left&space;\{&space;y(\mathbf{x};D)-E_D[y(\mathbf{x};D)]&space;\right&space;\}^2&plus;\left&space;\{&space;E_D[y(\mathbf{x};D)-h(\mathbf{x})]&space;\right&space;\}^2&space;\\&space;&plus;2\left&space;\{&space;y(\mathbf{x};D)-E_D[y(\mathbf{x};D)]&space;\right&space;\}\left&space;\{&space;E_D(\mathbf{x};D)-h(\mathbf{x})&space;\right&space;\}" title="\because \left \{ y(\mathbf{x};D)-E_D[y(\mathbf{x};D)]+E_D[y(\mathbf{x};D)]-h(\mathbf{x}) \right \}^2 \\ =\left \{ y(\mathbf{x};D)-E_D[y(\mathbf{x};D)] \right \}^2+\left \{ E_D[y(\mathbf{x};D)-h(\mathbf{x})] \right \}^2 \\ +2\left \{ y(\mathbf{x};D)-E_D[y(\mathbf{x};D)] \right \}\left \{ E_D(\mathbf{x};D)-h(\mathbf{x}) \right \}" />   
   
   > 따라서,
   
   > <img src="https://latex.codecogs.com/gif.latex?E_D[\left&space;\{&space;y({\bf&space;x};D)-h({\bf&space;x})&space;\right&space;\}^2]\&space;=&space;\left&space;\{&space;E_D[y({\bf&space;x};D)]-h({\bf&space;x})&space;\right&space;\}^2&plus;&space;E_D[\left&space;\{&space;y({\bf&space;x};D)-E_D[y({\bf&space;x};D)]&space;\right&space;\}^2]" title="E_D[\left \{ y({\bf x};D)-h({\bf x}) \right \}^2]\ = \left \{ E_D[y({\bf x};D)]-h({\bf x}) \right \}^2+ E_D[\left \{ y({\bf x};D)-E_D[y({\bf x};D)] \right \}^2]" />   
   
+ 정리하면, <img src="https://latex.codecogs.com/gif.latex?\textup{Expected&space;loss}&space;=&space;(bias)^2&space;&plus;&space;variance&space;&plus;&space;noise" title="\textup{Expected loss} = (bias)^2 + variance + noise" />   

   + <img src="https://latex.codecogs.com/gif.latex?(bias)^2=\int{{\left&space;\{&space;E_D[y(\mathbf{x};D)]-h(\mathbf{x})&space;\right&space;\}}^2p(\mathbf{x})d\mathbf{x}}" title="(bias)^2=\int{{\left \{ E_D[y(\mathbf{x};D)]-h(\mathbf{x}) \right \}}^2p(\mathbf{x})d\mathbf{x}}" />   
   
   + <img src="https://latex.codecogs.com/gif.latex?variance&space;=&space;\int{E_D[{\left&space;\{&space;y(\mathbf{x};D)-E_D[y(\mathbf{x};D)]&space;\right&space;\}}^2]p(\mathbf{x})d\mathbf{x}}" title="variance = \int{E_D[{\left \{ y(\mathbf{x};D)-E_D[y(\mathbf{x};D)] \right \}}^2]p(\mathbf{x})d\mathbf{x}}" />   
   
   + <img src="https://latex.codecogs.com/gif.latex?noise=\iint{{\left&space;\{&space;h(\mathbf{x})-t&space;\right&space;\}}^2p(\mathbf{x},t)d\mathbf{x}dt}" title="noise=\iint{{\left \{ h(\mathbf{x})-t \right \}}^2p(\mathbf{x},t)d\mathbf{x}dt}" />   
   
   + 자유도 ↑, 복잡도 ↑, var ↑, bias^2 ↓ (var, bias : trade-off)   
   
   + 모델학습에 적절한 모델복잡도(자유도)를 가질수 있도록 해야 좋은 모델(새로운 데이터에 대해 너무 과적합되지 않은 결과를 낼 수 있는 모델) ❗
   
   
## 베이지안 선형회귀(Bayesian Linear Regression)
 
+ 위에서 처럼 빈도주의방법으로는 모델의 불확실성을 나타내기 힘듦 ❗ 베이지안 선형회귀를 통해 훨씬 더 불확실성을 깔끔하게 다룰 수 있음 ❗   
 
+ 파라미터 w의 사전확률
 
   > <img src="https://latex.codecogs.com/gif.latex?p({\bf&space;w})&space;=&space;N({\bf&space;w}|{\bf&space;m}_0,&space;{\bf&space;S}_0)" title="p({\bf w}) = N({\bf w}|{\bf m}_0, {\bf S}_0)" />   
    
+ 우도
   > <img src="https://latex.codecogs.com/gif.latex?p({\mathbf{t}|\bf&space;w})&space;=&space;p(t_1,&space;...,&space;t_N|\mathbf{w})=\prod&space;_{n=1}^{N}&space;N(t_n|\mathbf{w}^{T}\phi(\mathbf{x}_n),&space;\beta^{-1})=N(\mathbf{t}|\Phi&space;\mathbf{w},&space;\beta^{-1}\mathbf{I})" title="p({\mathbf{t}|\bf w}) = p(t_1, ..., t_N|\mathbf{w})=\prod _{n=1}^{N} N(t_n|\mathbf{w}^{T}\phi(\mathbf{x}_n), \beta^{-1})=N(\mathbf{t}|\Phi \mathbf{w}, \beta^{-1}\mathbf{I})" />   
    
+ 사후확률 
   > <img src="https://latex.codecogs.com/gif.latex?p({\bf&space;w}|{\bf&space;t})&space;=&space;N({\bf&space;w}|{\bf&space;m}_N,&space;{\bf&space;S}_N)" title="p({\bf w}|{\bf t}) = N({\bf w}|{\bf m}_N, {\bf S}_N)" />   
   
   > (using 가우시안 분포를 위한 베이즈 정리)
   
   > <img src="https://latex.codecogs.com/gif.latex?{\bf&space;S}_N&space;=&space;\left&space;({\bf&space;S}_0^{-1}&plus;\beta\Phi^T\Phi&space;\right&space;)^{-1}" title="{\bf S}_N = \left ({\bf S}_0^{-1}+\beta\Phi^T\Phi \right )^{-1}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?{\bf&space;S}_N^{-1}&space;=&space;{\bf&space;S}_0^{-1}&plus;\beta\Phi^T\Phi" title="{\bf S}_N^{-1} = {\bf S}_0^{-1}+\beta\Phi^T\Phi" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?{\bf&space;m}_N&space;=&space;{\bf&space;S}_N(S_0^{-1}{\bf&space;m}_0&plus;\beta\Phi^T{\bf&space;t})" title="{\bf m}_N = {\bf S}_N(S_0^{-1}{\bf m}_0+\beta\Phi^T{\bf t})" />   
   
   > 사전 확률의 공분산 <img src="https://latex.codecogs.com/gif.latex?S_{0}=\alpha^{-1}\mathbf{I},&space;\alpha\rightarrow&space;0" title="S_{0}=\alpha^{-1}\mathbf{I}, \alpha\rightarrow 0" />이라고 가정하면,
   
   > <img src="https://latex.codecogs.com/gif.latex?S_{0}^{-1}\rightarrow&space;0" title="S_{0}^{-1}\rightarrow 0" />, <img src="https://latex.codecogs.com/gif.latex?S_{N}^{-1}\rightarrow&space;\beta\Phi&space;^{T}\Phi" title="S_{N}^{-1}\rightarrow \beta\Phi ^{T}\Phi" /> 수렴
   
   > <img src="https://latex.codecogs.com/gif.latex?S_{N}=\left&space;(&space;\beta\Phi&space;^{T}\Phi&space;\right&space;)^{-1}=\frac{1}{\beta}\left&space;(\Phi&space;^{T}\Phi&space;\right&space;)^{-1}" title="S_{N}=\left ( \beta\Phi ^{T}\Phi \right )^{-1}=\frac{1}{\beta}\left (\Phi ^{T}\Phi \right )^{-1}" /> mN에 대입하면,   
   
   > <img src="https://latex.codecogs.com/gif.latex?m_{N}=\left&space;(\Phi&space;^{T}\Phi&space;\right&space;)^{-1}\Phi^{T}\mathbf{t}" title="m_{N}=\left (\Phi ^{T}\Phi \right )^{-1}\Phi^{T}\mathbf{t}" /> (normal equations)   
   
+ 사후확률의 로그값

   > <img src="https://latex.codecogs.com/gif.latex?\ln&space;p({\bf&space;w}|{\bf&space;t})&space;=&space;-\frac{\beta}{2}\sum_{n=1}^{N}{\left&space;\{&space;t_n-{\bf&space;w}^T\phi({\bf&space;x}_n)&space;\right&space;\}}^2&space;-&space;\frac{\alpha}{2}{\bf&space;w}^T{\bf&space;w}&plus;\textup{const}" title="\ln p({\bf w}|{\bf t}) = -\frac{\beta}{2}\sum_{n=1}^{N}{\left \{ t_n-{\bf w}^T\phi({\bf x}_n) \right \}}^2 - \frac{\alpha}{2}{\bf w}^T{\bf w}+\textup{const}" />   
   
+ 베이지안 방법은 빈도주의보다 일반적이고, 강력한 방법론 ❗   
 
 
+ 예측값의 분포를 구할 수 있음 ❗

+ 예측 분포 (Predictive Distribution)

   + 새로운 입력 x이 주어졌을 때, t 예측
   
      > <img src="https://latex.codecogs.com/gif.latex?p(t|{\bf&space;t},&space;\alpha,&space;\beta)&space;=&space;\int&space;p(t|{\bf&space;w},&space;\beta)p({\bf&space;w}|{\bf&space;t},&space;\alpha,&space;\beta)d{\bf&space;w}" title="p(t|{\bf t}, \alpha, \beta) = \int p(t|{\bf w}, \beta)p({\bf w}|{\bf t}, \alpha, \beta)d{\bf w}" />   
      
   + 이전 결과 적용하면,
   
      > <img src="https://latex.codecogs.com/gif.latex?p(t|{\bf&space;x},&space;{\bf&space;t},&space;\alpha,&space;\beta)&space;=&space;N\left&space;(&space;t|\phi(\mathbf{x})^{T}\mathbf{m}_N,&space;\beta^{-1}&space;&plus;\phi(\mathbf{x})^{T}\mathbf{S}_N\phi(\mathbf{x})&space;\right&space;)" title="p(t|{\bf x}, {\bf t}, \alpha, \beta) = N\left ( t|\phi(\mathbf{x})^{T}\mathbf{m}_N, \beta^{-1} +\phi(\mathbf{x})^{T}\mathbf{S}_N\phi(\mathbf{x}) \right )" />   
    
    
+ [공부하면서 참고한 사이트 ✨](http://norman3.github.io/prml/docs/chapter03/1.html) 
