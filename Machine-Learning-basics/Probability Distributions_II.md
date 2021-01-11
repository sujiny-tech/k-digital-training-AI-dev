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
            
         
      > z 부분에 대해 정리하면,
      
      > <img src="https://latex.codecogs.com/gif.latex?\int&space;\textup{exp}\left&space;\{&space;-\frac{1}{2}\mathbf{z}^{T}&space;\Sigma^{-1}\mathbf{z}&space;\right&space;\}\mathbf{z}&space;d\mathbf{z}=\int&space;\left&space;|\mathbf{J}&space;\right&space;|&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}\sum_{i=1}^{D}&space;\frac{y_{i}^{2}}{\lambda_{i}}&space;\right&space;\}\mathbf{y}d\mathbf{y}" title="\int \textup{exp}\left \{ -\frac{1}{2}\mathbf{z}^{T} \Sigma^{-1}\mathbf{z} \right \}\mathbf{z} d\mathbf{z}=\int \left |\mathbf{J} \right | \textup{exp} \left \{ -\frac{1}{2}\sum_{i=1}^{D} \frac{y_{i}^{2}}{\lambda_{i}} \right \}\mathbf{y}d\mathbf{y}" />  <img src="https://latex.codecogs.com/gif.latex?\left&space;(\textup{by&space;}\mathbf{z}=\sum_{j=1}^{D}y_{i}\mathbf{u}_{j},&space;y_{j}=\mathbf{u}_{j}^{T}\mathbf{z}&space;\right&space;)" title="\left (\textup{by }\mathbf{z}=\sum_{j=1}^{D}y_{i}\mathbf{u}_{j}, y_{j}=\mathbf{u}_{j}^{T}\mathbf{z} \right )" />   
            
      > <img src="https://latex.codecogs.com/gif.latex?=\begin{bmatrix}&space;\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\sum_{i=1}^{D}&space;\frac{y_{i}^{2}}{\lambda_{i}}&space;\right&space;\}y_{1}dy_{1},&space;...&space;,&space;dy_{D}&space;\\&space;\vdots&space;\\&space;\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\sum_{i=1}^{D}&space;\frac{y_{i}^{2}}{\lambda_{i}}&space;\right&space;\}y_{D}dy_{1},&space;...&space;,&space;dy_{D}&space;\end{bmatrix}=\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}\sum_{i=1}^{D}&space;\frac{y_{i}^{2}}{\lambda_{i}}&space;\right&space;\}y_{1}dy_{1},&space;...,&space;dy_{D}" title="=\begin{bmatrix} \int \textup{exp} \left \{ -\frac{1}{2} \sum_{i=1}^{D} \frac{y_{i}^{2}}{\lambda_{i}} \right \}y_{1}dy_{1}, ... , dy_{D} \\ \vdots \\ \int \textup{exp} \left \{ -\frac{1}{2} \sum_{i=1}^{D} \frac{y_{i}^{2}}{\lambda_{i}} \right \}y_{D}dy_{1}, ... , dy_{D} \end{bmatrix}=\int \textup{exp} \left \{ -\frac{1}{2}\sum_{i=1}^{D} \frac{y_{i}^{2}}{\lambda_{i}} \right \}y_{1}dy_{1}, ..., dy_{D}" />     
            
      > <img src="https://latex.codecogs.com/gif.latex?=\int\left&space;(&space;\int_{0}^{\infty&space;}&space;\textup{exp}\left&space;\{&space;-\frac{1}{2}\sum_{i=1}^{D}&space;\frac{y_{i}^{2}}{\lambda_{i}}&space;\right&space;\}y_{1}dy_{1}&plus;\int_{-\infty}^{0}&space;\textup{exp}\left&space;\{&space;-\frac{1}{2}\sum_{i=1}^{D}\frac{y_{i}^{2}}{\lambda_{i}}&space;\right&space;\}y_{1}dy_{1}&space;\right&space;)dy_{2}...dy_{D}" title="=\int\left ( \int_{0}^{\infty } \textup{exp}\left \{ -\frac{1}{2}\sum_{i=1}^{D} \frac{y_{i}^{2}}{\lambda_{i}} \right \}y_{1}dy_{1}+\int_{-\infty}^{0} \textup{exp}\left \{ -\frac{1}{2}\sum_{i=1}^{D}\frac{y_{i}^{2}}{\lambda_{i}} \right \}y_{1}dy_{1} \right )dy_{2}...dy_{D}" />    
      
      
      > <img src="https://latex.codecogs.com/gif.latex?=\int\left&space;(&space;\int_{0}^{\infty&space;}&space;\textup{exp}\left&space;\{&space;-\frac{1}{2}\sum_{i=1}^{D}&space;\frac{y_{i}^{2}}{\lambda_{i}}&space;\right&space;\}y_{1}dy_{1}&plus;\int_{0}^{\infty}&space;\textup{exp}\left&space;\{&space;-\frac{1}{2}\sum_{i=1}^{D}\frac{y_{i}^{2}}{\lambda_{i}}&space;\right&space;\}\left&space;(-y_{1}&space;\right&space;)dy_{1}&space;\right&space;)dy_{2}...dy_{D}" title="=\int\left ( \int_{0}^{\infty } \textup{exp}\left \{ -\frac{1}{2}\sum_{i=1}^{D} \frac{y_{i}^{2}}{\lambda_{i}} \right \}y_{1}dy_{1}+\int_{0}^{\infty} \textup{exp}\left \{ -\frac{1}{2}\sum_{i=1}^{D}\frac{y_{i}^{2}}{\lambda_{i}} \right \}\left (-y_{1} \right )dy_{1} \right )dy_{2}...dy_{D}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?=0" title="=0" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;E[\mathbf{x}]=\mathbf{\mu}" title="\therefore E[\mathbf{x}]=\mathbf{\mu}" /> (<img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />부분이 남기때문에)
      
      
   + 가우시안 분포의 공분산
   
      > 공분산을 구하기 위해 먼저 2차 적률(seconde order moments)를 구함
     
      > <img src="https://latex.codecogs.com/gif.latex?E[\mathbf{x}\mathbf{x}^{T}]=\frac{1}{\left&space;(&space;2\pi&space;\right&space;)^{D/2}}\frac{1}{\left&space;|&space;\Sigma&space;\right&space;|^{1/2}}\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}\left&space;(&space;\mathbf{x}-\mu&space;\right&space;)^{T}\Sigma^{-1}&space;\left&space;(\mathbf{x}-\mu&space;\right&space;)&space;\right&space;\}\mathbf{x}\mathbf{x}^{T}d\mathbf{x}" title="E[\mathbf{x}\mathbf{x}^{T}]=\frac{1}{\left ( 2\pi \right )^{D/2}}\frac{1}{\left | \Sigma \right |^{1/2}}\int \textup{exp} \left \{ -\frac{1}{2}\left ( \mathbf{x}-\mu \right )^{T}\Sigma^{-1} \left (\mathbf{x}-\mu \right ) \right \}\mathbf{x}\mathbf{x}^{T}d\mathbf{x}" />   
     
      > <img src="https://latex.codecogs.com/gif.latex?=\frac{1}{\left&space;(&space;2\pi&space;\right&space;)^{D/2}}\frac{1}{\left&space;|&space;\Sigma&space;\right&space;|^{1/2}}\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}\mathbf{z}^{T}\Sigma^{-1}&space;\mathbf{z}&space;\right&space;\}\left&space;(\mathbf{z}&plus;\mu&space;\right&space;)\left(\mathbf{z}&plus;\mu&space;\right&space;)^{T}d\mathbf{z}" title="=\frac{1}{\left ( 2\pi \right )^{D/2}}\frac{1}{\left | \Sigma \right |^{1/2}}\int \textup{exp} \left \{ -\frac{1}{2}\mathbf{z}^{T}\Sigma^{-1} \mathbf{z} \right \}\left (\mathbf{z}+\mu \right )\left(\mathbf{z}+\mu \right )^{T}d\mathbf{z}" />   
     
      > <img src="https://latex.codecogs.com/gif.latex?E[\mathbf{x}\mathbf{x}^{T}]" title="E[\mathbf{x}\mathbf{x}^{T}]" />는 DxD 행렬이므로 <img src="https://latex.codecogs.com/gif.latex?\mathbf{z}" title="\mathbf{z}" />를 <img src="https://latex.codecogs.com/gif.latex?U^{T}\mathbf{y}" title="U^{T}\mathbf{y}" />로 치환하면,
      
      > <img src="https://latex.codecogs.com/gif.latex?\frac{1}{\left&space;(&space;2\pi&space;\right&space;)^{D/2}}\frac{1}{\left&space;|&space;\Sigma&space;\right&space;|^{1/2}}\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}\mathbf{z}^{T}\Sigma^{-1}&space;\mathbf{z}&space;\right&space;\}\mathbf{z}\mathbf{z}^{T}d\mathbf{z}=\frac{1}{\left&space;(&space;2\pi&space;\right&space;)^{D/2}}\frac{1}{\left&space;|&space;\Sigma&space;\right&space;|^{1/2}}\sum_{i=1}^{D}\sum_{j=1}^{D}\mathbf{u}_{i}\mathbf{u}_{j}^{T}\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\sum_{k=1}^{D}&space;\frac{y_{k}^{2}}{\lambda_{k}}&space;\right&space;\}y_{i}y_{j}d\mathbf{y}" title="\frac{1}{\left ( 2\pi \right )^{D/2}}\frac{1}{\left | \Sigma \right |^{1/2}}\int \textup{exp} \left \{ -\frac{1}{2}\mathbf{z}^{T}\Sigma^{-1} \mathbf{z} \right \}\mathbf{z}\mathbf{z}^{T}d\mathbf{z}=\frac{1}{\left ( 2\pi \right )^{D/2}}\frac{1}{\left | \Sigma \right |^{1/2}}\sum_{i=1}^{D}\sum_{j=1}^{D}\mathbf{u}_{i}\mathbf{u}_{j}^{T}\int \textup{exp} \left \{ -\frac{1}{2} \sum_{k=1}^{D} \frac{y_{k}^{2}}{\lambda_{k}} \right \}y_{i}y_{j}d\mathbf{y}" />    
      
      > <img src="https://latex.codecogs.com/gif.latex?\because&space;\mathbf{z}=U^{T}\mathbf{y}=\begin{bmatrix}&space;\mid&space;&&space;\\&space;\mathbf{u_{1}}&space;&&space;...&space;\\&space;\mid&space;&&space;\end{bmatrix}\mathbf{y}=\sum&space;\mathbf{u}_{i}&space;y_{i}" title="\because \mathbf{z}=U^{T}\mathbf{y}=\begin{bmatrix} \mid & \\ \mathbf{u_{1}} & ... \\ \mid & \end{bmatrix}\mathbf{y}=\sum \mathbf{u}_{i} y_{i}" />   
      
      
      > <img src="https://latex.codecogs.com/gif.latex?\because&space;\mathbf{z}\mathbf{z}^{T}=\left&space;(&space;\sum&space;\mathbf{u}_{i}y_{i}&space;\right&space;)\left&space;(&space;\sum&space;\mathbf{u}_{j}^{T}&space;y_{j}&space;\right&space;)=\sum_{i}&space;\sum_{j}&space;\mathbf{u}_{i}\mathbf{u}_{j}^{T}y_{i}y_{j}" title="\because \mathbf{z}\mathbf{z}^{T}=\left ( \sum \mathbf{u}_{i}y_{i} \right )\left ( \sum \mathbf{u}_{j}^{T} y_{j} \right )=\sum_{i} \sum_{j} \mathbf{u}_{i}\mathbf{u}_{j}^{T}y_{i}y_{j}" />   
      
      
      > <img src="https://latex.codecogs.com/gif.latex?\because&space;\mathbf{z}\Sigma^{-1}\mathbf{z}^{T}&space;=\left&space;(\mathbf{U}^{T}\mathbf{y}&space;\right&space;)^{T}\Sigma^{-1}\left&space;(\mathbf{U}^{T}\mathbf{y}&space;\right&space;)=\mathbf{y}^{T}\mathbf{U}\mathbf{U}^{T}\lambda^{-1}\mathbf{U}\mathbf{U}^{T}\mathbf{y}" title="\because \mathbf{z}\Sigma^{-1}\mathbf{z}^{T} =\left (\mathbf{U}^{T}\mathbf{y} \right )^{T}\Sigma^{-1}\left (\mathbf{U}^{T}\mathbf{y} \right )=\mathbf{y}^{T}\mathbf{U}\mathbf{U}^{T}\lambda^{-1}\mathbf{U}\mathbf{U}^{T}\mathbf{y}" />    
      
      > <img src="https://latex.codecogs.com/gif.latex?=\mathbf{y}^{T}\lambda^{-1}\mathbf{y}&space;=\sum_{i=1}^{D}&space;\sum&space;_{j=1}^{D}\lambda^{-1}y_{i}y_{j}&space;=\sum_{i=1}^{D}\frac{1}{\lambda_{i}}y_{i}^{2}" title="=\mathbf{y}^{T}\lambda^{-1}\mathbf{y} =\sum_{i=1}^{D} \sum _{j=1}^{D}\lambda^{-1}y_{i}y_{j} =\sum_{i=1}^{D}\frac{1}{\lambda_{i}}y_{i}^{2}" />   
      
      + <img src="https://latex.codecogs.com/gif.latex?\frac{1}{\left&space;(&space;2\pi&space;\right&space;)^{D/2}}\frac{1}{\left&space;|&space;\Sigma&space;\right&space;|^{1/2}}\sum_{i=1}^{D}\sum_{j=1}^{D}\mathbf{u}_{i}\mathbf{u}_{j}^{T}\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\sum_{k=1}^{D}&space;\frac{y_{k}^{2}}{\lambda_{k}}&space;\right&space;\}y_{i}y_{j}d\mathbf{y}" title="\frac{1}{\left ( 2\pi \right )^{D/2}}\frac{1}{\left | \Sigma \right |^{1/2}}\sum_{i=1}^{D}\sum_{j=1}^{D}\mathbf{u}_{i}\mathbf{u}_{j}^{T}\int \textup{exp} \left \{ -\frac{1}{2} \sum_{k=1}^{D} \frac{y_{k}^{2}}{\lambda_{k}} \right \}y_{i}y_{j}d\mathbf{y}" />는 <img src="https://latex.codecogs.com/gif.latex?D^{2}" title="D^{2}" />개의 행렬 합이며 그 중 <img src="https://latex.codecogs.com/gif.latex?i\not\equiv&space;j" title="i\not\equiv j" />에 관해 영행렬이 됨.
      
         > <img src="https://latex.codecogs.com/gif.latex?\textup{for&space;}&space;i\not\equiv&space;j&space;,&space;\int&space;...&space;\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}\sum_{k=1}^{D}&space;\frac{y_{k}^{2}}{\lambda_{k}}&space;\right&space;\}y_{i}y_{j}d\mathbf{y}" title="\textup{for } i\not\equiv j , \int ... \int \textup{exp} \left \{ -\frac{1}{2}\sum_{k=1}^{D} \frac{y_{k}^{2}}{\lambda_{k}} \right \}y_{i}y_{j}d\mathbf{y}" />   
         
         
         > <img src="https://latex.codecogs.com/gif.latex?=\int&space;...&space;y_{j}\left&space;[&space;\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}\sum_{k=1}^{D}&space;\frac{y_{k}^{2}}{\lambda_{k}}y_{i}dy_{i}&space;\right&space;\}&space;\right&space;]d\mathbf{y}\setminus&space;\left&space;\{&space;y_{i}&space;\right&space;\}&space;=0" title="=\int ... y_{j}\left [ \int \textup{exp} \left \{ -\frac{1}{2}\sum_{k=1}^{D} \frac{y_{k}^{2}}{\lambda_{k}}y_{i}dy_{i} \right \} \right ]d\mathbf{y}\setminus \left \{ y_{i} \right \} =0" /> ( [ ]안의 식이 odd function이므로)
         
         > 따라서, 
         
         > <img src="https://latex.codecogs.com/gif.latex?\frac{1}{\left&space;(&space;2\pi&space;\right&space;)^{D/2}}\frac{1}{\left&space;|&space;\Sigma&space;\right&space;|^{1/2}}\sum_{i=1}^{D}\sum_{j=1}^{D}\mathbf{u}_{i}\mathbf{u}_{j}^{T}\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\sum_{k=1}^{D}&space;\frac{y_{k}^{2}}{\lambda_{k}}&space;\right&space;\}y_{i}y_{j}d\mathbf{y}" title="\frac{1}{\left ( 2\pi \right )^{D/2}}\frac{1}{\left | \Sigma \right |^{1/2}}\sum_{i=1}^{D}\sum_{j=1}^{D}\mathbf{u}_{i}\mathbf{u}_{j}^{T}\int \textup{exp} \left \{ -\frac{1}{2} \sum_{k=1}^{D} \frac{y_{k}^{2}}{\lambda_{k}} \right \}y_{i}y_{j}d\mathbf{y}" />   
                  
         > <img src="https://latex.codecogs.com/gif.latex?=\frac{1}{\left&space;(&space;2\pi&space;\right&space;)^{D/2}}\frac{1}{\left&space;|&space;\Sigma&space;\right&space;|^{1/2}}\sum_{i=1}^{D}\mathbf{u}_{i}\mathbf{u}_{i}^{T}\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\sum_{k=1}^{D}&space;\frac{y_{k}^{2}}{\lambda_{k}}&space;\right&space;\}y_{i}^{2}d\mathbf{y}" title="=\frac{1}{\left ( 2\pi \right )^{D/2}}\frac{1}{\left | \Sigma \right |^{1/2}}\sum_{i=1}^{D}\mathbf{u}_{i}\mathbf{u}_{i}^{T}\int \textup{exp} \left \{ -\frac{1}{2} \sum_{k=1}^{D} \frac{y_{k}^{2}}{\lambda_{k}} \right \}y_{i}^{2}d\mathbf{y}" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?=&space;\sum_{i=1}^{D}\mathbf{u}_{i}\mathbf{u}_{i}^{T}\left&space;[&space;\frac{1}{\left&space;(&space;2\pi&space;\right&space;)^{D/2}}\prod_{j=1}^{D}\frac{1}{\lambda_{j}^{1/2}}&space;\right&space;]\left&space;[&space;\prod_{k=\left&space;\{&space;1,...,D&space;\right&space;\}&space;\setminus&space;\left&space;\{&space;i&space;\right&space;\}}&space;\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\frac{y_{k}^{2}}{\lambda_{k}}&space;\right&space;\}dy_{k}&space;\right&space;]\left&space;[&space;\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\frac{y_{k}^{2}}{\lambda_{k}}&space;\right&space;\}y_{i}^{2}dy_{i}&space;\right&space;]" title="= \sum_{i=1}^{D}\mathbf{u}_{i}\mathbf{u}_{i}^{T}\left [ \frac{1}{\left ( 2\pi \right )^{D/2}}\prod_{j=1}^{D}\frac{1}{\lambda_{j}^{1/2}} \right ]\left [ \prod_{k=\left \{ 1,...,D \right \} \setminus \left \{ i \right \}} \int \textup{exp} \left \{ -\frac{1}{2} \frac{y_{k}^{2}}{\lambda_{k}} \right \}dy_{k} \right ]\left [ \int \textup{exp} \left \{ -\frac{1}{2} \frac{y_{k}^{2}}{\lambda_{k}} \right \}y_{i}^{2}dy_{i} \right ]" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?=\sum_{i=1}^{D}\mathbf{u}_{i}&space;\mathbf{u}_{i}^{T}\lambda_{i}=\Sigma" title="=\sum_{i=1}^{D}\mathbf{u}_{i} \mathbf{u}_{i}^{T}\lambda_{i}=\Sigma" />   
         
         
         > <img src="https://latex.codecogs.com/gif.latex?\because&space;\left&space;[&space;\frac{1}{\left&space;(&space;2\pi&space;\right&space;)^{D/2}}\prod_{j=1}^{D}\frac{1}{\lambda_{j}^{1/2}}&space;\right&space;]" title="\because \left [ \frac{1}{\left ( 2\pi \right )^{D/2}}\prod_{j=1}^{D}\frac{1}{\lambda_{j}^{1/2}} \right ]" /> : 상수부분   
               
         > <img src="https://latex.codecogs.com/gif.latex?\because&space;\left&space;[&space;\prod_{k=\left&space;\{&space;1,...,D&space;\right&space;\}&space;\setminus&space;\left&space;\{&space;i&space;\right&space;\}}&space;\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\frac{y_{k}^{2}}{\lambda_{k}}&space;\right&space;\}dy_{k}&space;\right&space;]=1" title="\because \left [ \prod_{k=\left \{ 1,...,D \right \} \setminus \left \{ i \right \}} \int \textup{exp} \left \{ -\frac{1}{2} \frac{y_{k}^{2}}{\lambda_{k}} \right \}dy_{k} \right ]=1" />   
         
         > <img src="https://latex.codecogs.com/gif.latex?\because&space;\left&space;[&space;\int&space;\textup{exp}&space;\left&space;\{&space;-\frac{1}{2}&space;\frac{y_{k}^{2}}{\lambda_{k}}&space;\right&space;\}y_{i}^{2}dy_{i}&space;\right&space;]=\lambda_{i}" title="\because \left [ \int \textup{exp} \left \{ -\frac{1}{2} \frac{y_{k}^{2}}{\lambda_{k}} \right \}y_{i}^{2}dy_{i} \right ]=\lambda_{i}" />   
         
         > 나머지 <img src="https://latex.codecogs.com/gif.latex?\mathbf{z}\mu^{T},&space;\mu\mathbf{z}^{T}" title="\mathbf{z}\mu^{T}, \mu\mathbf{z}^{T}" />부분에 관해서는 odd function의 성질로 사라지며, 마지막 <img src="https://latex.codecogs.com/gif.latex?\mu&space;\mu^{T}" title="\mu \mu^{T}" />은 별개의 부분으로 적분 앞으로 나옴.   
         
         
      + 따라서 정리하면, <img src="https://latex.codecogs.com/gif.latex?E[\mathbf{x}\mathbf{x}^{T}]=\mu\mu^{T}&space;&plus;\Sigma" title="E[\mathbf{x}\mathbf{x}^{T}]=\mu\mu^{T} +\Sigma" />임.
      
      + 확률변수의 벡터 x를 위한 공분산은 다음과 같음.
      
         > <img src="https://latex.codecogs.com/gif.latex?cov[\mathbf{x}]=E[\left&space;(&space;\mathbf{x}-E[\mathbf{x}]&space;\right&space;)\left&space;(&space;\mathbf{x}-E[\mathbf{x}]&space;\right&space;)^{T}]" title="cov[\mathbf{x}]=E[\left ( \mathbf{x}-E[\mathbf{x}] \right )\left ( \mathbf{x}-E[\mathbf{x}] \right )^{T}]" />   
         
         > 위에서 게산한 결과를 이용하면, <img src="https://latex.codecogs.com/gif.latex?cov[\mathbf{x}]=\Sigma" title="cov[\mathbf{x}]=\Sigma" /> ❗   
         
         
     
## 조건부 가우시안 분포(Conditional Gaussian Distribution)

+ D차원의 확률변수 벡터 x가 가우시안 분포 <img src="https://latex.codecogs.com/gif.latex?N(\mathbf{x}|\mu,&space;\Sigma)" title="N(\mathbf{x}|\mu, \Sigma)" />를 따른다고 하자. x를 두 그룹의 확률변수들로 나눴을때, 한 그룹이 주어졌을때 **나머지 그룹의 조건부 확률도 가우시안 분포를 따르며**, **각 그룹의 주변확률변수 또한 가우시안 분포를 따름**.
   
   >  <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}=\begin{bmatrix}&space;\mathbf{x}_{a}\\&space;\mathbf{x}_{b}&space;\end{bmatrix}" title="\mathbf{x}=\begin{bmatrix} \mathbf{x}_{a}\\ \mathbf{x}_{b} \end{bmatrix}" />   
   
   > + <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}_{a}" title="\mathbf{x}_{a}" /> : M개의 원소를 가짐.   
   
   
   > 평균벡터 : <img src="https://latex.codecogs.com/gif.latex?\mathbf{\mu}=\begin{bmatrix}&space;\mathbf{\mu}_{a}\\&space;\mathbf{\mu}_{b}&space;\end{bmatrix}" title="\mathbf{\mu}=\begin{bmatrix} \mathbf{\mu}_{a}\\ \mathbf{\mu}_{b} \end{bmatrix}" />   
   
   > 공분산 행렬 : <img src="https://latex.codecogs.com/gif.latex?\mathbf{\Sigma}=&space;\begin{bmatrix}&space;\mathbf{\Sigma}_{aa}&space;&&space;\mathbf{\Sigma}_{ab}&space;\\&space;\mathbf{\Sigma}_{ba}&space;&&space;\mathbf{\Sigma}_{bb}&space;\end{bmatrix}" title="\mathbf{\Sigma}= \begin{bmatrix} \mathbf{\Sigma}_{aa} & \mathbf{\Sigma}_{ab} \\ \mathbf{\Sigma}_{ba} & \mathbf{\Sigma}_{bb} \end{bmatrix}" />의 형태를 가진다고 하자.   
   
   
   > 공분산의 역행렬 : <img src="https://latex.codecogs.com/gif.latex?\Lambda&space;=\Sigma_{-1}" title="\Lambda =\Sigma_{-1}" />  ( 정확도 행렬(precision matrix)를 사용하는 것이 수식을 간편하게 함)  
   
   > <img src="https://latex.codecogs.com/gif.latex?\Lambda=\begin{bmatrix}&space;\Lambda_{aa}&space;&&space;\Lambda_{ab}\\&space;\Lambda_{ba}&space;&&space;\Lambda_{bb}&space;\end{bmatrix}&space;\left&space;(&space;\Lambda_{aa}\not\equiv&space;\Sigma^{-1}_{aa}&space;\right&space;)" title="\Lambda=\begin{bmatrix} \Lambda_{aa} & \Lambda_{ab}\\ \Lambda_{ba} & \Lambda_{bb} \end{bmatrix} \left ( \Lambda_{aa}\not\equiv \Sigma^{-1}_{aa} \right )" />   
  
   + 지수부의 이차형식을 파티션을 사용해서 전개하면 다음과 같다.
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{z}=\mathbf{z}^{T}\Lambda&space;\mathbf{z}=\mathbf{z}^{T}_{a}\Lambda_{aa}\mathbf{z}_{a}&plus;\mathbf{z}^{T}_{b}\Lambda_{ba}\mathbf{z}_{a}&plus;\mathbf{z}^{T}_{a}\Lambda_{ab}\mathbf{z}_{b}&plus;\mathbf{z}^{T}_{b}\Lambda_{bb}\mathbf{z}_{b}" title="\mathbf{z}=\mathbf{z}^{T}\Lambda \mathbf{z}=\mathbf{z}^{T}_{a}\Lambda_{aa}\mathbf{z}_{a}+\mathbf{z}^{T}_{b}\Lambda_{ba}\mathbf{z}_{a}+\mathbf{z}^{T}_{a}\Lambda_{ab}\mathbf{z}_{b}+\mathbf{z}^{T}_{b}\Lambda_{bb}\mathbf{z}_{b}" />   
      
      
   
+ **완전제곱식(Completing the Square) 방법** 
   + 변형해서 함수g(xa)를 찾는 것이 목표 ❗      
   
   
   > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x}_{a},&space;\mathbf{x}_{b})=g(\mathbf{x}_{a})\alpha" title="p(\mathbf{x}_{a}, \mathbf{x}_{b})=g(\mathbf{x}_{a})\alpha" />라 하며, 이때 이 함수의 적분이 1이고, α는 <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}_{a}" title="\mathbf{x}_{a}" />와 독립적임.
   
   > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;\int&space;p(\mathbf{x}_{a},&space;\mathbf{x}_{b})=\int&space;g(\mathbf{x}_{a})\alpha=&space;\alpha" title="\therefore \int p(\mathbf{x}_{a}, \mathbf{x}_{b})=\int g(\mathbf{x}_{a})\alpha= \alpha" />    
   
   > α는 <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}_{a}" title="\mathbf{x}_{a}" />에 관해 적분했으므로, <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}_{b}" title="\mathbf{x}_{b}" />의 주변확률.
   
   > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x}_{a},&space;\mathbf{x}_{b})=&space;g(\mathbf{x}_{a})p(\mathbf{x}_{b})" title="p(\mathbf{x}_{a}, \mathbf{x}_{b})= g(\mathbf{x}_{a})p(\mathbf{x}_{b})" />이므로, <img src="https://latex.codecogs.com/gif.latex?g(\mathbf{x}_{a})=p(\mathbf{x}_{a}|\mathbf{x}_{b})" title="g(\mathbf{x}_{a})=p(\mathbf{x}_{a}|\mathbf{x}_{b})" /> ❗
   
   > 즉, 함수 <img src="https://latex.codecogs.com/gif.latex?g(\mathbf{x}_{a})" title="g(\mathbf{x}_{a})" />를 찾는 것이 목표
   
   > 이때, 이차 형식을 완전제곱식 형식으로 변형하면, 
   
   > <img src="https://latex.codecogs.com/gif.latex?-\frac{1}{2}\mathbf{x}_{a}^{T}A\mathbf{x}_{a}&plus;x_{a}^{T}m" title="-\frac{1}{2}\mathbf{x}_{a}^{T}A\mathbf{x}_{a}+x_{a}^{T}m" />   
   
   
   > <img src="https://latex.codecogs.com/gif.latex?=\left&space;(-\frac{1}{2}\mathbf{x}_{a}^{T}A\mathbf{x}_{a}&plus;x_{a}^{T}m-\tau&space;\right&space;)&plus;\tau" title="=\left (-\frac{1}{2}\mathbf{x}_{a}^{T}A\mathbf{x}_{a}+x_{a}^{T}m-\tau \right )+\tau" />   
   > <img src="https://latex.codecogs.com/gif.latex?=-\frac{1}{2}\left&space;(\mathbf{x}_{a}-?&space;\right&space;)^{T}A&space;\left&space;(\mathbf{x}_{a}-?&space;\right&space;)&plus;\tau" title="=-\frac{1}{2}\left (\mathbf{x}_{a}-? \right )^{T}A \left (\mathbf{x}_{a}-? \right )+\tau" /> ❗   
   
   
   > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x}_{a},\mathbf{x}_{b})=a&space;\textup{&space;exp}\left&space;\{-\frac{1}{2}\left&space;(\mathbf{x}_{a}-?&space;\right&space;)^{T}\Lambda_{aa}&space;\left&space;(\mathbf{x}_{a}-?&space;\right&space;)&space;\right&space;\}\textup{exp}\left&space;\{&space;\tau&space;\right&space;\}=b&space;\textup{&space;exp}\left&space;\{-\frac{1}{2}\left&space;(\mathbf{x}_{a}-?&space;\right&space;)^{T}\Lambda_{aa}&space;\left&space;(\mathbf{x}_{a}-?&space;\right&space;)&space;\right&space;\}\frac{a}{b}\textup{exp}\left&space;\{&space;\tau&space;\right&space;\}" title="p(\mathbf{x}_{a},\mathbf{x}_{b})=a \textup{ exp}\left \{-\frac{1}{2}\left (\mathbf{x}_{a}-? \right )^{T}\Lambda_{aa} \left (\mathbf{x}_{a}-? \right ) \right \}\textup{exp}\left \{ \tau \right \}=b \textup{ exp}\left \{-\frac{1}{2}\left (\mathbf{x}_{a}-? \right )^{T}\Lambda_{aa} \left (\mathbf{x}_{a}-? \right ) \right \}\frac{a}{b}\textup{exp}\left \{ \tau \right \}" />   
      
   > 이때, b는 normalize하기 위한 상수   
   
   >  <img src="https://latex.codecogs.com/gif.latex?g(\mathbf{x}_{a})" title="g(\mathbf{x}_{a})" />에 해당하는 부분 : <img src="https://latex.codecogs.com/gif.latex?b&space;\textup{&space;exp}\left&space;\{-\frac{1}{2}\left&space;(\mathbf{x}_{a}-?&space;\right&space;)^{T}\Lambda_{aa}&space;\left&space;(\mathbf{x}_{a}-?&space;\right&space;)&space;\right&space;\}" title="b \textup{ exp}\left \{-\frac{1}{2}\left (\mathbf{x}_{a}-? \right )^{T}\Lambda_{aa} \left (\mathbf{x}_{a}-? \right ) \right \}" />   
      
   
   > α에 해당하는 부분 : <img src="https://latex.codecogs.com/gif.latex?\frac{a}{b}\textup{exp}\left&space;\{&space;\tau&space;\right&space;\}" title="\frac{a}{b}\textup{exp}\left \{ \tau \right \}" />     
   
+ 가우시안 분포의 지수부

   > <img src="https://latex.codecogs.com/gif.latex?-\frac{1}{2}\left&space;(&space;\mathbf{x}-\mu&space;\right&space;)^{T}\Sigma^{-1}\left&space;(&space;\mathbf{x}-\mu&space;\right&space;)=-\frac{1}{2}\left&space;(&space;\mathbf{x}^{T}\Sigma^{-1}\mathbf{x}-\mu^{T}\Sigma^{-1}\mathbf{x}-\mathbf{x}^{T}\Sigma^{-1}\mu&plus;\mu^{T}\Sigma^{-1}\mu&space;\right&space;)" title="-\frac{1}{2}\left ( \mathbf{x}-\mu \right )^{T}\Sigma^{-1}\left ( \mathbf{x}-\mu \right )=-\frac{1}{2}\left ( \mathbf{x}^{T}\Sigma^{-1}\mathbf{x}-\mu^{T}\Sigma^{-1}\mathbf{x}-\mathbf{x}^{T}\Sigma^{-1}\mu+\mu^{T}\Sigma^{-1}\mu \right )" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?=-\frac{1}{2}\mathbf{x}^{T}\Sigma^{-1}\mathbf{x}-\mathbf{x}^{T}\Sigma^{-1}\mu&plus;\textup{const}" title="=-\frac{1}{2}\mathbf{x}^{T}\Sigma^{-1}\mathbf{x}-\mathbf{x}^{T}\Sigma^{-1}\mu+\textup{const}" />   
   
   > 이때, 가운데 두 값은 transpose하면 같은 값이고, 마지막항은 x와 관계없으르모 상수 취급   
   
   > 이차항을 통해 공분산 행렬을 구하고, 이를 통해 일차항의 계수인 평균벡터 mu를 구할 수 있음 ❗   
   
+ 앞서 파티션한 부분에서 

   > <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}_{a}" title="\mathbf{x}_{a}" />의 이차항 : <img src="https://latex.codecogs.com/gif.latex?-\frac{1}{2}\mathbf{x}_{a}^{T}\Lambda_{aa}\mathbf{x}_{a}" title="-\frac{1}{2}\mathbf{x}_{a}^{T}\Lambda_{aa}\mathbf{x}_{a}" />   
   
   > 따라서 공분산 -> <img src="https://latex.codecogs.com/gif.latex?\Sigma_{a|b}=\Lambda_{aa}^{-1}" title="\Sigma_{a|b}=\Lambda_{aa}^{-1}" />   
   
   > 이를 통해 일차항을 정리해서 계수를 통해 평균벡터를 구하면,  
   > <img src="https://latex.codecogs.com/gif.latex?\mu_{a|b}=\Sigma_{a|b}\left&space;\{&space;\Lambda_{aa}\mu_{a}-\Lambda_{ab}\left&space;(&space;\mathbf{x}_{b}-\mu_{b}&space;\right&space;)&space;\right&space;\}=\mu_{a}-\Lambda_{aa}^{-1}\Lambda_{ab}\left&space;(&space;\mathbf{x}_{b}-\mu_{b}&space;\right&space;)" title="\mu_{a|b}=\Sigma_{a|b}\left \{ \Lambda_{aa}\mu_{a}-\Lambda_{ab}\left ( \mathbf{x}_{b}-\mu_{b} \right ) \right \}=\mu_{a}-\Lambda_{aa}^{-1}\Lambda_{ab}\left ( \mathbf{x}_{b}-\mu_{b} \right )" />   
   
   
## 주변 가우시안 분포(Marginal Gaussian Distributions)

+ 목표 ❗
   > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x}_{a})=\int&space;p(\mathbf{x}_{a},\mathbf{x}_{b})d\mathbf{x}_{b}" title="p(\mathbf{x}_{a})=\int p(\mathbf{x}_{a},\mathbf{x}_{b})d\mathbf{x}_{b}" />    

+ 전략

   > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x}_{a})=\int&space;p(\mathbf{x}_{a},\mathbf{x}_{b})d\mathbf{x}_{b}" title="p(\mathbf{x}_{a})=\int p(\mathbf{x}_{a},\mathbf{x}_{b})d\mathbf{x}_{b}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?=\int&space;\alpha&space;\textup{&space;exp&space;}\left&space;\{&space;-\frac{1}{2}\left&space;(&space;\mathbf{x}-\mu&space;\right&space;)^{T}\Sigma^{-1}\left&space;(&space;\mathbf{x}-\mu&space;\right&space;)&space;\right&space;\}&space;d\mathbf{x}_{b}" title="=\int \alpha \textup{ exp }\left \{ -\frac{1}{2}\left ( \mathbf{x}-\mu \right )^{T}\Sigma^{-1}\left ( \mathbf{x}-\mu \right ) \right \} d\mathbf{x}_{b}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?=\int&space;\alpha&space;\textup{&space;exp&space;}\left&space;\{&space;f(\mathbf{x}_{b},&space;\mathbf{x}_{a})&plus;g(\mathbf{x}_{a})&plus;\textup{const}&space;\right&space;\}&space;d\mathbf{x}_{b}" title="=\int \alpha \textup{ exp }\left \{ f(\mathbf{x}_{b}, \mathbf{x}_{a})+g(\mathbf{x}_{a})+\textup{const} \right \} d\mathbf{x}_{b}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?=\int&space;\alpha&space;\textup{&space;exp&space;}\left&space;\{&space;f(\mathbf{x}_{b},&space;\mathbf{x}_{a})-\tau&plus;\tau&plus;g(\mathbf{x}_{a})&plus;\textup{const}&space;\right&space;\}&space;d\mathbf{x}_{b}" title="=\int \alpha \textup{ exp }\left \{ f(\mathbf{x}_{b}, \mathbf{x}_{a})-\tau+\tau+g(\mathbf{x}_{a})+\textup{const} \right \} d\mathbf{x}_{b}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?=\int&space;\alpha&space;\textup{&space;exp&space;}\left&space;\{&space;f(\mathbf{x}_{b},&space;\mathbf{x}_{a})-\tau&space;\right&space;\}&space;\textup{exp&space;}\left&space;\{\tau&plus;g(\mathbf{x}_{a})&plus;\textup{const}&space;\right&space;\}&space;d\mathbf{x}_{b}" title="=\int \alpha \textup{ exp }\left \{ f(\mathbf{x}_{b}, \mathbf{x}_{a})-\tau \right \} \textup{exp }\left \{\tau+g(\mathbf{x}_{a})+\textup{const} \right \} d\mathbf{x}_{b}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?=\alpha&space;\textup{&space;exp&space;}\left&space;\{\tau&plus;g(\mathbf{x}_{a})&plus;\textup{const}&space;\right&space;\}&space;\int&space;\textup{exp&space;}\left&space;\{&space;f(\mathbf{x}_{b},&space;\mathbf{x}_{a})-\tau&space;\right&space;\}&space;d\mathbf{x}_{b}" title="=\alpha \textup{ exp }\left \{\tau+g(\mathbf{x}_{a})+\textup{const} \right \} \int \textup{exp }\left \{ f(\mathbf{x}_{b}, \mathbf{x}_{a})-\tau \right \} d\mathbf{x}_{b}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?=\alpha&space;\beta&space;\textup{&space;exp&space;}\left&space;\{\tau&plus;g(\mathbf{x}_{a})&plus;\textup{const}&space;\right&space;\}" title="=\alpha \beta \textup{ exp }\left \{\tau+g(\mathbf{x}_{a})+\textup{const} \right \}" />   
   
   > 이때, β는 <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}_{b}" title="\mathbf{x}_{b}" />에 관한 적분 값. 
   
   > 이를 완전제곱식으로 변형해서 이전의 방법처럼 공분산과 평균벡터 구할 수 있음 ❗   
   

+ 파티션을 위한 이차형식을 다시 살펴보면, 전체 16개 항 중  <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}_{b}" title="\mathbf{x}_{b}" />를 포함한 항은 7개이며 <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}_{a}" title="\mathbf{x}_{a}" />를 포함한 항은 5개   

   > 정리하면, 
   > <img src="https://latex.codecogs.com/gif.latex?f(\mathbf{x}_{b},&space;\mathbf{x}_{a})=-\frac{1}{2}\mathbf{x}_{b}^{T}\Lambda_{bb}\mathbf{x}_{b}&plus;\mathbf{x}_{b}^{T}\left&space;\{&space;\Lambda_{bb}\mu_{b}-\Lambda_{ba}\left&space;(&space;\mathbf{x}_{a}-\mu_{a}&space;\right&space;)&space;\right&space;\}" title="f(\mathbf{x}_{b}, \mathbf{x}_{a})=-\frac{1}{2}\mathbf{x}_{b}^{T}\Lambda_{bb}\mathbf{x}_{b}+\mathbf{x}_{b}^{T}\left \{ \Lambda_{bb}\mu_{b}-\Lambda_{ba}\left ( \mathbf{x}_{a}-\mu_{a} \right ) \right \}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?g(\mathbf{x}_{a})=-\frac{1}{2}\mathbf{x}_{a}^{T}\Lambda_{aa}\mathbf{x}_{a}&plus;\mathbf{x}_{a}^{T}\left&space;(&space;\Lambda_{aa}\mu_{a}&plus;\Lambda_{ab}\mu_{b}&space;\right&space;)" title="g(\mathbf{x}_{a})=-\frac{1}{2}\mathbf{x}_{a}^{T}\Lambda_{aa}\mathbf{x}_{a}+\mathbf{x}_{a}^{T}\left ( \Lambda_{aa}\mu_{a}+\Lambda_{ab}\mu_{b} \right )" />   
   
+ <img src="https://latex.codecogs.com/gif.latex?f(\mathbf{x}_{b},&space;\mathbf{x}_{a})" title="f(\mathbf{x}_{b}, \mathbf{x}_{a})" />를 완전제곱식 형태로 만들기

   > <img src="https://latex.codecogs.com/gif.latex?\mathbf{m}=\Lambda_{bb}\mu_{b}-\Lambda_{ba}\left&space;(&space;\mathbf{x}_{a}-\mu_{a}&space;\right&space;)" title="\mathbf{m}=\Lambda_{bb}\mu_{b}-\Lambda_{ba}\left ( \mathbf{x}_{a}-\mu_{a} \right )" /> 치환해서 <img src="https://latex.codecogs.com/gif.latex?\tau=\frac{1}{2}\mathbf{m}^{T}\Lambda_{bb}^{-1}\mathbf{m}" title="\tau=\frac{1}{2}\mathbf{m}^{T}\Lambda_{bb}^{-1}\mathbf{m}" />를 빼주고 더해주면 다음과 같이 변형됨.
   
   > <img src="https://latex.codecogs.com/gif.latex?\int&space;\textup{exp}\left&space;\{&space;f(\mathbf{x}_{b},&space;\mathbf{x}_{a})-\tau&space;\right&space;\}d\mathbf{x}_{b}=\int&space;\textup{exp}\left&space;\{&space;-\frac{1}{2}\left&space;(&space;\mathbf{x}_{b}-\Lambda_{bb}^{-1}\mathbf{m}&space;\right&space;)^{T}\Lambda_{bb}\left&space;(&space;\mathbf{x}_{b}-\Lambda_{bb}^{-1}\mathbf{m}&space;\right&space;)&space;\right&space;\}d\mathbf{x}_{b}" title="\int \textup{exp}\left \{ f(\mathbf{x}_{b}, \mathbf{x}_{a})-\tau \right \}d\mathbf{x}_{b}=\int \textup{exp}\left \{ -\frac{1}{2}\left ( \mathbf{x}_{b}-\Lambda_{bb}^{-1}\mathbf{m} \right )^{T}\Lambda_{bb}\left ( \mathbf{x}_{b}-\Lambda_{bb}^{-1}\mathbf{m} \right ) \right \}d\mathbf{x}_{b}" />   
   
   > 이는 공분산 <img src="https://latex.codecogs.com/gif.latex?\Lambda_{bb}" title="\Lambda_{bb}" />에만 종속되며, <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}_{a}" title="\mathbf{x}_{a}" />에는 독립이므로 앞서 설명한 <img src="https://latex.codecogs.com/gif.latex?\alpha&space;\beta&space;\textup{&space;exp&space;}\left&space;\{\tau&plus;g(\mathbf{x}_{a})&plus;\textup{const}&space;\right&space;\}" title="\alpha \beta \textup{ exp }\left \{\tau+g(\mathbf{x}_{a})+\textup{const} \right \}" />의 지수부에 집중하면 됨 ❗   
   
   
+ 따라서, <img src="https://latex.codecogs.com/gif.latex?\tau&plus;g(\mathbf{x}_{a})&plus;\textup{const}" title="\tau+g(\mathbf{x}_{a})+\textup{const}" />에 관해 정리하면,

   > <img src="https://latex.codecogs.com/gif.latex?\tau&plus;g(\mathbf{x}_{a})&plus;\textup{const}=\frac{1}{2}\mathbf{m}^{T}\Lambda_{bb}^{-1}\mathbf{m}-\frac{1}{2}\mathbf{x}_{a}^{T}\Lambda_{aa}\mathbf{x}_{a}&plus;\mathbf{x}_{a}^{T}\left&space;(&space;\Lambda_{aa}\mu_{a}&plus;\Lambda_{ab}\mu_{b}&space;\right&space;)&plus;\textup{const}" title="\tau+g(\mathbf{x}_{a})+\textup{const}=\frac{1}{2}\mathbf{m}^{T}\Lambda_{bb}^{-1}\mathbf{m}-\frac{1}{2}\mathbf{x}_{a}^{T}\Lambda_{aa}\mathbf{x}_{a}+\mathbf{x}_{a}^{T}\left ( \Lambda_{aa}\mu_{a}+\Lambda_{ab}\mu_{b} \right )+\textup{const}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?=-\frac{1}{2}\mathbf{x}_{a}^{T}\left&space;(&space;\Lambda_{aa}-\Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba}&space;\right&space;)\mathbf{x}_{a}&plus;\mathbf{x}_{a}^{T}\left&space;(&space;\Lambda_{aa}-\Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba}&space;\right&space;)\mu_{a}&plus;\textup{const}" title="=-\frac{1}{2}\mathbf{x}_{a}^{T}\left ( \Lambda_{aa}-\Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \right )\mathbf{x}_{a}+\mathbf{x}_{a}^{T}\left ( \Lambda_{aa}-\Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \right )\mu_{a}+\textup{const}" />   
      
   > <img src="https://latex.codecogs.com/gif.latex?\because&space;\mathbf{m}=\Lambda_{bb}\mu_{b}-\Lambda_{ba}\left&space;(&space;\mathbf{x}_{a}-\mu_{a}&space;\right&space;)" title="\because \mathbf{m}=\Lambda_{bb}\mu_{b}-\Lambda_{ba}\left ( \mathbf{x}_{a}-\mu_{a} \right )" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?\Sigma_{a}=\left&space;(\Lambda_{aa}-\Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba}&space;\right&space;)^{-1}" title="\Sigma_{a}=\left (\Lambda_{aa}-\Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \right )^{-1}" />   
      
   > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;\left&space;(\Lambda_{aa}-\Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba}&space;\right&space;)^{-1}=\Sigma_{aa}&space;\left&space;(&space;\textup{by&space;Schur&space;complement}&space;\right&space;)" title="\therefore \left (\Lambda_{aa}-\Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \right )^{-1}=\Sigma_{aa} \left ( \textup{by Schur complement} \right )" />   
      
   
   > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;\Sigma_{a}\left&space;(&space;\Lambda_{aa}-\Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba}&space;\right&space;)\mu_{a}=\mu_{a}" title="\therefore \Sigma_{a}\left ( \Lambda_{aa}-\Lambda_{ab}\Lambda_{bb}^{-1}\Lambda_{ba} \right )\mu_{a}=\mu_{a}" />   
   
   + <img src="https://latex.codecogs.com/gif.latex?E[\mathbf{x}_{a}]=\mu_{a}" title="E[\mathbf{x}_{a}]=\mu_{a}" />   
   
   + <img src="https://latex.codecogs.com/gif.latex?cov[\mathbf{x}_{a}]=\Sigma_{aa}" title="cov[\mathbf{x}_{a}]=\Sigma_{aa}" />  by Schur complement   
   
   

## 가우시안 분포를 위한 베이즈 정리(Bayes' Theorem for Gaussian Variables)

+ 주어진 값   

   + <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x})=N(\mathbf{x}|\mu,&space;\Lambda^{-1})" title="p(\mathbf{x})=N(\mathbf{x}|\mu, \Lambda^{-1})" />   
   
   + <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{y}|\mathbf{x})=N(\mathbf{y}|\Lambda&space;\mathbf{x}&plus;\mathbf{b},&space;L^{-1})" title="p(\mathbf{y}|\mathbf{x})=N(\mathbf{y}|\Lambda \mathbf{x}+\mathbf{b}, L^{-1})" />   
   
      + <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{y}|\mathbf{x})" title="p(\mathbf{y}|\mathbf{x})" />의 평균은 x의 선형함수   
      
      + <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{y}|\mathbf{x})" title="p(\mathbf{y}|\mathbf{x})" />의 공분산은 x와 독립   
      
+ 구할 값 : <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{y}),&space;p(\mathbf{x}|\mathbf{y})" title="p(\mathbf{y}), p(\mathbf{x}|\mathbf{y})" />   

+ <img src="https://latex.codecogs.com/gif.latex?\mathbf{z}=\begin{bmatrix}&space;\mathbf{x}\\&space;\mathbf{y}&space;\end{bmatrix}" title="\mathbf{z}=\begin{bmatrix} \mathbf{x}\\ \mathbf{y} \end{bmatrix}" />를 위한 결합확률분포 (이를 통해 공분산, 평균벡터 계산) 

   > <img src="https://latex.codecogs.com/gif.latex?\textup{ln&space;}p(\mathbf{z})=\textup{ln&space;}p(\mathbf{x})&plus;\textup{ln&space;}p(\mathbf{y}|\mathbf{x})" title="\textup{ln }p(\mathbf{z})=\textup{ln }p(\mathbf{x})+\textup{ln }p(\mathbf{y}|\mathbf{x})" />
   
   > <img src="https://latex.codecogs.com/gif.latex?=-\frac{1}{2}\left&space;(&space;\mathbf{x}-\mu&space;\right&space;)^{T}\Lambda&space;\left&space;(&space;\mathbf{x}-\mu&space;\right&space;)-\frac{1}{2}\left&space;(&space;\mathbf{y}-\mathbf{Ax}-\mathbf{b}&space;\right&space;)^{T}\mathbf{L}\left&space;(&space;\mathbf{y}-\mathbf{Ax}-\mathbf{b}&space;\right&space;)&plus;\textup{const}" title="=-\frac{1}{2}\left ( \mathbf{x}-\mu \right )^{T}\Lambda \left ( \mathbf{x}-\mu \right )-\frac{1}{2}\left ( \mathbf{y}-\mathbf{Ax}-\mathbf{b} \right )^{T}\mathbf{L}\left ( \mathbf{y}-\mathbf{Ax}-\mathbf{b} \right )+\textup{const}" />   
   
   + z의 이차항 정리 (공분산)
   
      > <img src="https://latex.codecogs.com/gif.latex?=-\frac{1}{2}\mathbf{x}^{T}\left&space;(&space;\Lambda&plus;\mathbf{A}^{T}\mathbf{LA}&space;\right&space;)\mathbf{x}-\frac{1}{2}\mathbf{y}^{T}\mathbf{Ly}&plus;\frac{1}{2}\mathbf{y}^{T}\mathbf{LAx}&plus;\frac{1}{2}\mathbf{x}^{T}\mathbf{A}^{T}\mathbf{Ly}" title="=-\frac{1}{2}\mathbf{x}^{T}\left ( \Lambda+\mathbf{A}^{T}\mathbf{LA} \right )\mathbf{x}-\frac{1}{2}\mathbf{y}^{T}\mathbf{Ly}+\frac{1}{2}\mathbf{y}^{T}\mathbf{LAx}+\frac{1}{2}\mathbf{x}^{T}\mathbf{A}^{T}\mathbf{Ly}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?=-\frac{1}{2}\begin{bmatrix}&space;\mathbf{x}\\&space;\mathbf{y}&space;\end{bmatrix}^{T}\begin{bmatrix}&space;\Lambda&plus;\mathbf{A}^{T}\mathbf{LA}&space;&&space;-\mathbf{A}^{T}\mathbf{L}&space;\\&space;-\mathbf{LA}&space;&&space;\mathbf{L}&space;\end{bmatrix}\begin{bmatrix}&space;\mathbf{x}\\&space;\mathbf{y}&space;\end{bmatrix}" title="=-\frac{1}{2}\begin{bmatrix} \mathbf{x}\\ \mathbf{y} \end{bmatrix}^{T}\begin{bmatrix} \Lambda+\mathbf{A}^{T}\mathbf{LA} & -\mathbf{A}^{T}\mathbf{L} \\ -\mathbf{LA} & \mathbf{L} \end{bmatrix}\begin{bmatrix} \mathbf{x}\\ \mathbf{y} \end{bmatrix}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?=-\frac{1}{2}\mathbf{z}^{T}\mathbf{R}\mathbf{z}" title="=-\frac{1}{2}\mathbf{z}^{T}\mathbf{R}\mathbf{z}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;cov[\mathbf{z}]=\mathbf{R}^{-1}=\begin{bmatrix}&space;\Lambda^{-1}&space;&&space;\Lambda^{-1}\mathbf{A}^{T}&space;\\&space;\mathbf{A}\Lambda^{-1}&space;&&space;\mathbf{L}^{-1}&plus;\mathbf{A}\Lambda^{-1}\mathbf{A}^{T}&space;\end{bmatrix}" title="\therefore cov[\mathbf{z}]=\mathbf{R}^{-1}=\begin{bmatrix} \Lambda^{-1} & \Lambda^{-1}\mathbf{A}^{T} \\ \mathbf{A}\Lambda^{-1} & \mathbf{L}^{-1}+\mathbf{A}\Lambda^{-1}\mathbf{A}^{T} \end{bmatrix}" />   
      
   + z의 이차항 정리 (평균벡터 -> 일차항)
   
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}^{T}\Lambda\mu-\mathbf{x}^{T}\mathbf{A}^{T}\mathbf{Lb}&plus;\mathbf{y}^{T}\mathbf{Lb}=\begin{bmatrix}&space;\mathbf{x}\\&space;\mathbf{y}&space;\end{bmatrix}^{T}&space;\begin{bmatrix}&space;\Lambda\mu-\mathbf{A}^{T}\mathbf{Lb}&space;\\&space;\mathbf{Lb}&space;\end{bmatrix}" title="\mathbf{x}^{T}\Lambda\mu-\mathbf{x}^{T}\mathbf{A}^{T}\mathbf{Lb}+\mathbf{y}^{T}\mathbf{Lb}=\begin{bmatrix} \mathbf{x}\\ \mathbf{y} \end{bmatrix}^{T} \begin{bmatrix} \Lambda\mu-\mathbf{A}^{T}\mathbf{Lb} \\ \mathbf{Lb} \end{bmatrix}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;E[\mathbf{z}]=\mathbf{R}^{-1}\begin{bmatrix}&space;\Lambda\mu-\mathbf{A}^{T}\mathbf{Lb}&space;\\&space;\mathbf{Lb}&space;\end{bmatrix}=\begin{bmatrix}&space;\mu&space;\\&space;\mathbf{A}\mu&plus;\mathbf{b}&space;\end{bmatrix}" title="\therefore E[\mathbf{z}]=\mathbf{R}^{-1}\begin{bmatrix} \Lambda\mu-\mathbf{A}^{T}\mathbf{Lb} \\ \mathbf{Lb} \end{bmatrix}=\begin{bmatrix} \mu \\ \mathbf{A}\mu+\mathbf{b} \end{bmatrix}" />   
      
   + **주변 가우시안 분포 결과** 를 적용하여 **y에 관한 주변확률분포의 평균과 공분산**은 다음과 같음.
   
      > <img src="https://latex.codecogs.com/gif.latex?E[\mathbf{y}]=\mathbf{A}\mu&plus;\mathbf{b}" title="E[\mathbf{y}]=\mathbf{A}\mu+\mathbf{b}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?cov[\mathbf{y}]=\mathbf{L}^{-1}&plus;\mathbf{A}\Lambda^{-1}\mathbf{A}^{T}" title="cov[\mathbf{y}]=\mathbf{L}^{-1}+\mathbf{A}\Lambda^{-1}\mathbf{A}^{T}" />   
      
   + **조건부 가우시안 분포 결과** 를 적용하여 **조건부 확률** <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x}|\mathbf{y})" title="p(\mathbf{x}|\mathbf{y})" />**의 평균과 공분산**은 다음과 같음.   
   
      > <img src="https://latex.codecogs.com/gif.latex?E[\mathbf{x}|\mathbf{y}]=\left&space;(&space;\Lambda&plus;\mathbf{A}^{T}\mathbf{LA}&space;\right&space;)^{-1}\left&space;\{&space;\mathbf{A}^{T}\mathbf{L}\left&space;(\mathbf{&space;y-b}&space;\right&space;)&plus;\Lambda\mu&space;\right&space;\}" title="E[\mathbf{x}|\mathbf{y}]=\left ( \Lambda+\mathbf{A}^{T}\mathbf{LA} \right )^{-1}\left \{ \mathbf{A}^{T}\mathbf{L}\left (\mathbf{ y-b} \right )+\Lambda\mu \right \}" />   
      > <img src="https://latex.codecogs.com/gif.latex?cov[\mathbf{x}|\mathbf{y}]=\left&space;(&space;\Lambda&plus;\mathbf{A}^{T}\mathbf{LA}&space;\right&space;)^{-1}" title="cov[\mathbf{x}|\mathbf{y}]=\left ( \Lambda+\mathbf{A}^{T}\mathbf{LA} \right )^{-1}" />   
      
      
- - - - - - - - - -       
## 가우시안 분포의 최대우도(Maximum Likelihood for the Gaussian)

+ 가우시안 분포에 의해 데이터 <img src="https://latex.codecogs.com/gif.latex?\mathbf{X}=\left&space;(&space;\mathbf{x}_{1},&space;...&space;,&space;\mathbf{x}_{n}&space;\right&space;)^{T}" title="\mathbf{X}=\left ( \mathbf{x}_{1}, ... , \mathbf{x}_{n} \right )^{T}" />가 주어졌을 때 **우도를 최대화하는 파라미터 값(평균, 공분산) 찾기** ❗   

   + 로그 우도 함수   
   
      > <img src="https://latex.codecogs.com/gif.latex?\textup{ln}&space;p(\mathbf{X}|\mu,&space;\Sigma)=-\frac{ND}{2}\textup{ln}\left&space;(&space;2\pi&space;\right&space;)-\frac{N}{2}\textup{ln}\left&space;|&space;\Sigma&space;\right&space;|-\frac{1}{2}\sum_{n=1}^{N}\left&space;(&space;\mathbf{x}_{n}-\mu&space;\right&space;)^{T}\Sigma^{-1}\left&space;(&space;\mathbf{x}_{n}-\mu&space;\right&space;)" title="\textup{ln} p(\mathbf{X}|\mu, \Sigma)=-\frac{ND}{2}\textup{ln}\left ( 2\pi \right )-\frac{N}{2}\textup{ln}\left | \Sigma \right |-\frac{1}{2}\sum_{n=1}^{N}\left ( \mathbf{x}_{n}-\mu \right )^{T}\Sigma^{-1}\left ( \mathbf{x}_{n}-\mu \right )" />   
      
   + 우도를 최대화하는 평균벡터 <img src="https://latex.codecogs.com/gif.latex?\mu_{ML}" title="\mu_{ML}" />   
   
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{y}=\left&space;(&space;\mathbf{x}-\mu&space;\right&space;)" title="\mathbf{y}=\left ( \mathbf{x}-\mu \right )" /> 치환   
      
      > <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;\mu}\left&space;(&space;\mathbf{x}-\mu&space;\right&space;)^{T}\Sigma^{-1}\left&space;(&space;\mathbf{x}-\mu&space;\right&space;)=\frac{\partial&space;}{\partial&space;y}\mathbf{y}^{T}\Sigma&space;\mathbf{y}\frac{\partial&space;\mathbf{y}}{\partial&space;\mu}=-2\Sigma^{-1}\mathbf{y}\equiv&space;-2\Lambda&space;\mathbf{y}" title="\frac{\partial }{\partial \mu}\left ( \mathbf{x}-\mu \right )^{T}\Sigma^{-1}\left ( \mathbf{x}-\mu \right )=\frac{\partial }{\partial y}\mathbf{y}^{T}\Sigma \mathbf{y}\frac{\partial \mathbf{y}}{\partial \mu}=-2\Sigma^{-1}\mathbf{y}\equiv -2\Lambda \mathbf{y}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;\mu}\textup{ln&space;}&space;p(\mathbf{X}|\mu,&space;\Sigma)=-\frac{1}{2}\sum_{i=1}^{N}-2\Lambda&space;\left&space;(&space;\mathbf{x}_{i}-\mu&space;\right&space;)=\Lambda\sum_{i=1}^{N}\left&space;(&space;\mathbf{x}_{i}-\mu&space;\right&space;)=0" title="\frac{\partial }{\partial \mu}\textup{ln } p(\mathbf{X}|\mu, \Sigma)=-\frac{1}{2}\sum_{i=1}^{N}-2\Lambda \left ( \mathbf{x}_{i}-\mu \right )=\Lambda\sum_{i=1}^{N}\left ( \mathbf{x}_{i}-\mu \right )=0" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;\mu_{ML}=\frac{1}N{}\sum_{i=1}^{N}\mathbf{x}_{i}=\bar{\mathbf{x}}" title="\therefore \mu_{ML}=\frac{1}N{}\sum_{i=1}^{N}\mathbf{x}_{i}=\bar{\mathbf{x}}" />   
      
   + 우도를 최대화하는 공분산 행렬 <img src="https://latex.codecogs.com/gif.latex?\Sigma_{ML}" title="\Sigma_{ML}" />   
   
      > <img src="https://latex.codecogs.com/gif.latex?l(\Lambda)=\frac{N}{2}\textup{ln&space;}|\Lambda|&space;-\frac{1}{2}\sum_{n=1}^{N}tr\left&space;(&space;\left&space;(&space;\mathbf{x}_{n}-\mu&space;\right&space;)\left&space;(&space;\mathbf{x}_{n}-\mu&space;\right&space;)^{T}&space;\Lambda&space;\right&space;)&space;=\frac{N}{2}\textup{ln&space;}|\Lambda|-\frac{1}{2}tr(\mathbf{S}\Lambda)" title="l(\Lambda)=\frac{N}{2}\textup{ln }|\Lambda| -\frac{1}{2}\sum_{n=1}^{N}tr\left ( \left ( \mathbf{x}_{n}-\mu \right )\left ( \mathbf{x}_{n}-\mu \right )^{T} \Lambda \right ) =\frac{N}{2}\textup{ln }|\Lambda|-\frac{1}{2}tr(\mathbf{S}\Lambda)" />   
            
      > <img src="https://latex.codecogs.com/gif.latex?\because&space;\mathbf{x}^{T}\mathbf{Ax}=\textup{tr}\left&space;(&space;\mathbf{x}^{T}\mathbf{Ax}&space;\right&space;)=\left&space;(&space;\mathbf{xx}^{T}\mathbf{A}&space;\right&space;)" title="\because \mathbf{x}^{T}\mathbf{Ax}=\textup{tr}\left ( \mathbf{x}^{T}\mathbf{Ax} \right )=\left ( \mathbf{xx}^{T}\mathbf{A} \right )" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\because&space;\textup{tr}(A)&plus;\textup{tr}(B)=\textup{tr}(A&plus;B)" title="\because \textup{tr}(A)+\textup{tr}(B)=\textup{tr}(A+B)" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{S}=\sum_{n=1}^{N}\left&space;(&space;\mathbf{x}_{n}-\mu&space;\right&space;)\left&space;(&space;\mathbf{x}_{n}-\mu&space;\right&space;)^{T}" title="\mathbf{S}=\sum_{n=1}^{N}\left ( \mathbf{x}_{n}-\mu \right )\left ( \mathbf{x}_{n}-\mu \right )^{T}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;l(\Lambda)}{\partial&space;\Lambda}=\frac{N}{2}\left&space;(&space;\Lambda^{-1}&space;\right&space;)^{T}-\frac{1}{2}\mathbf{S}^{T}=0" title="\frac{\partial l(\Lambda)}{\partial \Lambda}=\frac{N}{2}\left ( \Lambda^{-1} \right )^{T}-\frac{1}{2}\mathbf{S}^{T}=0" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\because&space;\frac{\partial&space;}{\partial&space;\mathbf{A}}&space;\textup{ln}\left&space;|&space;\mathbf{A}&space;\right&space;|=\left&space;(\mathbf{A}^{-1}&space;\right&space;)^{T}" title="\because \frac{\partial }{\partial \mathbf{A}} \textup{ln}\left | \mathbf{A} \right |=\left (\mathbf{A}^{-1} \right )^{T}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\because&space;\frac{\partial&space;}{\partial&space;\mathbf{A}}&space;tr(\mathbf{BA})=\mathbf{B}^{T}" title="\because \frac{\partial }{\partial \mathbf{A}} tr(\mathbf{BA})=\mathbf{B}^{T}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;\Lambda_{ML}&space;\right&space;)^{-1}=\Sigma_{ML}=\frac{1}{N}S" title="\left ( \Lambda_{ML} \right )^{-1}=\Sigma_{ML}=\frac{1}{N}S" />
      
      > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;\Sigma_{ML}=\frac{1}{N}\sum_{n=1}^{N}\left&space;(&space;\mathbf{x}_{n}-\mu&space;\right&space;)\left&space;(&space;\mathbf{x}_{n}-\mu&space;\right&space;)^{T}" title="\therefore \Sigma_{ML}=\frac{1}{N}\sum_{n=1}^{N}\left ( \mathbf{x}_{n}-\mu \right )\left ( \mathbf{x}_{n}-\mu \right )^{T}" />   
      
      
      + <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;\Lambda_{ML}&space;\right&space;)^{-1}=\Sigma_{ML}" title="\left ( \Lambda_{ML} \right )^{-1}=\Sigma_{ML}" /> 이해하기   
      
         + 역행렬 연산이 일대일함수를 정의하기 때문에, 성립함 ❗   
         
         
## 가우시안 분포를 위한 베이지안 추론(Bayesian Inference for the Gaussian)

+ MLE방법은 파라미터들<img src="https://latex.codecogs.com/gif.latex?\left&space;(\mu,&space;\Sigma&space;\right&space;)" title="\left (\mu, \Sigma \right )" />의 하나의 값만 구했다면, 파라미터의 확률분포 자체를 구할 수 있음 ❗   

+ 우도함수 <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{X}|\mu)" title="p(\mathbf{X}|\mu)" />와 사전확률 <img src="https://latex.codecogs.com/gif.latex?p(\mu)" title="p(\mu)" />를 통해 <img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />의 사후확률 <img src="https://latex.codecogs.com/gif.latex?p(\mu|\mathbf{X})" title="p(\mu|\mathbf{X})" /> 구하기 ❗
   
   + 분산은 주어졌다고 가정, 단변량 가우시간 확률변수 x의 μ를 베이지안 추론을 통해 구한다.   
   
   + **우도함수** 
   
      > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x}|\mu)=\prod_{n=1}^{N}p(x_{n}|\mu)=\frac{1}{\left&space;(&space;2\pi\sigma^{2}&space;\right&space;)^{N/2}}&space;\textup{exp}\left&space;\{-\frac{1}{2\sigma^{2}}\sum_{n=1}^{N}&space;\left&space;(&space;x_{n}-\mu&space;\right&space;)^{2}&space;\right&space;\}" title="p(\mathbf{x}|\mu)=\prod_{n=1}^{N}p(x_{n}|\mu)=\frac{1}{\left ( 2\pi\sigma^{2} \right )^{N/2}} \textup{exp}\left \{-\frac{1}{2\sigma^{2}}\sum_{n=1}^{N} \left ( x_{n}-\mu \right )^{2} \right \}" />   
      
   + **사전확률**
   
      > <img src="https://latex.codecogs.com/gif.latex?p(\mu)=N(\mu|\mu_{0},&space;\sigma_{0}^{2})" title="p(\mu)=N(\mu|\mu_{0}, \sigma_{0}^{2})" />   
      
   + **사후확률**
   
      > <img src="https://latex.codecogs.com/gif.latex?p(\mu|\mathbf{x})=N(\mu|\mu_{N},&space;\sigma_{N}^{2})" title="p(\mu|\mathbf{x})=N(\mu|\mu_{N}, \sigma_{N}^{2})" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\mu_{N}=\frac{\sigma^{2}}{N\sigma^{2}_{0}&plus;\sigma^{2}}\mu_{0}&plus;\frac{N\sigma^{2}_{0}}{N\sigma^{2}_{0}&plus;\sigma^{2}}\mu_{ML}" title="\mu_{N}=\frac{\sigma^{2}}{N\sigma^{2}_{0}+\sigma^{2}}\mu_{0}+\frac{N\sigma^{2}_{0}}{N\sigma^{2}_{0}+\sigma^{2}}\mu_{ML}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\frac{1}{\sigma^{2}_{N}}=\frac{1}{\sigma^{2}_{0}}&plus;\frac{N}{\sigma^{2}}" title="\frac{1}{\sigma^{2}_{N}}=\frac{1}{\sigma^{2}_{0}}+\frac{N}{\sigma^{2}}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\mu_{ML}=\frac{1}{N}\sum_{n=1}^{N}\mathbf{x}_{n}" title="\mu_{ML}=\frac{1}{N}\sum_{n=1}^{N}\mathbf{x}_{n}" />   
      
      > 앞에서 사용했던 완전제곱식 방법을 통해 보일 수 있음 ❗   
      
      
