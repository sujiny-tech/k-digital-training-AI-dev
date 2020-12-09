# 특이값 분해(SVD, Singular Value Decomposition)
+ 이전에 공부했던 LU 분해와 QR 분해는 m x n 정방행렬에 대한 행렬분해
+ 특이값 분해는 **일반적인 m x n 행렬** 에 관한 행렬 분해
+ 직교분할, 확대축소, 차원변환 등과 관련있음

+ 주어진 행렬 <img src="https://latex.codecogs.com/gif.latex?A_{m\times&space;n}" title="A_{m\times n}" />을 세 행렬의 곱으로 나누는 행렬 분해 : <img src="https://latex.codecogs.com/gif.latex?A=UDV^{T}" title="A=UDV^{T}" />   
   + 행렬 <img src="https://latex.codecogs.com/gif.latex?U_{m\times&space;n}" title="U_{m\times n}" /> : m차원 회전행렬 (정규직교행렬)
   + 행렬 <img src="https://latex.codecogs.com/gif.latex?D_{m\times&space;n}" title="D_{m\times n}" /> : n차원 확대축소 (확대축소 크기에 따른 정렬 형태) - eigenvalue
   + 행렬 <img src="https://latex.codecogs.com/gif.latex?V_{n\times&space;n}^{T}" title="V_{n\times n}^{T}" /> : n차원 회전행렬 (정규직교행렬)   
   
   + 특이값 분해는 행렬을 회전과 확대축소로 분해하는 방법   

     <img src="https://user-images.githubusercontent.com/72974863/101590090-1da19480-3a2d-11eb-9838-2c02919f2032.png" width="70%" height="70%">   

### 특이값 분해의 활용
   + 행렬 A의 특이값 분해는 각각 열벡터의 순서대로 행렬 A의 열벡터가 **어떤 방향으로 강한 응집성을 보이고 있는가** 를 분석 
   + 강한 응집성을 갖는 p개의 방향으로 수선의 발을 내린 A의 근사치 A'를 재구성할 수 있음.
   + 위의 그림에서 강한 응집성을 갖는 <img src="https://latex.codecogs.com/gif.latex?D'_{1\times&space;1}" title="D'_{1\times 1}" />를 취한다면,   
   
      <img src="https://latex.codecogs.com/gif.latex?U'_{3\times&space;1}&space;D'_{1\times&space;1}&space;{V'}^{T}_{1\times&space;2}=A'_{3\times&space;2}\Rightarrow&space;\begin{bmatrix}&space;\frac{1}{\sqrt{2}}\\&space;0\\&space;\frac{-1}{\sqrt{2}}&space;\end{bmatrix}&space;\begin{bmatrix}&space;4&space;\end{bmatrix}&space;\begin{bmatrix}&space;\frac{1}{\sqrt{2}}&space;&&space;\frac{1}{\sqrt{2}}&space;\end{bmatrix}=\begin{bmatrix}&space;2&space;&&space;2\\&space;0&space;&&space;0\\&space;-2&space;&&space;-2&space;\end{bmatrix}" title="U'_{3\times 1} D'_{1\times 1} {V'}^{T}_{1\times 2}=A'_{3\times 2}\Rightarrow \begin{bmatrix} \frac{1}{\sqrt{2}}\\ 0\\ \frac{-1}{\sqrt{2}} \end{bmatrix} \begin{bmatrix} 4 \end{bmatrix} \begin{bmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \end{bmatrix}=\begin{bmatrix} 2 & 2\\ 0 & 0\\ -2 & -2 \end{bmatrix}" />   
    
   + 근사치 행렬 A'는 행렬 A의 중간 부분이 날라간 것을 볼 수 있음 (응집성이 낮은 부분이므로...)   
   
   + **근사치 A'에 대한 기하적인 해석** 은 아래 그림과 같음   
   
     <img src="https://user-images.githubusercontent.com/72974863/101591789-99e9a700-3a30-11eb-9720-761e85e48398.png" width="60%" height="60%">   
   
   + #### 영상 처리에서 많이 쓰이는 분석이며, 데이터의 응집성이 높은 방향만 선택적으로 추출하는 방법 ❗❗
   
- - - - - - - - - - - - - - - -
# 주성분 분석(PCA, Principal Component Analysis)
+ 다수의 n차원 데이터에 대해, **데이터의 중심** 으로부터 **데이터의 응집력이 좋은 n개의 직교방향** 을 분석하는 방법
+ 데이터의 공분산행렬(covariance matrix)에 대한 **고유값 분해** 에 기반을 둔 **직교분해** 
+ K개의 n차원 데이터 <img src="https://latex.codecogs.com/gif.latex?^{\left&space;\{&space;x_{i}&space;\right&space;\}_{i=1}^{K}}" title="^{\left \{ x_{i} \right \}_{i=1}^{K}}" />가 있을때,   

   + <img src="https://latex.codecogs.com/gif.latex?\mathbf{m}=\frac{1}{K}\sum_{i=1}^{K}\mathbf{x}_{i}" title="\mathbf{m}=\frac{1}{K}\sum_{i=1}^{K}\mathbf{x}_{i}" /> : **데이터의 중심 m**    
   
   + <img src="https://latex.codecogs.com/gif.latex?C=\frac{1}{K}\sum_{i=1}^{K}\left&space;(&space;\mathbf{x}_{i}-\mathbf{m}&space;\right&space;)\left&space;(&space;\mathbf{x}_{i}-\mathbf{m}&space;\right&space;)^{T}" title="C=\frac{1}{K}\sum_{i=1}^{K}\left ( \mathbf{x}_{i}-\mathbf{m} \right )\left ( \mathbf{x}_{i}-\mathbf{m} \right )^{T}" /> : **공분산행렬 C**    
   
+ 공분산행렬 C에 대한 주성분분석 : <img src="https://latex.codecogs.com/gif.latex?C_{n\times&space;n}=W_{n\times&space;n}&space;D_{n\times&space;n}&space;W_{n\times&space;n}^{T}" title="C_{n\times n}=W_{n\times n} D_{n\times n} W_{n\times n}^{T}" />   
   + 행렬 <img src="https://latex.codecogs.com/gif.latex?W_{n\times&space;n}" title="W_{n\times n}" /> : n차원 회전행렬 (정규직교행렬)   
   + 행렬 <img src="https://latex.codecogs.com/gif.latex?D_{n\times&space;n}" title="D_{n\times n}" /> : n차원 확대축소 (확대축소 크기에 따른 정렬 형태)   
   
   
+ 주성분분석의 활용   
   + 예 ) 아래 그림과 같이 데이터가 6개 주어진다면, 이에 대한 공분산행렬과 주성분분석은 다음과 같다.   
   
       <img src="https://user-images.githubusercontent.com/72974863/101594910-cd7b0000-3a35-11eb-996c-51e3592c5803.png" width="40%" height="40%">   
       
       <img src="https://latex.codecogs.com/gif.latex?C=\frac{1}{K}\sum_{i=1}^{K}\left&space;(&space;\mathbf{x}_{i}-\mathbf{m}&space;\right&space;)\left&space;(&space;\mathbf{x}_{i}-\mathbf{m}&space;\right&space;)^{T}" title="C=\frac{1}{K}\sum_{i=1}^{K}\left ( \mathbf{x}_{i}-\mathbf{m} \right )\left ( \mathbf{x}_{i}-\mathbf{m} \right )^{T}" />이므로, <img src="https://latex.codecogs.com/gif.latex?C=\frac{1}{6}\begin{bmatrix}&space;28&space;&&space;18&space;\\&space;18&space;&&space;12&space;\end{bmatrix}" title="C=\frac{1}{6}\begin{bmatrix} 28 & 18 \\ 18 & 12 \end{bmatrix}" />.   
      
       이에 대한 주성분분석은 아래와 같음   
      
       <img src="https://latex.codecogs.com/gif.latex?C=\frac{1}{6}\begin{bmatrix}&space;28&space;&&space;18&space;\\&space;18&space;&&space;12&space;\end{bmatrix}\approx&space;\begin{bmatrix}&space;-0.84&space;&&space;0.55\\&space;-0.55&space;&&space;-0.84&space;\end{bmatrix}&space;\begin{bmatrix}&space;6.3&space;&&space;\\&space;&&space;0.55&space;\end{bmatrix}\begin{bmatrix}&space;-0.84&space;&&space;-0.55\\&space;0.55&space;&&space;-0.84&space;\end{bmatrix}" title="C=\frac{1}{6}\begin{bmatrix} 28 & 18 \\ 18 & 12 \end{bmatrix}\approx \begin{bmatrix} -0.84 & 0.55\\ -0.55 & -0.84 \end{bmatrix} \begin{bmatrix} 6.3 & \\ & 0.55 \end{bmatrix}\begin{bmatrix} -0.84 & -0.55\\ 0.55 & -0.84 \end{bmatrix}" />   
         
      + 행렬 D에서 6.3에 해당하는 방향에 대해 남기고 나머지는 없애도 데이터를 표현하는데에 있어서 받아들일 수 있는 오차정도라면 이런식으로 차원 축소를 함.   
      
