# 행렬연산과 선형조합

--------------------------------
## 행렬 기본
+ **행렬(matrix)** : 숫자들을 직사각형 모양으로 배열한 구조
+ m x n 행렬은 m개의 행, n개의 열로 숫자들을 직사각형 구조에 채워진 형태   

  <img src="https://latex.codecogs.com/gif.latex?A=\begin{bmatrix}&space;a_{11}&space;&&space;a_{12}&space;&&space;...&space;&&space;a_{1j}&space;&&space;...&space;&&space;a_{1n}\\&space;a_{21}&space;&&space;a_{22}&space;&&space;...&space;&&space;a_{2j}&space;&&space;...&space;&&space;a_{2n}\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots&space;\\&space;a_{i1}&space;&&space;a_{i2}&space;&&space;&&space;a_{ij}&space;&&space;...&space;&&space;a_{in}&space;\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots\\&space;a_{m1}&space;&&space;a_{m2}&space;&&space;...&space;&&space;a_{mj}&space;&&space;...&space;&&space;a_{mn}&space;\end{bmatrix}" title="A=\begin{bmatrix} a_{11} & a_{12} & ... & a_{1j} & ... & a_{1n}\\ a_{21} & a_{22} & ... & a_{2j} & ... & a_{2n}\\ \vdots & \vdots & & \vdots & & \vdots \\ a_{i1} & a_{i2} & & a_{ij} & ... & a_{in} \\ \vdots & \vdots & & \vdots & & \vdots\\ a_{m1} & a_{m2} & ... & a_{mj} & ... & a_{mn} \end{bmatrix}" />   
  
+ 행렬 A의 각 <img src="https://latex.codecogs.com/gif.latex?(i,j)" title="(i,j)" />-요소 : <img src="https://latex.codecogs.com/gif.latex?a_{ij}" title="a_{ij}" /> 
+ 행렬 A의 간략한 표기할 때 <img src="https://latex.codecogs.com/gif.latex?A=[a_{ij}]" title="A=[a_{ij}]" />으로 표기
+ 행렬 A의 크기도 같이 표현하려면 <img src="https://latex.codecogs.com/gif.latex?A=[a_{ij}]_{m\times&space;n}" title="A=[a_{ij}]_{m\times n}" />으로 표기

+ 전치행렬(Transpose Matrix) : m x n 행렬 A에 대한 전치 행렬은 <img src="https://latex.codecogs.com/gif.latex?A^{T}" title="A^{T}" />는 A의 행을 열로, A의 열을 행으로 가지는 n x m 행렬 
  > 즉, <img src="https://latex.codecogs.com/gif.latex?(A^{T})_{ij}=(A)_{ij}" title="(A^{T})_{ij}=(A)_{ij}" />  
  
  <img src="https://latex.codecogs.com/gif.latex?A^{T}=\begin{bmatrix}&space;a_{11}&space;&&space;a_{12}&space;&&space;...&space;&&space;a_{1j}&space;&&space;...&space;&&space;a_{1m}\\&space;a_{21}&space;&&space;a_{22}&space;&&space;...&space;&&space;a_{2j}&space;&&space;...&space;&&space;a_{2m}\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots&space;\\&space;a_{i1}&space;&&space;a_{i2}&space;&&space;&&space;a_{ij}&space;&&space;...&space;&&space;a_{im}&space;\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots\\&space;a_{n1}&space;&&space;a_{n2}&space;&&space;...&space;&&space;a_{nj}&space;&&space;...&space;&&space;a_{nm}&space;\end{bmatrix}" title="A^{T}=\begin{bmatrix} a_{11} & a_{12} & ... & a_{1j} & ... & a_{1m}\\ a_{21} & a_{22} & ... & a_{2j} & ... & a_{2m}\\ \vdots & \vdots & & \vdots & & \vdots \\ a_{i1} & a_{i2} & & a_{ij} & ... & a_{im} \\ \vdots & \vdots & & \vdots & & \vdots\\ a_{n1} & a_{n2} & ... & a_{nj} & ... & a_{nm} \end{bmatrix}" />   
  
+ 벡터는 볼드체 소문자 로 표기
   ex) <img src="https://latex.codecogs.com/gif.latex?\mathbf{x,&space;y,&space;z&space;...}" title="\mathbf{x, y, z ...}" />   
         
   > + 여기에 내용정리할 때, 정확히 표기를 안했는데 이전에 Ax=b에서 x, b는 열벡터.   
   > + 일반적으로 벡터는 열벡터(column vector)를 말하며, n-벡터는 n개의 스칼라(scalar)로 구성된 벡터를 말함
   
+ 영행렬(zero matrix) : 모든 요소가 0인 행렬, <img src="https://latex.codecogs.com/gif.latex?O" title="O" />으로 표기
   > 숫자 0과 같은 존재, 행렬합에 대한 항등원 역할
   > 두 행렬을 더해주려면, 같은 크기여야함 (즉, 행과 열 개수가 같아야 더할 수 있음)
   
+ 정방행렬(Square Matrix) : 행과 열의 개수가 모두 n인 정사각형 모양의 행렬 = n차 정방행렬   
   + 대각선에 있는 요소들<img src="https://latex.codecogs.com/gif.latex?(a_{11},&space;a_{22},&space;...,&space;a_{ii})" title="(a_{11}, a_{22}, ..., a_{ii})" />을 주대각선(maxin diagonal)이라 함   
   
      
   <img src="https://latex.codecogs.com/gif.latex?A=\begin{bmatrix}&space;a_{11}&space;&&space;a_{12}&space;&&space;...&space;&&space;a_{1i}&space;&&space;...&space;&&space;a_{1n}\\&space;a_{21}&space;&&space;a_{22}&space;&&space;...&space;&&space;a_{2i}&space;&&space;...&space;&&space;a_{2n}\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots&space;\\&space;a_{i1}&space;&&space;a_{i2}&space;&&space;&&space;a_{ii}&space;&&space;...&space;&&space;a_{in}&space;\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots\\&space;a_{n1}&space;&&space;a_{n2}&space;&&space;...&space;&&space;a_{ni}&space;&&space;...&space;&&space;a_{nn}&space;\end{bmatrix}" title="A=\begin{bmatrix} a_{11} & a_{12} & ... & a_{1i} & ... & a_{1n}\\ a_{21} & a_{22} & ... & a_{2i} & ... & a_{2n}\\ \vdots & \vdots & & \vdots & & \vdots \\ a_{i1} & a_{i2} & & a_{ii} & ... & a_{in} \\ \vdots & \vdots & & \vdots & & \vdots\\ a_{n1} & a_{n2} & ... & a_{ni} & ... & a_{nn} \end{bmatrix}" />    
   
+ 항등행렬(Identity Matrix) : 주대각선이 1이고, 나머지가 모두 0인 n차 정방행렬   
   > 숫자 1과 같은 존재, 행렬곱에 대한 항등원 역할
   
   <img src="https://latex.codecogs.com/gif.latex?I_{n}=\begin{bmatrix}&space;1&space;&&space;0&space;&&space;...&space;&&space;0&space;&&space;...&space;&&space;0\\&space;0&space;&&space;1&space;&&space;...&space;&&space;0&space;&&space;...&space;&&space;0\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots&space;\\&space;0&&space;0&&space;&&space;1&space;&&space;...&space;&&space;0&space;\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots\\&space;0&space;&&space;0&&space;...&space;&&space;0&space;&&space;...&space;&&space;1&space;\end{bmatrix}" title="I_{n}=\begin{bmatrix} 1 & 0 & ... & 0 & ... & 0\\ 0 & 1 & ... & 0 & ... & 0\\ \vdots & \vdots & & \vdots & & \vdots \\ 0& 0& & 1 & ... & 0 \\ \vdots & \vdots & & \vdots & & \vdots\\ 0 & 0& ... & 0 & ... & 1 \end{bmatrix}" />   
 
-----------------------------------------------------------------------------------------
## 행렬 곱   
+ <img src="https://latex.codecogs.com/gif.latex?A\cdot&space;B=C" title="A\cdot B=C" />   
   
   <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;*&space;&&space;*&space;&&space;...&space;&&space;*&space;\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;\\&space;a_{i1}&space;&&space;a_{i2}&space;&&space;...&space;&&space;a_{ir}&space;\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;\\&space;*&space;&&space;*&space;&&space;...&space;&&space;*&space;\end{bmatrix}" title="\begin{bmatrix} * & * & ... & * \\ \vdots & \vdots & & \vdots \\ a_{i1} & a_{i2} & ... & a_{ir} \\ \vdots & \vdots & & \vdots \\ * & * & ... & * \end{bmatrix}" /> <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;*&space;&&space;...&space;&&space;b_{1j}&space;&&space;...&space;&&space;*&space;\\&space;*&space;&&space;...&space;&&space;b_{2j}&space;&&space;...&space;&&space;*&space;\\&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots&space;\\&space;*&space;&&space;...&space;&&space;b_{rj}&space;&&space;...&space;&&space;*&space;\end{bmatrix}=\begin{bmatrix}&space;*&space;&&space;...&space;&&space;*&space;&&space;...&space;&&space;*\\&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots&space;\\&space;*&space;&&space;...&space;&&space;c_{ij}&space;&&space;...&space;&&space;*\\&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots&space;\\&space;*&space;&&space;...&space;&&space;*&space;&&space;...&space;&&space;*&space;\end{bmatrix}" title="\begin{bmatrix} * & ... & b_{1j} & ... & * \\ * & ... & b_{2j} & ... & * \\ \vdots & & \vdots & & \vdots \\ * & ... & b_{rj} & ... & * \end{bmatrix}=\begin{bmatrix} * & ... & * & ... & *\\ \vdots & & \vdots & & \vdots \\ * & ... & c_{ij} & ... & *\\ \vdots & & \vdots & & \vdots \\ * & ... & * & ... & * \end{bmatrix}" />   
   
   + <img src="https://latex.codecogs.com/gif.latex?A=[a_{ij}]" title="A=[a_{ij}]" /> : **m x r 행렬**   
   
   + <img src="https://latex.codecogs.com/gif.latex?B=[b_{ij}]" title="B=[b_{ij}]" /> : **r x n 행렬**   
   
   + <img src="https://latex.codecogs.com/gif.latex?C=[c_{ij}]" title="C=[c_{ij}]" /> : 행렬 A와 B의 곱으로 **m x n 행렬**   
   > 행렬 C의 각 (i,j)-요소 : <img src="https://latex.codecogs.com/gif.latex?c_{ij}=a_{i1}b_{1j}&plus;&space;...&space;&plus;&space;a_{ir}b_{rj}" title="c_{ij}=a_{i1}b_{1j}+ ... + a_{ir}b_{rj}" />   
   
   > 이는 행렬 A의 i번째 행벡터, 행렬 B의 j번째 열벡터의 내적(inner product)   
   
+ 따라서, 두 행렬의 곱 AB에 대해 A의 열개수 = B의 행개수 일치해야함  
+ 일반적으로 **AB와 BA는 다르다** (행과 열을 뽑아오는 방법이 다르므로)  
+ 행렬의 곱은 **병렬처리(parallel processing)으로 가속 가능**     

---------------------------------------------------------------------------------------
## 스칼라, 벡터, 행렬, 그리고 텐서 : 계층적 구조 이해하기

+ 스칼라 : 숫자 하나로 구성
   + 벡터로 표현하면 1개의 구성요소로 이뤄진 1-벡터, 행렬로 표현하면 1 x 1 행렬
+ 벡터 : 여러 숫자가 일열로 늘어선 구조
   + 벡터를 행렬로 표현하면 여러 모양의 행렬로 표현 가능   
   
      <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;1\\&space;2\\&space;3\\&space;4&space;\end{bmatrix},&space;{\begin{bmatrix}&space;1&space;&&space;2\\&space;3&space;&&space;4&space;\end{bmatrix}}_{2\times&space;2},&space;{\begin{bmatrix}&space;1&space;&&space;3&space;\\&space;2&space;&&space;4&space;\end{bmatrix}}_{2\times&space;2},&space;{\begin{bmatrix}&space;1&space;&&space;2&space;&&space;3&space;&&space;4&space;\end{bmatrix}}_{1\times&space;4}" title="\begin{bmatrix} 1\\ 2\\ 3\\ 4 \end{bmatrix}, {\begin{bmatrix} 1 & 2\\ 3 & 4 \end{bmatrix}}_{2\times 2}, {\begin{bmatrix} 1 & 3 \\ 2 & 4 \end{bmatrix}}_{2\times 2}, {\begin{bmatrix} 1 & 2 & 3 & 4 \end{bmatrix}}_{1\times 4}" />   

+ 행렬은 사각형 구조에 여러 숫자가 행/열로 늘어선 구조
   + 벡터로 표현 가능   
   
      <img src="https://latex.codecogs.com/gif.latex?{\begin{bmatrix}&space;1&space;&&space;2&space;&&space;3&space;\\&space;4&space;&&space;5&space;&&space;6&space;\end{bmatrix}}_{2\times&space;3}&space;=\begin{bmatrix}&space;1\\&space;2\\&space;3\\&space;4\\&space;5\\&space;6&space;\end{bmatrix}" title="{\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}}_{2\times 3} =\begin{bmatrix} 1\\ 2\\ 3\\ 4\\ 5\\ 6 \end{bmatrix}" />, <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;1\\&space;4\\&space;2\\&space;5\\&space;3\\&space;6&space;\end{bmatrix}" title="\begin{bmatrix} 1\\ 4\\ 2\\ 5\\ 3\\ 6 \end{bmatrix}" />, ...    
   
+ 텐서(tensor) : 스칼라, 벡터, 행렬을 아우르는 개념이며, 숫자가 늘어날 수 있는 방향이 k개면 k-텐서라 부름
   + 0-텐서 : 스칼라
   + 1-텐서 : 벡터
   + 2-텐서 : 행렬
   + T의 요소 p(i,j)가 벡터라면, T는 3-텐서   
   
     <img src="https://latex.codecogs.com/gif.latex?T=\begin{bmatrix}&space;\mathbf{p}_{(1,1)}&space;&&space;\mathbf{p}_{(1,2)}&space;&&space;\mathbf{p}_{(1,3)}&space;&&space;\mathbf{p}_{(1,4)}&space;\\&space;\mathbf{p}_{(2,1)}&space;&&space;\mathbf{p}_{(2,2)}&space;&&space;\mathbf{p}_{(2,3)}&space;&&space;\mathbf{p}_{(2,4)}\\&space;\mathbf{p}_{(3,1)}&space;&&space;\mathbf{p}_{(3,2)}&space;&&space;\mathbf{p}_{(3,3)}&space;&&space;\mathbf{p}_{(3,4)}\\&space;\mathbf{p}_{(4,1)}&space;&&space;\mathbf{p}_{(4,2)}&space;&&space;\mathbf{p}_{(4,3)}&space;&&space;\mathbf{p}_{(4,4)}&space;\end{bmatrix}" title="T=\begin{bmatrix} \mathbf{p}_{(1,1)} & \mathbf{p}_{(1,2)} & \mathbf{p}_{(1,3)} & \mathbf{p}_{(1,4)} \\ \mathbf{p}_{(2,1)} & \mathbf{p}_{(2,2)} & \mathbf{p}_{(2,3)} & \mathbf{p}_{(2,4)}\\ \mathbf{p}_{(3,1)} & \mathbf{p}_{(3,2)} & \mathbf{p}_{(3,3)} & \mathbf{p}_{(3,4)}\\ \mathbf{p}_{(4,1)} & \mathbf{p}_{(4,2)} & \mathbf{p}_{(4,3)} & \mathbf{p}_{(4,4)} \end{bmatrix}" />    
      > 3-텐서의 대표적인 예로는 컬러영상으로 3-벡터이면 RGB 영상, 4-벡터이면 RGBA 영상   
      
---------------------------------------------------------------------------------
## **분할행렬(Partitioned Matrix)** 
+ 행렬을 구조적으로 보는 방법으로 블록행렬(block matrix)이라고도 함
+ 행렬을 조각 단위로 분할하여 생각하는 것, 행렬은 부분행렬(submatrix)로 이뤄진 직사각형 구조로 생각할 수 있음
+ 행벡터들의 모임으로 생각해서 표현할 수 있고, 열벡터들의 모임으로 생각해서 표현할 수 있음.
   + 14 x 14 행렬을 <img src="https://latex.codecogs.com/gif.latex?2^{i}\times&space;2^{j}" title="2^{i}\times 2^{j}" />의 행렬 블록들로 분할하면, (이때, i,j는 1,2,3)      
     
     ![image](https://user-images.githubusercontent.com/72974863/101445207-680b0e80-3964-11eb-84c1-63761f015ed6.png)      
     
     > [블록행렬-위키백과](https://ko.wikipedia.org/wiki/%EB%B8%94%EB%A1%9D_%ED%96%89%EB%A0%AC)   
     

+ 분할행렬로 행렬곱 하기

   + 두 행렬의 곱 AB=C를 **maxtrix-column vector products** 로 볼 수 있음   
   
     <img src="https://latex.codecogs.com/gif.latex?AB=A\begin{bmatrix}&space;\mathbf{b}_{1}&space;&&space;\mathbf{b}_{2}&space;&&space;...&space;&&space;\mathbf{b}_{n}&space;\end{bmatrix}&space;=\begin{bmatrix}&space;A\mathbf{b}_{1}&space;&&space;A\mathbf{b}_{2}&space;&&space;...&space;&&space;A\mathbf{b}_{n}&space;\end{bmatrix}=C" title="AB=A\begin{bmatrix} \mathbf{b}_{1} & \mathbf{b}_{2} & ... & \mathbf{b}_{n} \end{bmatrix} =\begin{bmatrix} A\mathbf{b}_{1} & A\mathbf{b}_{2} & ... & A\mathbf{b}_{n} \end{bmatrix}=C" />   
   
   + 두 행렬 곱 AB=C를 **row vector-matrix products** 으로도 볼 수 있음    
   
     <img src="https://latex.codecogs.com/gif.latex?AB=\begin{bmatrix}&space;\boldsymbol{\mathbf{a}_{1}}\\&space;\mathbf{a}_{2}\\&space;\vdots&space;\\&space;\mathbf{a}_{m}&space;\end{bmatrix}B=&space;\begin{bmatrix}&space;\mathbf{a}_{1}B\\&space;\mathbf{a}_{2}B\\&space;\vdots&space;\\&space;\mathbf{a}_{m}B&space;\end{bmatrix}=C" title="AB=\begin{bmatrix} \boldsymbol{\mathbf{a}_{1}}\\ \mathbf{a}_{2}\\ \vdots \\ \mathbf{a}_{m} \end{bmatrix}B= \begin{bmatrix} \mathbf{a}_{1}B\\ \mathbf{a}_{2}B\\ \vdots \\ \mathbf{a}_{m}B \end{bmatrix}=C" />   
   
---------------------------------------------------------------------------------------
## 선형 조합(Linear Combination)

+ **Ax는 A의 열벡터에 대한 선형 조합** 
+ 행렬은 열벡터의 리스트, m x n 행렬은 m-벡터가 n개 있다고 생각하자   

   <img src="https://latex.codecogs.com/gif.latex?A=\begin{bmatrix}&space;a_{11}&space;&&space;a_{12}&space;&&space;...&space;&&space;a_{1j}&space;&&space;...&space;&&space;a_{1n}\\&space;a_{21}&space;&&space;a_{22}&space;&&space;...&space;&&space;a_{2j}&space;&&space;...&space;&&space;a_{2n}\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots&space;\\&space;a_{i1}&space;&&space;a_{i2}&space;&&space;&&space;a_{ij}&space;&&space;...&space;&&space;a_{in}&space;\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots\\&space;a_{m1}&space;&&space;a_{m2}&space;&&space;...&space;&&space;a_{mj}&space;&&space;...&space;&&space;a_{mn}&space;\end{bmatrix}=\begin{bmatrix}&space;\mathbf{a}_{1}&space;&&space;\mathbf{a}_{2}&space;&&space;...&space;&&space;\mathbf{a}_{n}&space;\end{bmatrix}" title="A=\begin{bmatrix} a_{11} & a_{12} & ... & a_{1j} & ... & a_{1n}\\ a_{21} & a_{22} & ... & a_{2j} & ... & a_{2n}\\ \vdots & \vdots & & \vdots & & \vdots \\ a_{i1} & a_{i2} & & a_{ij} & ... & a_{in} \\ \vdots & \vdots & & \vdots & & \vdots\\ a_{m1} & a_{m2} & ... & a_{mj} & ... & a_{mn} \end{bmatrix}=\begin{bmatrix} \mathbf{a}_{1} & \mathbf{a}_{2} & ... & \mathbf{a}_{n} \end{bmatrix}" />   
   
+ Ax는 행렬 A가 가지고 있는 열벡터의 선형조합   
   <img src="https://latex.codecogs.com/gif.latex?A\boldsymbol{\mathbf{x}}=\begin{bmatrix}&space;a_{11}&space;&&space;a_{12}&space;&&space;...&space;&&space;a_{1j}&space;&&space;...&space;&&space;a_{1n}\\&space;a_{21}&space;&&space;a_{22}&space;&&space;...&space;&&space;a_{2j}&space;&&space;...&space;&&space;a_{2n}\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots&space;\\&space;a_{i1}&space;&&space;a_{i2}&space;&&space;&&space;a_{ij}&space;&&space;...&space;&&space;a_{in}&space;\\&space;\vdots&space;&&space;\vdots&space;&&space;&&space;\vdots&space;&&space;&&space;\vdots\\&space;a_{m1}&space;&&space;a_{m2}&space;&&space;...&space;&&space;a_{mj}&space;&&space;...&space;&&space;a_{mn}&space;\end{bmatrix}&space;\begin{bmatrix}&space;x_{1}\\&space;x_{2}\\&space;\vdots&space;\\&space;x_{n}&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;\mathbf{a}_{1}&space;&&space;\mathbf{a}_{2}&space;&&space;...&space;&&space;\mathbf{a}_{n}&space;\end{bmatrix}\begin{bmatrix}&space;x_{1}\\&space;x_{2}\\&space;\vdots&space;\\&space;x_{n}&space;\end{bmatrix}" title="A\boldsymbol{\mathbf{x}}=\begin{bmatrix} a_{11} & a_{12} & ... & a_{1j} & ... & a_{1n}\\ a_{21} & a_{22} & ... & a_{2j} & ... & a_{2n}\\ \vdots & \vdots & & \vdots & & \vdots \\ a_{i1} & a_{i2} & & a_{ij} & ... & a_{in} \\ \vdots & \vdots & & \vdots & & \vdots\\ a_{m1} & a_{m2} & ... & a_{mj} & ... & a_{mn} \end{bmatrix} \begin{bmatrix} x_{1}\\ x_{2}\\ \vdots \\ x_{n} \end{bmatrix} = \begin{bmatrix} \mathbf{a}_{1} & \mathbf{a}_{2} & ... & \mathbf{a}_{n} \end{bmatrix}\begin{bmatrix} x_{1}\\ x_{2}\\ \vdots \\ x_{n} \end{bmatrix}" />   
   
   <img src="https://latex.codecogs.com/gif.latex?=x_{1}\mathbf{a_{1}}&plus;x_{2}\mathbf{a_{2}}&plus;...&plus;x_{n}\mathbf{a_{n}}" title="=x_{1}\mathbf{a_{1}}+x_{2}\mathbf{a_{2}}+...+x_{n}\mathbf{a_{n}}" />   
   
   > 선형 대수에서는 벡터들에 대한 가중치 합을 선형조합(linear combination)이라 부름   
   > Ax의 결과는 행렬 A가 갖고 있는 열벡터의 가중치 합을 벗어날 수 없음   
   
+ **예를 들어**, 선형시스템 Ax=b가 주어졌다고 하자.   
   <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;-1&space;&&space;3&space;&&space;2\\&space;1&space;&&space;2&space;&&space;-3\\&space;2&space;&&space;1&space;&&space;-2&space;\end{bmatrix}\begin{bmatrix}&space;x_{1}\\&space;x_{2}\\&space;x_{3}&space;\end{bmatrix}=\begin{bmatrix}&space;1\\&space;9\\&space;-3&space;\end{bmatrix}" title="\begin{bmatrix} -1 & 3 & 2\\ 1 & 2 & -3\\ 2 & 1 & -2 \end{bmatrix}\begin{bmatrix} x_{1}\\ x_{2}\\ x_{3} \end{bmatrix}=\begin{bmatrix} 1\\ 9\\ -3 \end{bmatrix}" />   
   
   + (좌항) 선형조합으로 해석한 Ax는 다음과 같다.   
      <img src="https://latex.codecogs.com/gif.latex?x_{1}\begin{bmatrix}&space;-1\\&space;1\\&space;2&space;\end{bmatrix}&plus;&space;x_{2}\begin{bmatrix}&space;3\\&space;2\\&space;1&space;\end{bmatrix}&plus;x_{3}\begin{bmatrix}&space;2\\&space;-3\\&space;-2&space;\end{bmatrix}" title="x_{1}\begin{bmatrix} -1\\ 1\\ 2 \end{bmatrix}+ x_{2}\begin{bmatrix} 3\\ 2\\ 1 \end{bmatrix}+x_{3}\begin{bmatrix} 2\\ -3\\ -2 \end{bmatrix}" />   
      
   +  (우항) b는 다음과 같다.   
      <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;1\\&space;-9\\&space;-3&space;\end{bmatrix}" title="\begin{bmatrix} 1\\ -9\\ -3 \end{bmatrix}" />   
   
   + 벡터 b를 만들수있는 Ax의 가중치 합이 존재하느냐, 즉 가중치 x가 존재하느냐   
   
+ 열공간(Column Sapce) : 행렬 A의 열벡터들에 대한 가능한 모든 선형조합의 결과 집합, <img src="https://latex.codecogs.com/gif.latex?col(A)" title="col(A)" />으로 표기   
   + 선형 시스템 Ax=b가 해를 가지면(consistent), <img src="https://latex.codecogs.com/gif.latex?\mathbf{b}\in&space;col(A)" title="\mathbf{b}\in col(A)" />   
   + 선형 시스템 Ax=b가 해가 없다면(inconsistent), <img src="https://latex.codecogs.com/gif.latex?\mathbf{b}\notin&space;col(A)" title="\mathbf{b}\notin col(A)" />   
   
