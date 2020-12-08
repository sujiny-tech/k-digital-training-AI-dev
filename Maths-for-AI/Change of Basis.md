# 좌표계 변환(Change of Basis)
+ #### 좌표계 :: 좌표값 = 행렬 :: 벡터

+ 벡터는 크기와 방향을 가지는 물리량
   + 물리적 표현(좌표계가 없는) : 화살표의 길이(벡터의 크기), 방향(벡터 방향)
   + 수학적 표현(좌표계가 있는) : **좌표계** 를 도입한 후, 화살표 길이(벡터의 크기), 방향(벡터 방향)
      
## 좌표계(Coordinate System)
+ 2-벡터 <img src="https://latex.codecogs.com/gif.latex?\mathbf{v}" title="\mathbf{v}" />가 주어졌다고 할 때, 이 벡터는 xy-평면 상에서 원점에서 (a,b)에서 끝나는 벡터를 의미   

  <img src="https://latex.codecogs.com/gif.latex?\mathbf{v}=\begin{bmatrix}&space;a\\&space;b&space;\end{bmatrix}=\begin{bmatrix}&space;1&space;&&space;0&space;\\&space;0&space;&&space;1&space;\end{bmatrix}\begin{bmatrix}&space;a\\&space;b&space;\end{bmatrix}&space;=a\begin{bmatrix}&space;1\\&space;0&space;\end{bmatrix}&plus;b\begin{bmatrix}&space;0\\&space;1&space;\end{bmatrix}" title="\mathbf{v}=\begin{bmatrix} a\\ b \end{bmatrix}=\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}\begin{bmatrix} a\\ b \end{bmatrix} =a\begin{bmatrix} 1\\ 0 \end{bmatrix}+b\begin{bmatrix} 0\\ 1 \end{bmatrix}" />    
  
  + x-축으로 내린 수선의 발, (x-축 단위로 a번 전진) => <img src="https://latex.codecogs.com/gif.latex?a\begin{bmatrix}&space;1\\&space;0&space;\end{bmatrix}" title="a\begin{bmatrix} 1\\ 0 \end{bmatrix}" />  
  
  + y-축으로 내린 수선의 발, (y-축 단위로 b번 전진) => <img src="https://latex.codecogs.com/gif.latex?b\begin{bmatrix}&space;0\\&space;1&space;\end{bmatrix}" title="b\begin{bmatrix} 0\\ 1 \end{bmatrix}" />   
  
  
+ 두 벡터 <img src="https://latex.codecogs.com/gif.latex?v_{1}" title="v_{1}" />, <img src="https://latex.codecogs.com/gif.latex?v_{2}" title="v_{2}" />를 이용해 새로운 좌표 <img src="https://latex.codecogs.com/gif.latex?\mathbf{v}" title="\mathbf{v}" />는?
  + ex) <img src="https://latex.codecogs.com/gif.latex?4\mathbf{v}_{1}&plus;3\mathbf{v}_{2}=\mathbf{v}" title="4\mathbf{v}_{1}+3\mathbf{v}_{2}=\mathbf{v}" /> => 따라서, <img src="https://latex.codecogs.com/gif.latex?\mathbf{v}=(4,3)" title="\mathbf{v}=(4,3)" />   
  
  + <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;\mathbf{v}_{1}&space;&&space;\mathbf{v}_{2}&space;\end{bmatrix}\begin{bmatrix}&space;4\\&space;3&space;\end{bmatrix}=\begin{bmatrix}&space;\mathbf{v}&space;\end{bmatrix}\left&space;(=&space;\begin{bmatrix}&space;a\\&space;b&space;\end{bmatrix}&space;\right&space;)" title="\begin{bmatrix} \mathbf{v}_{1} & \mathbf{v}_{2} \end{bmatrix}\begin{bmatrix} 4\\ 3 \end{bmatrix}=\begin{bmatrix} \mathbf{v} \end{bmatrix}\left (= \begin{bmatrix} a\\ b \end{bmatrix} \right )" /> #1   
     + (우항의 좌측) 벡터 v1, v2를 기저(basis)로 가지는 **좌표계(coordinate system)** 에서는 동일한 벡터 v의 좌표값은 (4,3)임.   
    
  + <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;\mathbf{v}_{1}&space;&&space;\mathbf{v}_{2}&space;\end{bmatrix}\begin{bmatrix}&space;4\\&space;3&space;\end{bmatrix}=\begin{bmatrix}&space;\mathbf{e}_{1}&space;&&space;\mathbf{e}_{2}&space;\end{bmatrix}\begin{bmatrix}&space;a\\&space;b&space;\end{bmatrix}" title="\begin{bmatrix} \mathbf{v}_{1} & \mathbf{v}_{2} \end{bmatrix}\begin{bmatrix} 4\\ 3 \end{bmatrix}=\begin{bmatrix} \mathbf{e}_{1} & \mathbf{e}_{2} \end{bmatrix}\begin{bmatrix} a\\ b \end{bmatrix}" /> #2  
     + (우항의 좌측) 항등행렬의 열벡터 e1, e2를 기저(basis)로 가지는 **표준좌표계(standard coordinate system)** 에서 벡터 v의 좌표값은 (a,b)임.      
     
     
+ **선형시스템** <img src="https://latex.codecogs.com/gif.latex?A\mathbf{x}=\mathbf{b}" title="A\mathbf{x}=\mathbf{b}" />를 좌표계 변환으로 바라보면,
   + (우항) : 표준좌표계에서 어떤 벡터의 좌표값은 b
   + (좌항) : 행렬 A의 열벡터들을 기저(basis)로 가지는 좌표계에서는 동일 벡터의 좌표값은 x
    
    
+ **선형시스템의 해를 구하는 문제** <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}=A^{-1}\mathbf{b}" title="\mathbf{x}=A^{-1}\mathbf{b}" />를 좌표계 변환으로 바라보면,
   + (좌항) : 표준좌표계에서 어떤 벡터의 좌표값은 x
   + (좌항) : 역행렬 <img src="https://latex.codecogs.com/gif.latex?A^{-1}" title="A^{-1}" />의 열벡터들을 기저(basis)로 가지는 좌표계에서는 동일 벡터의 좌표값은 b

### 정리
+ 행렬 = 좌표계, 벡터 = 좌표값
+ 임의의 벡터 v는 다양한 좌표계에서 표현 가능
   + 표준 좌표계에서 표현된 v = (좌표계 A) (좌표계 A에서 표현된 v) = (좌표계 B) (좌표계 B에서 표현된 v)
   
-----------------------------------------------------------------------------------------
### 예제 1. 좌표계 변환(Change of Basis)
+ 2-벡터 v가 표준좌표계에서 (2,3)으로 표현된다고 하자.
+ 벡터 (3,1), (1,-2)를 기저벡터로 가지는 새로운 좌표계를 도입한다면, 해당 벡터 v는 어떤 좌표값을 가질까?   

  <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;3&space;&&space;1&space;\\&space;1&space;&&space;-2&space;\end{bmatrix}\begin{bmatrix}&space;x_{1}\\&space;x_{2}&space;\end{bmatrix}=&space;\begin{bmatrix}&space;1&space;&&space;0\\&space;0&space;&&space;1&space;\end{bmatrix}\begin{bmatrix}&space;2\\&space;3&space;\end{bmatrix}" title="\begin{bmatrix} 3 & 1 \\ 1 & -2 \end{bmatrix}\begin{bmatrix} x_{1}\\ x_{2} \end{bmatrix}= \begin{bmatrix} 1 & 0\\ 0 & 1 \end{bmatrix}\begin{bmatrix} 2\\ 3 \end{bmatrix}" />   
  <img src="https://latex.codecogs.com/gif.latex?\Rightarrow&space;\therefore&space;\begin{bmatrix}&space;x_{1}\\&space;x_{2}&space;\end{bmatrix}=\begin{bmatrix}&space;1\\&space;-1&space;\end{bmatrix}" title="\Rightarrow \therefore \begin{bmatrix} x_{1}\\ x_{2} \end{bmatrix}=\begin{bmatrix} 1\\ -1 \end{bmatrix}" />   
  
### 예제 2. 3-벡터에 대한 좌표계 변환
+ 3-벡터 v가 표준좌표계에서 (2,1,3)으로 표현된다고 하자.
+ 벡터 (1,3,1), (1,-2,2)를 기저벡터로 가지는 새로운 좌표계를 도입했을 때, 해당 벡터 v는 어떤 좌표값을 가질까?   

  <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;1&space;&&space;1&space;\\&space;3&space;&&space;-2\\&space;1&space;&&space;2&space;\end{bmatrix}\begin{bmatrix}&space;x_{1}\\&space;x_{2}&space;\end{bmatrix}=\begin{bmatrix}&space;1&space;&&space;0&space;&&space;0\\&space;0&space;&&space;1&space;&&space;0\\&space;0&space;&&space;0&space;&&space;1&space;\end{bmatrix}\begin{bmatrix}&space;2\\&space;1\\&space;3&space;\end{bmatrix}" title="\begin{bmatrix} 1 & 1 \\ 3 & -2\\ 1 & 2 \end{bmatrix}\begin{bmatrix} x_{1}\\ x_{2} \end{bmatrix}=\begin{bmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} 2\\ 1\\ 3 \end{bmatrix}" />   
  <img src="https://latex.codecogs.com/gif.latex?\Rightarrow&space;x_{1}\begin{bmatrix}&space;1\\&space;3\\&space;1&space;\end{bmatrix}&plus;x_{2}\begin{bmatrix}&space;1\\&space;-2\\&space;2&space;\end{bmatrix}=\begin{bmatrix}&space;2\\&space;1\\&space;3&space;\end{bmatrix}" title="\Rightarrow x_{1}\begin{bmatrix} 1\\ 3\\ 1 \end{bmatrix}+x_{2}\begin{bmatrix} 1\\ -2\\ 2 \end{bmatrix}=\begin{bmatrix} 2\\ 1\\ 3 \end{bmatrix}" />   
  <img src="https://latex.codecogs.com/gif.latex?\Rightarrow&space;\therefore&space;\begin{bmatrix}&space;x_{1}\\&space;x_{2}&space;\end{bmatrix}=\begin{bmatrix}&space;1\\&space;1&space;\end{bmatrix}" title="\Rightarrow \therefore \begin{bmatrix} x_{1}\\ x_{2} \end{bmatrix}=\begin{bmatrix} 1\\ 1 \end{bmatrix}" />   
