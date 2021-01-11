## 가우시안 분포(Gaussian Distribution)

+ 가우시안 분포가 일어나는 여러가지 상황
   + 정보이론에서 엔트로피를 최대화시키는 확률분포
   + 중심극한 정리   
   
      > ![image](https://user-images.githubusercontent.com/72974863/104146672-d41edd80-540e-11eb-9ae2-e81140f520de.png)   
            
      > [그림 출처](https://ko.wikipedia.org/wiki/%EC%A4%91%EC%8B%AC_%EA%B7%B9%ED%95%9C_%EC%A0%95%EB%A6%AC)
      
+ 단일 변수 x   

   > <img src="https://latex.codecogs.com/gif.latex?N(x|\mu,&space;\sigma^{2})={\frac&space;1{\sigma&space;{\sqrt&space;{2\pi&space;}}}}\;\exp&space;\left(-{\frac&space;{\left(x-\mu&space;\right)^{2}}{2\sigma&space;^{2}}}\right)\!" title="N(x|\mu, \sigma^{2})={\frac 1{\sigma {\sqrt {2\pi }}}}\;\exp \left(-{\frac {\left(x-\mu \right)^{2}}{2\sigma ^{2}}}\right)\!" />   

+ D차원 벡터 x

   > <img src="https://latex.codecogs.com/gif.latex?N(\mathbf{x}|\mathbf{\mu},\mathbf{\Sigma})={\frac&space;1{\left&space;(2\pi&space;\right&space;)&space;^{D/2}}}\frac{1}{\left&space;|&space;\Sigma&space;\right&space;|^{1/2}}\;\exp&space;\left(-\frac{1}{2}\left&space;(\mathbf{x}-\mathbf{\mu}&space;\right&space;)^{T}\Sigma^{-1}\left&space;(&space;\mathbf{x}-\mathbf{\mu}&space;\right&space;)&space;\right)\!" title="N(\mathbf{x}|\mathbf{\mu},\mathbf{\Sigma})={\frac 1{\left (2\pi \right ) ^{D/2}}}\frac{1}{\left | \Sigma \right |^{1/2}}\;\exp \left(-\frac{1}{2}\left (\mathbf{x}-\mathbf{\mu} \right )^{T}\Sigma^{-1}\left ( \mathbf{x}-\mathbf{\mu} \right ) \right)\!" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\mathbf{\mu}" title="\mathbf{\mu}" /> : D차원의 평균 벡터   
      
   > <img src="https://latex.codecogs.com/gif.latex?\mathbf{\Sigma}" title="\mathbf{\Sigma}" /> : DxD크기를 가지는 공분산 행렬   
   
   > 평균과 분산으로 주어진게 아니라 위의 형태의 함수를 가지고 있으며 mu, sigma가 파라미터로 주어져있을 때, 확률밀도함수의 평균과 공분산이 mu, sigma가 된다는 것을 유도 ❗
   
+ 가우시안 분포의 기하학적인 형태

   + x에 대한 함수적 종속성은 지수부에 등장하는 이차형식(quadratic form)
   
      > <img src="https://latex.codecogs.com/gif.latex?\Delta&space;^{2}=\left&space;(&space;\mathbf{x}-\mathbf{\mu}&space;\right&space;)^{T}\Sigma^{-1}\left&space;(&space;\mathbf{x}-\mathbf{\mu}&space;\right&space;)" title="\Delta ^{2}=\left ( \mathbf{x}-\mathbf{\mu} \right )^{T}\Sigma^{-1}\left ( \mathbf{x}-\mathbf{\mu} \right )" />   
      
   + <img src="https://latex.codecogs.com/gif.latex?\mathbf{\Sigma}" title="\mathbf{\Sigma}" />가 공분산으로 주어진 것은 아니므로 처음부터 이 행렬이 대칭이라고 미리 가정할 필요 x ❗    
   
   + 하지만, 선형대수에서 배웠듯 **이차형식에 나타나는 행렬은 오직 대칭부분만이 그 값에 기여한다는 사실**을 기억하자 ❗
   
      > <img src="https://latex.codecogs.com/gif.latex?x^{T}Ax=(x^{T}Ax)^{T}=x^{T}A^{T}x=x^{T}\left&space;(&space;\frac{1}{2}A&space;&plus;\frac{1}{2}A^{T}&space;\right&space;)x" title="x^{T}Ax=(x^{T}Ax)^{T}=x^{T}A^{T}x=x^{T}\left ( \frac{1}{2}A +\frac{1}{2}A^{T} \right )x" />   
      
      > 따라서, <img src="https://latex.codecogs.com/gif.latex?\mathbf{\Sigma}" title="\mathbf{\Sigma}" />가 **대칭행렬인 것**으로 간주할 수 있음.   
      
   + 대칭행렬의 성질에 따라서 <img src="https://latex.codecogs.com/gif.latex?\mathbf{\Sigma}" title="\mathbf{\Sigma}" />를 아래와 같이 나타낼 수 있음.   
   
      > <img src="https://latex.codecogs.com/gif.latex?\Sigma=U^{T}\Lambda&space;U" title="\Sigma=U^{T}\Lambda U" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?U=\begin{bmatrix}&space;-&space;\mathbf{u}_{1}^{T}-\\&space;-&space;\mathbf{u}_{2}^{T}-\\&space;...\\&space;-&space;\mathbf{u}_{D}^{T}-&space;\end{bmatrix},&space;\Lambda&space;=\textup{diag}\left&space;(&space;\lambda_{1},&space;...,&space;\lambda_{D}&space;\right&space;)" title="U=\begin{bmatrix} - \mathbf{u}_{1}^{T}-\\ - \mathbf{u}_{2}^{T}-\\ ...\\ - \mathbf{u}_{D}^{T}- \end{bmatrix}, \Lambda =\textup{diag}\left ( \lambda_{1}, ..., \lambda_{D} \right )" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\Sigma=U^{T}\Lambda&space;U" title="\Sigma=U^{T}\Lambda U" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?=\begin{bmatrix}&space;\mid&space;&&space;\mid&space;&&space;&&space;\mid&space;\\&space;\mathbf{u}_{1}&space;&&space;\mathbf{u}_{2}&space;&&space;...&space;&&space;\mathbf{u}_{D}&space;\\&space;\mid&space;&&space;\mid&space;&&space;&&space;\mid&space;\end{bmatrix}&space;\textup{diag}\left&space;(&space;\lambda_{1},&space;...,&space;\lambda_{D}&space;\right&space;)&space;\begin{bmatrix}&space;-\mathbf{u}_{1}^{T}-\\&space;-\mathbf{u}_{2}^{T}-\\&space;...\\&space;-\mathbf{u}_{D}^{T}-&space;\end{bmatrix}" title="=\begin{bmatrix} \mid & \mid & & \mid \\ \mathbf{u}_{1} & \mathbf{u}_{2} & ... & \mathbf{u}_{D} \\ \mid & \mid & & \mid \end{bmatrix} \textup{diag}\left ( \lambda_{1}, ..., \lambda_{D} \right ) \begin{bmatrix} -\mathbf{u}_{1}^{T}-\\ -\mathbf{u}_{2}^{T}-\\ ...\\ -\mathbf{u}_{D}^{T}- \end{bmatrix}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?=\begin{bmatrix}&space;\mid&space;&&space;\mid&space;&&space;&&space;\mid&space;\\&space;\mathbf{u}_{1}&space;\lambda_{1}&space;&&space;\mathbf{u}_{2}&space;\lambda_{2}&space;&&space;...&space;&&space;\mathbf{u}_{D}&space;\lambda_{D}&space;\\&space;\mid&space;&&space;\mid&space;&&space;&&space;\mid&space;\end{bmatrix}&space;\begin{bmatrix}&space;-\mathbf{u}_{1}^{T}-\\&space;-\mathbf{u}_{2}^{T}-\\&space;...\\&space;-\mathbf{u}_{D}^{T}-&space;\end{bmatrix}" title="=\begin{bmatrix} \mid & \mid & & \mid \\ \mathbf{u}_{1} \lambda_{1} & \mathbf{u}_{2} \lambda_{2} & ... & \mathbf{u}_{D} \lambda_{D} \\ \mid & \mid & & \mid \end{bmatrix} \begin{bmatrix} -\mathbf{u}_{1}^{T}-\\ -\mathbf{u}_{2}^{T}-\\ ...\\ -\mathbf{u}_{D}^{T}- \end{bmatrix}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?=\sum_{i=1}^{D}\lambda_{i}\mathbf{u}_{i}\textbf{u}_{i}^{T}" title="=\sum_{i=1}^{D}\lambda_{i}\mathbf{u}_{i}\textbf{u}_{i}^{T}" />   


   + <img src="https://latex.codecogs.com/gif.latex?\Sigma^{-1}" title="\Sigma^{-1}" /> 쉽게 구할 수 있음.   
   
      > <img src="https://latex.codecogs.com/gif.latex?\Sigma^{-1}=\sum_{i=1}^{D}\frac{1}{\lambda_{i}\mathbf{u}_{i}\mathbf{u}_{i}^{T}}" title="\Sigma^{-1}=\sum_{i=1}^{D}\frac{1}{\lambda_{i}\mathbf{u}_{i}\mathbf{u}_{i}^{T}}" />   
      
   + 이차형식은 다음과 같이 표현
      
      > <img src="https://latex.codecogs.com/gif.latex?\Delta&space;^{2}=\sum_{i=1}^{D}\frac{y_{i}^{2}}{\lambda_{i}}" title="\Delta ^{2}=\sum_{i=1}^{D}\frac{y_{i}^{2}}{\lambda_{i}}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?y_{i}=\mathbf{u}_{i}^{T}&space;\left&space;(&space;\mathbf{x}&space;-&space;\mathbf{\mu}&space;\right&space;)" title="y_{i}=\mathbf{u}_{i}^{T} \left ( \mathbf{x} - \mathbf{\mu} \right )" />   
      
   + 벡터식으로 확장하면
   
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{y}=\mathbf{U}\left&space;(\mathbf{&space;x}&space;-&space;\mathbf{\mu}&space;\right&space;)" title="\mathbf{y}=\mathbf{U}\left (\mathbf{ x} - \mathbf{\mu} \right )" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{y}=\mathbf{U}\left&space;(\mathbf{&space;x}&space;-&space;\mathbf{\mu}&space;\right&space;)=&space;\begin{bmatrix}&space;-\mathbf{u}_{1}^{T}-\\&space;-\mathbf{u}_{2}^{T}-\\&space;...\\&space;-\mathbf{u}_{D}^{T}-&space;\end{bmatrix}\left&space;(\mathbf{&space;x}&space;-&space;\mathbf{\mu}&space;\right&space;)=&space;\begin{bmatrix}&space;-\mathbf{u}_{1}^{T}\left&space;(\mathbf{&space;x}&space;-&space;\mathbf{\mu}&space;\right&space;)-\\&space;-\mathbf{u}_{2}^{T}\left&space;(\mathbf{&space;x}&space;-&space;\mathbf{\mu}&space;\right&space;)-\\&space;...\\&space;-\mathbf{u}_{D}^{T}\left&space;(\mathbf{&space;x}&space;-&space;\mathbf{\mu}&space;\right&space;)-&space;\end{bmatrix}=&space;\begin{bmatrix}&space;-\mathbf{y}_{1}-\\&space;-\mathbf{y}_{2}-\\&space;...\\&space;-\mathbf{y}_{T}-&space;\end{bmatrix}" title="\mathbf{y}=\mathbf{U}\left (\mathbf{ x} - \mathbf{\mu} \right )= \begin{bmatrix} -\mathbf{u}_{1}^{T}-\\ -\mathbf{u}_{2}^{T}-\\ ...\\ -\mathbf{u}_{D}^{T}- \end{bmatrix}\left (\mathbf{ x} - \mathbf{\mu} \right )= \begin{bmatrix} -\mathbf{u}_{1}^{T}\left (\mathbf{ x} - \mathbf{\mu} \right )-\\ -\mathbf{u}_{2}^{T}\left (\mathbf{ x} - \mathbf{\mu} \right )-\\ ...\\ -\mathbf{u}_{D}^{T}\left (\mathbf{ x} - \mathbf{\mu} \right )- \end{bmatrix}= \begin{bmatrix} -\mathbf{y}_{1}-\\ -\mathbf{y}_{2}-\\ ...\\ -\mathbf{y}_{T}- \end{bmatrix}" />   
      
      > y를 벡터들 <img src="https://latex.codecogs.com/gif.latex?\mu_{i}" title="\mu_{i}" />에 의해 정희된 새로운 좌표체계 내의 점으로 해석 → 이를 **기저변환(change of basis)** 라 함.   
      
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{y}=\mathbf{U}\left&space;(\mathbf{&space;x}&space;-&space;\mathbf{\mu}&space;\right&space;)" title="\mathbf{y}=\mathbf{U}\left (\mathbf{ x} - \mathbf{\mu} \right )" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\left&space;(\mathbf{&space;x}&space;-&space;\mathbf{\mu}&space;\right&space;)=\mathbf{U}^{-1}\mathbf{y}" title="\left (\mathbf{ x} - \mathbf{\mu} \right )=\mathbf{U}^{-1}\mathbf{y}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?=\mathbf{U}^{T}\mathbf{y}=\begin{bmatrix}&space;\mid&space;&&space;\mid&space;&&space;&&space;\mid&space;\\&space;\mathbf{u}_{1}&space;&&space;\mathbf{u}_{2}&space;&&space;&&space;\mathbf{u}_{D}\\&space;\mid&space;&&space;\mid&space;&&space;&&space;\mid&space;\end{bmatrix}\mathbf{y}" title="=\mathbf{U}^{T}\mathbf{y}=\begin{bmatrix} \mid & \mid & & \mid \\ \mathbf{u}_{1} & \mathbf{u}_{2} & & \mathbf{u}_{D}\\ \mid & \mid & & \mid \end{bmatrix}\mathbf{y}" />   
            
      > <img src="https://latex.codecogs.com/gif.latex?\left&space;(\mathbf{&space;x}&space;-&space;\mathbf{\mu}&space;\right&space;)" title="\left (\mathbf{ x} - \mathbf{\mu} \right )" /> : standard basis에서의 좌표
      
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{y}" title="\mathbf{y}" /> : basis <img src="https://latex.codecogs.com/gif.latex?\left&space;\{&space;\mathbf{u}_{1},&space;\mathbf{u}_{2},&space;...&space;,&space;\mathbf{u}_{D}&space;\right&space;\}" title="\left \{ \mathbf{u}_{1}, \mathbf{u}_{2}, ... , \mathbf{u}_{D} \right \}" />에서의 좌표   
      
      > <img src="https://user-images.githubusercontent.com/72974863/104159403-95028380-5432-11eb-9d78-3c7281dc4a8e.png" width="30%" height="30%">   
      
      
+ 가우시안 분포의 Normalization 증명

   + <img src="https://latex.codecogs.com/gif.latex?\mathbf{y}" title="\mathbf{y}" />의 확률밀도함수를 구하기 위해서 Jacobian <img src="https://latex.codecogs.com/gif.latex?\mathbf{J}" title="\mathbf{J}" />를 구해야 함 ❗  
      
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{J}_{ij}=\frac{\partial&space;x_{i}}{\partial&space;y_{i}}=U_{ji}=\left&space;(&space;U^{T}&space;\right&space;)_{ij}" title="\mathbf{J}_{ij}=\frac{\partial x_{i}}{\partial y_{i}}=U_{ji}=\left ( U^{T} \right )_{ij}" />    
      
      > <img src="https://latex.codecogs.com/gif.latex?\left&space;|\mathbf{J}&space;\right&space;|^{2}=\left&space;|U^{T}&space;\right&space;|^{2}=\left&space;|U^{T}&space;\right&space;|&space;\left&space;|U&space;\right&space;|=\left&space;|U^{T}U&space;\right&space;|=\left&space;|\mathbf{I}&space;\right&space;|=1" title="\left |\mathbf{J} \right |^{2}=\left |U^{T} \right |^{2}=\left |U^{T} \right | \left |U \right |=\left |U^{T}U \right |=\left |\mathbf{I} \right |=1" />   
            
   + 행렬식 <img src="https://latex.codecogs.com/gif.latex?\left&space;|&space;\Sigma&space;\right&space;|" title="\left | \Sigma \right |" />는 고유값의 곱으로 나타낼 수 있음
   
      > <img src="https://latex.codecogs.com/gif.latex?\left&space;|&space;\Sigma&space;\right&space;|^{1/2}=\prod_{j=1}^{D}&space;\lambda_{j}^{1/2}" title="\left | \Sigma \right |^{1/2}=\prod_{j=1}^{D} \lambda_{j}^{1/2}" />   
      
   + 따라서, y의 확률밀도함수는 다음과 같음.
   
      > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{y})=p(\mathbf{x})\left&space;|&space;\mathbf{J}&space;\right&space;|=\prod_{j=1}^{D}\frac{1}{\left&space;(&space;2&space;\pi&space;\lambda_{j}&space;\right&space;)^{1/2}}&space;\textup{exp}\left&space;\{&space;-\frac{y_{i}^{2}}{2\lambda_{j}}&space;\right&space;\}" title="p(\mathbf{y})=p(\mathbf{x})\left | \mathbf{J} \right |=\prod_{j=1}^{D}\frac{1}{\left ( 2 \pi \lambda_{j} \right )^{1/2}} \textup{exp}\left \{ -\frac{y_{i}^{2}}{2\lambda_{j}} \right \}" />   
      
   + y의 normalization
      
      > <img src="https://latex.codecogs.com/gif.latex?\int&space;p(\mathbf{y})d\mathbf{y}=\prod_{j=1}^{D}\int_{-\infty}^{\infty}\frac{1}{\left&space;(&space;2\pi&space;\lambda_{j}&space;\right&space;)^{1/2}}&space;\textup{exp}\left&space;\{&space;-\frac{y_{j}^{2}}{2\lambda_{j}}&space;\right&space;\}dy_{j}=1" title="\int p(\mathbf{y})d\mathbf{y}=\prod_{j=1}^{D}\int_{-\infty}^{\infty}\frac{1}{\left ( 2\pi \lambda_{j} \right )^{1/2}} \textup{exp}\left \{ -\frac{y_{j}^{2}}{2\lambda_{j}} \right \}dy_{j}=1" />   
      
      
+ 가우시안 분포의 기댓값
   
   + 다변량(multivariate) 확률변수의 기댓값   
   
      + <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}=\left&space;(&space;x_{1},&space;...&space;,&space;x_{n}&space;\right&space;)^{T}" title="\mathbf{x}=\left ( x_{1}, ... , x_{n} \right )^{T}" />   
      
      + <img src="https://latex.codecogs.com/gif.latex?E[\mathbf{x}]=\left&space;(&space;E[x_{1}],&space;...,&space;E[x_{n}]&space;\right&space;)^{T}" title="E[\mathbf{x}]=\left ( E[x_{1}], ..., E[x_{n}] \right )^{T}" />   
      
      + <img src="https://latex.codecogs.com/gif.latex?E[x_{1}]=\int&space;x_{1}p(x_{1})dx_{1}=\int&space;x_{1}\left&space;(&space;\int&space;p(x_{1},&space;...,&space;x_{n})dx_{2},&space;...,&space;dx_{n}&space;\right&space;)dx_{1}=\int&space;x_{1}p(x_{1},&space;...,&space;x_{n})dx_{1},&space;...,&space;dx_{n}" title="E[x_{1}]=\int x_{1}p(x_{1})dx_{1}=\int x_{1}\left ( \int p(x_{1}, ..., x_{n})dx_{2}, ..., dx_{n} \right )dx_{1}=\int x_{1}p(x_{1}, ..., x_{n})dx_{1}, ..., dx_{n}" />   
 
   
   + 가우시안 분포의 기댓값 계산
   
      > <img src="https://latex.codecogs.com/gif.latex?E[\mathbf{x}]=\frac{1}{\left&space;(&space;2\pi&space;\right&space;)^{D/2}}\frac{1}{\left&space;|&space;\Sigma&space;\right&space;|^{1/2}}\int&space;\textup{exp}\left&space;\{&space;-\frac{1}{2}\left&space;(&space;\mathbf{x}-\mathbf{\mu}&space;\right&space;)^{T}&space;\Sigma^{-1}\left&space;(&space;\mathbf{x}-&space;\mathbf{\mu}&space;\right&space;)&space;\right&space;\}\mathbf{x}&space;d\mathbf{x}" title="E[\mathbf{x}]=\frac{1}{\left ( 2\pi \right )^{D/2}}\frac{1}{\left | \Sigma \right |^{1/2}}\int \textup{exp}\left \{ -\frac{1}{2}\left ( \mathbf{x}-\mathbf{\mu} \right )^{T} \Sigma^{-1}\left ( \mathbf{x}- \mathbf{\mu} \right ) \right \}\mathbf{x} d\mathbf{x}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?=\frac{1}{\left&space;(&space;2\pi&space;\right&space;)^{D/2}}\frac{1}{\left&space;|&space;\Sigma&space;\right&space;|^{1/2}}\int&space;\textup{exp}\left&space;\{&space;-\frac{1}{2}\mathbf{z}^{T}&space;\Sigma^{-1}\mathbf{z}&space;\right&space;\}\left&space;(\mathbf{z}&plus;\mathbf{\mu}&space;\right&space;)&space;d\mathbf{z}&space;\begin{matrix}&space;&&space;\end{matrix}\left&space;(&space;\textup{by&space;}&space;\mathbf{z}=\mathbf{x}-\mu&space;\right&space;)" title="=\frac{1}{\left ( 2\pi \right )^{D/2}}\frac{1}{\left | \Sigma \right |^{1/2}}\int \textup{exp}\left \{ -\frac{1}{2}\mathbf{z}^{T} \Sigma^{-1}\mathbf{z} \right \}\left (\mathbf{z}+\mathbf{\mu} \right ) d\mathbf{z} \begin{matrix} & \end{matrix}\left ( \textup{by } \mathbf{z}=\mathbf{x}-\mu \right )" />   
            
      
      > <img src="https://latex.codecogs.com/gif.latex?\int&space;\textup{exp}\left&space;\{&space;-\frac{1}{2}\mathbf{z}^{T}&space;\Sigma^{-1}\mathbf{z}&space;\right&space;\}\mathbf{z}&space;d\mathbf{z}=\int&space;\left&space;|\mathbf{J}&space;\right&space;|&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}\sum_{i=1}^{D}&space;\frac{y_{i}^{2}}{\lambda_{i}}&space;\right&space;\}\mathbf{y}d\mathbf{y}" title="\int \textup{exp}\left \{ -\frac{1}{2}\mathbf{z}^{T} \Sigma^{-1}\mathbf{z} \right \}\mathbf{z} d\mathbf{z}=\int \left |\mathbf{J} \right | \textup{exp} \left \{ -\frac{1}{2}\sum_{i=1}^{D} \frac{y_{i}^{2}}{\lambda_{i}} \right \}\mathbf{y}d\mathbf{y}" />  <img src="https://latex.codecogs.com/gif.latex?\left&space;(\textup{by&space;}\mathbf{z}=\sum_{j=1}^{D}y_{i}\mathbf{u}_{j},&space;y_{j}=\mathbf{u}_{j}^{T}\mathbf{z}&space;\right&space;)" title="\left (\textup{by }\mathbf{z}=\sum_{j=1}^{D}y_{i}\mathbf{u}_{j}, y_{j}=\mathbf{u}_{j}^{T}\mathbf{z} \right )" />   
            
      > <img src="https://latex.codecogs.com/gif.latex?=\begin{bmatrix}&space;\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\sum_{i=1}^{D}&space;\frac{y_{i}^{2}}{\lambda_{i}}&space;\right&space;\}y_{1}dy_{1},&space;...&space;,&space;dy_{D}&space;\\&space;\vdots&space;\\&space;\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\sum_{i=1}^{D}&space;\frac{y_{i}^{2}}{\lambda_{i}}&space;\right&space;\}y_{D}dy_{1},&space;...&space;,&space;dy_{D}&space;\end{bmatrix}" title="=\begin{bmatrix} \int \textup{exp} \left \{ -\frac{1}{2} \sum_{i=1}^{D} \frac{y_{i}^{2}}{\lambda_{i}} \right \}y_{1}dy_{1}, ... , dy_{D} \\ \vdots \\ \int \textup{exp} \left \{ -\frac{1}{2} \sum_{i=1}^{D} \frac{y_{i}^{2}}{\lambda_{i}} \right \}y_{D}dy_{1}, ... , dy_{D} \end{bmatrix}" />   
      
   
+
   
   
