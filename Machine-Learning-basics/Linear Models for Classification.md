# 선형 분류(Linear Classification)

+ 분류 목표 : 입력벡터 **x**를 **K**개의 가능한 클래스 중 하나의 클래스로 할당

+ 분류를 위한 결정이론 
   + **확률적 모델(probabilistic model)**
      + 생성모델(generative model)   
      
         > <img src="https://latex.codecogs.com/gif.latex?p({\bf&space;x}|\mathcal{C}_k),&space;p(\mathcal{C}_k)&space;\rightarrow&space;p(\mathcal{C}_k|\bf&space;x)" title="p({\bf x}|\mathcal{C}_k), p(\mathcal{C}_k) \rightarrow p(\mathcal{C}_k|\bf x)" /> 클래스의 사후확률 (using 베이즈 정리) 또는 <img src="https://latex.codecogs.com/gif.latex?p({\bf&space;x}|\mathcal{C}_k)" title="p({\bf x}|\mathcal{C}_k)" /> 직접 모델링   
         
      + 식별모델(discriminative model)   
      
         > <img src="https://latex.codecogs.com/gif.latex?p(\mathcal{C}_k|{\bf&space;x})" title="p(\mathcal{C}_k|{\bf x})" /> 직접 모델링
      
   + **판별함수(discriminant model)** 
   
      > 확률 계산 없이 입력 **x**를 클래스로 할당하는 판별함수 구하기(찾기)
      
## 판별함수 (Discriminant model)   

+ 선형함수에 관한 판별함수에 대해 생각하자.

+ 두개의 클래스에 대한 선형판별함수
   > <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;x})={\bf&space;w^Tx}&plus;w_0" title="y({\bf x})={\bf w^Tx}+w_0" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\bf&space;w" title="\bf w" /> : wight vector   
      
   > <img src="https://latex.codecogs.com/gif.latex?w_0" title="w_0" /> : bias   
   
   > <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;x})&space;\ge&space;0" title="y({\bf x}) \ge 0" />이면 클래스 1로 판별, <0이면 클래스 2로 판별   
   
+ **결정 경계(decision boundary)**
   + y(**x**)=0을 만족하는 **x**의 집합 (**x**가 D차원의 입력벡터일 때, D-1차원의 hyperplane)
   
   + 결정 경계면 위 <img src="https://latex.codecogs.com/gif.latex?{\bf&space;x}_A,&space;{\bf&space;x}_B" title="{\bf x}_A, {\bf x}_B" />   
   
      > <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;x}_A)=y({\bf&space;x}_B)=0" title="y({\bf x}_A)=y({\bf x}_B)=0" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?{\bf&space;w^T}({\bf&space;x}_A-{\bf&space;x}_B)=0" title="{\bf w^T}({\bf x}_A-{\bf x}_B)=0" /> → 즉, <img src="https://latex.codecogs.com/gif.latex?w^{T}" title="w^{T}" />는 결정경계면에 수직   
      
   + 원점에서 결정 경계면까지의 거리
   
      + 벡터 x⊥ : 원점에서 결정 경계면에 대한 사영(projection)일 때 (아래 그림 참고)
         
         > <img src="https://latex.codecogs.com/gif.latex?r\frac{{\bf&space;w}}{\|&space;{\bf&space;w}\|}&space;=&space;{\bf&space;w}_{\perp}" title="r\frac{{\bf w}}{\| {\bf w}\|} = {\bf w}_{\perp}" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;w}_{\perp})&space;=&space;0&space;\Rightarrow&space;{\bf&space;w}^T{\bf&space;w}_{\perp}&space;&plus;&space;w_0&space;=&space;0" title="y({\bf w}_{\perp}) = 0 \Rightarrow {\bf w}^T{\bf w}_{\perp} + w_0 = 0" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?\Rightarrow&space;\frac{{\bf&space;w}^T{\bf&space;w}}{\|{\bf&space;w}\|}r&space;&plus;&space;w_0&space;=&space;0" title="\Rightarrow \frac{{\bf w}^T{\bf w}}{\|{\bf w}\|}r + w_0 = 0" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?\Rightarrow&space;\|{\bf&space;w}\|&space;r&space;&plus;&space;w_0&space;=&space;0" title="\Rightarrow \|{\bf w}\| r + w_0 = 0" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?\Rightarrow&space;r&space;=&space;-\dfrac{w_0}{\|{\bf&space;w}\|}" title="\Rightarrow r = -\dfrac{w_0}{\|{\bf w}\|}" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?w_0<0" title="w_0<0" />이면, 결정 경계면은 원점으로부터 **w**가 향하는 방향으로 멀어져있음.
         
         > <img src="https://latex.codecogs.com/gif.latex?w_0>0" title="w_0>0" />이면, 결정 경계면은 원점으로부터 **w**가 반대 방향으로 멀어져있음.
         
         > 즉, <img src="https://latex.codecogs.com/gif.latex?w_0" title="w_0" />는 결정 경계면 위치 결정 ❗   
         

         
      + x⊥ : 임의의 한점 **x**의 결정 경계면에 대한 사영일 때
          
         > y(**x**)는 **x**와 결정 경계면 사이의 부호화된 거리에 비례
          
         > <img src="https://latex.codecogs.com/gif.latex?{\bf&space;x}={\bf&space;x}_\perp&space;&plus;&space;r\dfrac{\bf&space;w}{\|{\bf&space;w}\|}" title="{\bf x}={\bf x}_\perp + r\dfrac{\bf w}{\|{\bf w}\|}" />  
          
         > 정리하면,   
          
         > <img src="https://latex.codecogs.com/gif.latex?r=\dfrac{y({\bf&space;x})}{\|{\bf&space;w}\|}" title="r=\dfrac{y({\bf x})}{\|{\bf w}\|}" />
         
         > <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;x})&space;>&space;0" title="y({\bf x}) > 0" />이면, **x**는 결정 경계면 기준으로 **w**가 향하는 방향에 있음   
         
         > <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;x})&space;<&space;0" title="y({\bf x}) < 0" />이면, **x**는 결정 경계면 기준으로 **-w**가 향하는 방향에 있음.   
                  
         > <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;x})" title="y({\bf x})" />의 절댓값이 클수록 더 멀리 떨어져있음.   
         
         
         > <img src="https://user-images.githubusercontent.com/72974863/104458561-e2c3eb00-55ee-11eb-9ead-88dbaab9b5be.png" width="40%" height="40%">    
               
      + (수식 단순화) 가짜입력 dummy input <img src="https://latex.codecogs.com/gif.latex?x_0=1" title="x_0=1" /> 이용
      
         + <img src="https://latex.codecogs.com/gif.latex?{\bf&space;\widetilde{w}}=(w_0,&space;{\bf&space;w})" title="{\bf \widetilde{w}}=(w_0, {\bf w})" />   
         
         + <img src="https://latex.codecogs.com/gif.latex?{\bf&space;\widetilde{x}}=(x_0,&space;{\bf&space;x})" title="{\bf \widetilde{x}}=(x_0, {\bf x})" />   
         
         + <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;x})={\bf&space;\widetilde{w}}^T{\bf&space;\widetilde{x}}" title="y({\bf x})={\bf \widetilde{w}}^T{\bf \widetilde{x}}" />   
         

+ **다수의 클래스**에 대한 판별함수
   + 클래스 <img src="https://latex.codecogs.com/gif.latex?k=1,\ldots,K" title="k=1,\ldots,K" />에 대해 표현하면 다음과 같음.   
   
      > <img src="https://latex.codecogs.com/gif.latex?y_k({\bf&space;x})={\bf&space;w}_k^T{\bf&space;x}&plus;w_{k0}" title="y_k({\bf x})={\bf w}_k^T{\bf x}+w_{k0}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?j{\neq}k" title="j{\neq}k" />일 때, <img src="https://latex.codecogs.com/gif.latex?y_k({\bf&space;x})>y_j({\bf&space;x})" title="y_k({\bf x})>y_j({\bf x})" />를 만족하면, x를 클래스 <img src="https://latex.codecogs.com/gif.latex?C_k" title="C_k" />로 판별   

- - - - - - - - - - - - - -
## 분류를 위한 최소제곱법 (Least squares for classification)   

+ 사실 분류를 위해 최소제곱법 쓰는건 별로 좋지 x

+ 클래스를 판별하는 판별식은 다음과 같음   

   > <img src="https://latex.codecogs.com/gif.latex?y_k({\bf&space;x})={\bf&space;w}k^T{\bf&space;x}&plus;w{k0}" title="y_k({\bf x})={\bf w}k^T{\bf x}+w{k0}" />   

   > 행렬 <img src="https://latex.codecogs.com/gif.latex?\tilde{W}" title="\tilde{W}" />에 대해 나타내면,
   
   > <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;x})=\tilde{W}^T\tilde{\bf&space;x}" title="y({\bf x})=\tilde{W}^T\tilde{\bf x}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\tilde{W}" title="\tilde{W}" />의 k번째 열 : <img src="https://latex.codecogs.com/gif.latex?\tilde{w}_k=(w_{k0},&space;{\bf&space;w}_k^T)^T&space;\" title="\tilde{w}_k=(w_{k0}, {\bf w}_k^T)^T \" />   
   
+ **제곱합 에러 함수(sum-of-squared error function)**
   + 학습 데이터 <img src="https://latex.codecogs.com/gif.latex?\{{\bf&space;x}_n,&space;{\bf&space;t}_n\}" title="\{{\bf x}_n, {\bf t}_n\}" />, <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;n=1,\ldots,N&space;\right&space;)" title="\left ( n=1,\ldots,N \right )" />, n번째항이 <img src="https://latex.codecogs.com/gif.latex?{\bf&space;t}_n^T" title="{\bf t}_n^T" />인 행렬 T, n번째 행이 <img src="https://latex.codecogs.com/gif.latex?{\bf&space;\widetilde{x}}_n^T" title="{\bf \widetilde{x}}_n^T" />인 행렬 <img src="https://latex.codecogs.com/gif.latex?{\bf&space;\widetilde{x}}" title="{\bf \widetilde{x}}" />이 주어졌을 때, 제곱합 에러함수는 다음과 같음.   
   
   > <img src="https://latex.codecogs.com/gif.latex?E_D({\bf&space;\widetilde{W}})&space;=&space;\frac{1}{2}\mathrm{tr}\left\{&space;\left({\bf&space;\widetilde{X}}{\bf&space;\widetilde{W}}-{\bf&space;T}&space;\right)^T&space;\left({\bf&space;\widetilde{X}}{\bf&space;\widetilde{W}}-{\bf&space;T}&space;\right)&space;\right\}" title="E_D({\bf \widetilde{W}}) = \frac{1}{2}\mathrm{tr}\left\{ \left({\bf \widetilde{X}}{\bf \widetilde{W}}-{\bf T} \right)^T \left({\bf \widetilde{X}}{\bf \widetilde{W}}-{\bf T} \right) \right\}" />   
   
   > 유도 과정은 다음과 같음.
   
   > <img src="https://latex.codecogs.com/gif.latex?{\bf&space;\widetilde{X}}&space;=&space;\begin{bmatrix}&space;\vdots\\&space;\rule[.5ex]{1.7ex}{0.5pt}&space;{\bf&space;\widetilde{x}}_n^T&space;\rule[.5ex]{1.7ex}{0.5pt}\\&space;\vdots&space;\end{bmatrix},~~&space;{\bf&space;\widetilde{W}}&space;=&space;\begin{bmatrix}&space;\vert\\&space;\cdots&space;{\bf&space;\widetilde{w}}_k&space;\cdots\\&space;\vert&space;\end{bmatrix},~~&space;{\bf&space;T}=&space;\begin{bmatrix}&space;\vdots\\&space;\rule[.5ex]{1.7ex}{0.5pt}&space;{\bf&space;t}_n^T&space;\rule[.5ex]{1.7ex}{0.5pt}\\&space;\vdots&space;\end{bmatrix}" title="{\bf \widetilde{X}} = \begin{bmatrix} \vdots\\ \rule[.5ex]{1.7ex}{0.5pt} {\bf \widetilde{x}}_n^T \rule[.5ex]{1.7ex}{0.5pt}\\ \vdots \end{bmatrix},~~ {\bf \widetilde{W}} = \begin{bmatrix} \vert\\ \cdots {\bf \widetilde{w}}_k \cdots\\ \vert \end{bmatrix},~~ {\bf T}= \begin{bmatrix} \vdots\\ \rule[.5ex]{1.7ex}{0.5pt} {\bf t}_n^T \rule[.5ex]{1.7ex}{0.5pt}\\ \vdots \end{bmatrix}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;E_D({\bf&space;\widetilde{W}})&space;&=&space;\frac{1}{2}\sum_{n=1}^N\sum_{k=1}^K&space;\left({\bf&space;\widetilde{x}}_n^T{\bf&space;\widetilde{w}}_k&space;-&space;{\bf&space;t}_{nk}\right)^2\\&space;\end{align*}" title="\begin{align*} E_D({\bf \widetilde{W}}) &= \frac{1}{2}\sum_{n=1}^N\sum_{k=1}^K \left({\bf \widetilde{x}}_n^T{\bf \widetilde{w}}_k - {\bf t}_{nk}\right)^2\\ \end{align*}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;&=&space;\frac{1}{2}\sum_{n=1}^N&space;\left(&space;{\bf&space;\widetilde{x}}_n^T&space;{\bf&space;\widetilde{W}}&space;-&space;{\bf&space;t}_n^T&space;\right)&space;\left(&space;{\bf&space;\widetilde{x}}_n^T&space;{\bf&space;\widetilde{W}}&space;-&space;{\bf&space;t}_n^T&space;\right)^T\\&space;&=&space;\frac{1}{2}\sum_{n=1}^N&space;\mathrm{tr}\left\{&space;\left(&space;{\bf&space;\widetilde{x}}_n^T&space;{\bf&space;\widetilde{W}}&space;-&space;{\bf&space;t}_n^T&space;\right)&space;\left(&space;{\bf&space;\widetilde{x}}_n^T&space;{\bf&space;\widetilde{W}}&space;-&space;{\bf&space;t}_n^T&space;\right)^T&space;\right\}\\&space;\end{align*}" title="\begin{align*} &= \frac{1}{2}\sum_{n=1}^N \left( {\bf \widetilde{x}}_n^T {\bf \widetilde{W}} - {\bf t}_n^T \right) \left( {\bf \widetilde{x}}_n^T {\bf \widetilde{W}} - {\bf t}_n^T \right)^T\\ &= \frac{1}{2}\sum_{n=1}^N \mathrm{tr}\left\{ \left( {\bf \widetilde{x}}_n^T {\bf \widetilde{W}} - {\bf t}_n^T \right) \left( {\bf \widetilde{x}}_n^T {\bf \widetilde{W}} - {\bf t}_n^T \right)^T \right\}\\ \end{align*}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\begin{align*}&space;&=&space;\frac{1}{2}\sum_{n=1}^N&space;\mathrm{tr}\left\{&space;\left(&space;{\bf&space;\widetilde{x}}_n^T&space;{\bf&space;\widetilde{W}}&space;-&space;{\bf&space;t}_n^T&space;\right)^T&space;\left(&space;{\bf&space;\widetilde{x}}_n^T&space;{\bf&space;\widetilde{W}}&space;-&space;{\bf&space;t}_n^T&space;\right)&space;\right\}\\&space;&=&space;\frac{1}{2}\mathrm{tr}\left\{&space;\sum_{n=1}^N&space;\left(&space;{\bf&space;\widetilde{x}}_n^T&space;{\bf&space;\widetilde{W}}&space;-&space;{\bf&space;t}_n^T&space;\right)^T&space;\left(&space;{\bf&space;\widetilde{x}}_n^T&space;{\bf&space;\widetilde{W}}&space;-&space;{\bf&space;t}_n^T&space;\right)&space;\right\}\\&space;&=&space;\frac{1}{2}\mathrm{tr}\left\{&space;\left({\bf&space;\widetilde{X}}{\bf&space;\widetilde{W}}-{\bf&space;T}&space;\right)^T&space;\left({\bf&space;\widetilde{X}}{\bf&space;\widetilde{W}}-{\bf&space;T}&space;\right)&space;\right\}&space;\end{align*}" title="\begin{align*} &= \frac{1}{2}\sum_{n=1}^N \mathrm{tr}\left\{ \left( {\bf \widetilde{x}}_n^T {\bf \widetilde{W}} - {\bf t}_n^T \right)^T \left( {\bf \widetilde{x}}_n^T {\bf \widetilde{W}} - {\bf t}_n^T \right) \right\}\\ &= \frac{1}{2}\mathrm{tr}\left\{ \sum_{n=1}^N \left( {\bf \widetilde{x}}_n^T {\bf \widetilde{W}} - {\bf t}_n^T \right)^T \left( {\bf \widetilde{x}}_n^T {\bf \widetilde{W}} - {\bf t}_n^T \right) \right\}\\ &= \frac{1}{2}\mathrm{tr}\left\{ \left({\bf \widetilde{X}}{\bf \widetilde{W}}-{\bf T} \right)^T \left({\bf \widetilde{X}}{\bf \widetilde{W}}-{\bf T} \right) \right\} \end{align*}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\tilde{\bf&space;W}" title="\tilde{\bf W}" />에 대해 미분하고 식 전개하면,   
   
   > <img src="https://latex.codecogs.com/gif.latex?\tilde{\bf&space;W}=(\tilde{\bf&space;X}^T\tilde{\bf&space;X})^{-1}\tilde{\bf&space;X}^T\tilde{\bf&space;T}=\tilde{\bf&space;X}^{\dagger}\tilde{\bf&space;T}" title="\tilde{\bf W}=(\tilde{\bf X}^T\tilde{\bf X})^{-1}\tilde{\bf X}^T\tilde{\bf T}=\tilde{\bf X}^{\dagger}\tilde{\bf T}" /> (<img src="https://latex.codecogs.com/gif.latex?\tilde{\bf&space;X}^{\dagger}" title="\tilde{\bf X}^{\dagger}" /> : pseudo-inverse 행렬)    
   
+ 따라서 판별함수는 다음과 같음.

   > <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;x})=\widetilde{\bf&space;W}^T\widetilde{\bf&space;x}={\bf&space;T}^T\left(\widetilde{\bf&space;X}^{\dagger}\right)^T\widetilde{\bf&space;x}" title="y({\bf x})=\widetilde{\bf W}^T\widetilde{\bf x}={\bf T}^T\left(\widetilde{\bf X}^{\dagger}\right)^T\widetilde{\bf x}" />   
   
+ **분류를 위한 최소제곱법의 문제점** ✨
   + outlier에 민감
   + 목표값의 확률분포에 대한 잘못된 가정에 기초 ❗ 
   
- - - - - - - - -

## 퍼셉트론 알고리즘 (The perceptron algorithm)

+ 기저함수를 넣어 일반화된 식으로 표현하면 다음과 같음.  

   > <img src="https://latex.codecogs.com/gif.latex?y({\bf&space;x})=f({\bf&space;w}^T\phi({\bf&space;x}))" title="y({\bf x})=f({\bf w}^T\phi({\bf x}))" />   
   
   > 여기서 <img src="https://latex.codecogs.com/gif.latex?\phi_0({\bf&space;x})=1" title="\phi_0({\bf x})=1" />이며, f는 활성함수(activation function)로 계단형 함수임
   
   > <img src="https://latex.codecogs.com/gif.latex?f(a)=\begin{cases}&space;&plus;1,&space;&&space;a\geq&space;0&space;\\&space;-1,&space;&&space;a<0&space;\end{cases}" title="f(a)=\begin{cases} +1, & a\geq 0 \\ -1, & a<0 \end{cases}" />   
   
+ 에러 함수
   > <img src="https://latex.codecogs.com/gif.latex?E_P({\bf&space;w})=-\sum_{n&space;\in&space;\mathcal{M}}{\bf&space;w}^T\phi_nt_n" title="E_P({\bf w})=-\sum_{n \in \mathcal{M}}{\bf w}^T\phi_nt_n" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\mathcal{M}" title="\mathcal{M}" /> : 잘못 분류된 데이터들의 집합
   
+ Stochastic gradient descent의 적용하면,

   > <img src="https://latex.codecogs.com/gif.latex?{\bf&space;w}^{(\tau&plus;1)}={\bf&space;w}^{(\tau)}-\eta\triangledown&space;E_p({\bf&space;w})={\bf&space;w}^{(\tau)}&plus;\eta\phi_n{t_n}" title="{\bf w}^{(\tau+1)}={\bf w}^{(\tau)}-\eta\triangledown E_p({\bf w})={\bf w}^{(\tau)}+\eta\phi_n{t_n}" />   
   
+ 위 업데이트가 실행될 때 잘못 분류된 샘플에 미치는 영향
   > <img src="https://latex.codecogs.com/gif.latex?-{\bf&space;w}^{(\tau&plus;1)T}{\phi}_n{t_n}&space;=&space;-{\bf&space;w}^{(\tau)T}{\phi_n}{t_n}-(\phi_n{t_n})^T\phi_n{t_n}&space;<&space;-{\bf&space;w}^{(\tau)T}\phi_n{t_n}" title="-{\bf w}^{(\tau+1)T}{\phi}_n{t_n} = -{\bf w}^{(\tau)T}{\phi_n}{t_n}-(\phi_n{t_n})^T\phi_n{t_n} < -{\bf w}^{(\tau)T}\phi_n{t_n}" />   

⭐ 최소제곱법과 퍼셉트론 모두 output 출력하지만, 확률을 계산하진 않음 ❗

- - - - - - - - - - -
      
      
      
      
#### [공부하면서 참고한 사이트 ✨️](http://norman3.github.io/prml/docs/chapter04/0)
