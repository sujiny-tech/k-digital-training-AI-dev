# 벡터공간(Vector space)

+ [열린집합과 닫힌집합-위키백과](https://ko.wikipedia.org/wiki/%EC%97%B4%EB%A6%B0%EC%A7%91%ED%95%A9)
+ 공간(space) : 덧셈연산과 스칼라 곱 연산에 닫혀있는 집합
+ n-벡터의 집합은 모두 공간이며, <img src="https://latex.codecogs.com/gif.latex?x_{i}\in&space;\mathbb{R}" title="x_{i}\in \mathbb{R}" />에 대해 <img src="https://latex.codecogs.com/gif.latex?\mathbb{R}^{n}=\left&space;\{\mathbf{x}|\mathbf{x}=\left&space;(&space;x_{1},x_{2},&space;...,&space;x_{n}&space;\right&space;)&space;\right&space;\}" title="\mathbb{R}^{n}=\left \{\mathbf{x}|\mathbf{x}=\left ( x_{1},x_{2}, ..., x_{n} \right ) \right \}" />으로 나타낼 수 있음   
+ **모든 n-벡터 집합** <img src="https://latex.codecogs.com/gif.latex?\mathbb{R}^{n}" title="\mathbb{R}^{n}" />은 **n차원 벡터 공간(vector space)** 

+ 열공간(Column Space) : 행렬 A의 열벡터들에 대한 **가능한 모든 선형조합의 결과** 의 집합 : <img src="https://latex.codecogs.com/gif.latex?col(A)" title="col(A)" />   
  + Consistent Linear System : <img src="https://latex.codecogs.com/gif.latex?\mathbf{b}\in&space;col(A)" title="\mathbf{b}\in col(A)" />   
  + Inconsistent Linear System : <img src="https://latex.codecogs.com/gif.latex?\mathbf{b}\notin&space;col(A)" title="\mathbf{b}\notin col(A)" />   
  
- - - - - - - - - - - - - - -
# 최소제곱법(Least Squares Method)
+ 선형시스템 Ax=b에 대한 해가 없음에도 불구하고, **목표 b에 가장 가까운 지점** 을 구하는 방법 (최선의 방법을 구하는 방법)
   + 달성가능한 최선의 목표 <img src="https://latex.codecogs.com/gif.latex?proj_{W}\mathbf{b}" title="proj_{W}\mathbf{b}" />
   + 즉, 선형시스템 <img src="https://latex.codecogs.com/gif.latex?A\mathbf{\bar{x}}=\mathbf{\bar{b}}" title="A\mathbf{\bar{x}}=\mathbf{\bar{b}}" />을 해결.   
   
      > 단, <img src="https://latex.codecogs.com/gif.latex?\mathbf{\bar{b}}=proj_{W}\mathbf{b}" title="\mathbf{\bar{b}}=proj_{W}\mathbf{b}" />   
      
   + 목표 <img src="https://latex.codecogs.com/gif.latex?\mathbf{b}" title="\mathbf{b}" />와 최선의 대안 <img src="https://latex.codecogs.com/gif.latex?\mathbf{\bar{b}}" title="\mathbf{\bar{b}}" />의 차이를 나타내는 벡터의 제곱길이를 최소화 시키는 방법 
   
+ 최소제곱법의 해 구하기
   + 주어진 선형시스템의 양변에 A의 전치행렬을 곱하면 구할 수 있음   
   
      <img src="https://latex.codecogs.com/gif.latex?A\mathbf{x}=\mathbf{b}\Rightarrow&space;A^{T}A\mathbf{\bar{x}}=A^{T}\mathbf{b}\Rightarrow&space;\mathbf{\bar{x}}=(A^{T}A)^{-1}A^{T}\mathbf{b}" title="A\mathbf{x}=\mathbf{b}\Rightarrow A^{T}A\mathbf{\bar{x}}=A^{T}\mathbf{b}\Rightarrow \mathbf{\bar{x}}=(A^{T}A)^{-1}A^{T}\mathbf{b}" />   
      
      + 최소제곱법으로 구한 해 <img src="https://latex.codecogs.com/gif.latex?\mathbf{\bar{x}}" title="\mathbf{\bar{x}}" />는 <img src="https://latex.codecogs.com/gif.latex?A\mathbf{\bar{x}}=proj_{W}\mathbf{b}" title="A\mathbf{\bar{x}}=proj_{W}\mathbf{b}" />를 만족하는 **근사해(approximate solution)**    
      
     
- - - - - - - - - - - - - -
### 최소 제곱법 응용 ✨

#### 선형 회귀(Linear Regrssion) 
+ 2차원 공간에 있는 m개의 정점들에 대해, 이 정점들을 잘 표현할수있는 **직선 y=mx+b를 구하는 문제** 
   1. 선형 시스템 구성 : 직선이 각 정점을 모두 지난다고 가정하고, Ax=b를 구성
     > 그러나, 모든 정점을 지나는 직선은 존재하지 않으므로 해는 존재x   
     
   2. 최소제곱법 적용 : <img src="https://latex.codecogs.com/gif.latex?A^{T}A\mathbf{\bar{x}}=A^{T}\mathbf{b}" title="A^{T}A\mathbf{\bar{x}}=A^{T}\mathbf{b}" />를 생각하고, <img src="https://latex.codecogs.com/gif.latex?\mathbf{\bar{x}}=\begin{bmatrix}&space;\bar{m}\\&space;\bar{b}&space;\end{bmatrix}" title="\mathbf{\bar{x}}=\begin{bmatrix} \bar{m}\\ \bar{b} \end{bmatrix}" />를 구함.   
   
