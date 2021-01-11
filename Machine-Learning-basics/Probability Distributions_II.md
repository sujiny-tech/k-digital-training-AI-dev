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
      
      


+
