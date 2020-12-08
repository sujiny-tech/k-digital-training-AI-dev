# 선형 변환(Linear Transformation)

- - - - - - - - - - -
## 함수    
  + input을 통해 어떤 기능을 수행한 다음 output을 뱉어내는 **블랙박스(black box)**   
    ![image](https://user-images.githubusercontent.com/72974863/101455889-9691e500-3976-11eb-9457-d404c3e61af9.png)   
    
  + 두 집합 간의 **매핑룰(mapping rule)**   
    ![image](https://user-images.githubusercontent.com/72974863/101456089-e07acb00-3976-11eb-9668-be55d66110ee.png)   
     + X는 정의역(domain)
     + Y는 출력공간인 공역(codomain)
     + 공역 중, 실제 함수의 출력이 나오는 부분집합을 치역(range)   
     
  + ###### [그림 출처-위키백과](https://ko.wikipedia.org/wiki/%ED%95%A8%EC%88%98)   
  
- - - - - - - - - - -   
## 선형함수(Linear Function)
+ 다음 두 조건을 만족하는 함수 f를 선형함수이다.   
  
   1. <img src="https://latex.codecogs.com/gif.latex?f(x&plus;y)=f(x)&plus;f(y)" title="f(x+y)=f(x)+f(y)" />   
     
   2. <img src="https://latex.codecogs.com/gif.latex?f(cx)=cf(x)" title="f(cx)=cf(x)" /> (단, c는 임의의 스칼라)   

- - - - - - - - - - -
## 선형 변환(Linear Transformation)
+ n-벡터를 입력으로하여, m-벡터를 출력하는 함수 T처럼 입출력이 벡터인 함수를 변환(transformation)이라 한다.   

  <img src="https://latex.codecogs.com/gif.latex?T&space;:&space;\mathbb{R}^{n}\rightarrow&space;\mathbb{R}^{m}" title="T : \mathbb{R}^{n}\rightarrow \mathbb{R}^{m}" />   
  
   + 특별히 n=m인 경우, 해당 변환을 연산자(operator)라 한다.  
   
+ **예)** 28 x 28 해상도의 손글씨 숫자 영상을 그레이스케일로 받아서, 어떤 숫자가 적혀있는지 알아내는 MNIST 손글씨 인식 문제는 다음과 같은 (비선형) 변환이다.  
   
     <img src="https://latex.codecogs.com/gif.latex?T&space;:&space;\mathbb{R}^{28\times&space;28}\rightarrow&space;\mathbb{R}^{10}" title="T : \mathbb{R}^{28\times 28}\rightarrow \mathbb{R}^{10}" />   
     
+ 행렬 변환(Matrix Transformation)
   + m x n 행렬 A에 대해 Ax는 n-벡터를 입력으로 하여 m-벡터를 출력으로 하는 변환 <img src="https://latex.codecogs.com/gif.latex?T_{A(\mathbf{x})}=A\mathbf{x}" title="T_{A(\mathbf{x})}=A\mathbf{x}" />으로 볼 수 있음.
   + 이를 행렬 변환이라 하며 수식으로 는 다음과 같다.   
   
     <img src="https://latex.codecogs.com/gif.latex?T_{A}&space;:&space;\mathbb{R}^{n}\rightarrow&space;\mathbb{R}^{m}" title="T_{A} : \mathbb{R}^{n}\rightarrow \mathbb{R}^{m}" />   
     
   + 선형함수의 성질을 모두 만족하므로, 선형 변환임. (즉, 행렬변환은 선형변환 중의 일종)
  
- - - - - - - - - - - -

## :dizzy: 정리
+ **m x n 행렬** 은 n-벡터를 입력으로 받아 m-벡터를 출력하는 **선형변환** 
+ **임의의 선형변환** 은 **행렬로 표현 가능** 
+ 행렬은 **선형변환의 구현체** 

- - - - - - - - - - - -

## 표준 행렬(standard matrix)

### 선형변환 코딩하기
+ 다음 과정을 통해 원하는 기능을 갖는 행렬변환을 코딩할 수 있음.
   + 구현하고자 하는 기능(function)이 입출력이 벡터인가
   + 구현하고자 하는 기능이 선형인가
   + 입력이 n-벡터이고, 출력이 m-벡터이면, **m x n 표준 행렬을 구성** 
   
+ 다음 **m x n 표준행렬을 구성** 함으로써, 원하는 기능을 갖는 행렬 변환 <img src="https://latex.codecogs.com/gif.latex?T_{A}&space;:&space;\mathbb{R}^{n}\rightarrow&space;\mathbb{R}^{m}" title="T_{A} : \mathbb{R}^{n}\rightarrow \mathbb{R}^{m}" />을 코딩할 수 있다.   

   <img src="https://latex.codecogs.com/gif.latex?A=\begin{bmatrix}&space;T_{A}(\mathbf{e_{1}})&space;&&space;T_{A}(\mathbf{e_{2}})&space;&&space;...&space;&&space;T_{A}(\mathbf{e_{n}})&space;\end{bmatrix}_{m\times&space;n}" title="A=\begin{bmatrix} T_{A}(\mathbf{e_{1}}) & T_{A}(\mathbf{e_{2}}) & ... & T_{A}(\mathbf{e_{n}}) \end{bmatrix}_{m\times n}" />   
   
   + n-차원 표준기저벡터 <img src="https://latex.codecogs.com/gif.latex?\left&space;\{&space;\mathbf{e}_{1},&space;\mathbf{e}_{2},&space;...&space;,&space;\mathbf{e}_{n}&space;\right&space;\}" title="\left \{ \mathbf{e}_{1}, \mathbf{e}_{2}, ... , \mathbf{e}_{n} \right \}" /> 생각하기   
   + 각 n-차원 표준기저벡터 <img src="https://latex.codecogs.com/gif.latex?\mathbf{e}_{i}" title="\mathbf{e}_{i}" />에 대해, 원하는 기능을 통해 나온 m-차원 벡터 <img src="https://latex.codecogs.com/gif.latex?T(\mathbf{e}_{i})" title="T(\mathbf{e}_{i})" />를 표준행렬의 각 열에 적기    
   
   
### 예제 1) 2차원 벡터를 입력으로 받아서 해당 벡터를 x-축에 프로젝션하는 기능을 구현하기
+ 변환인가? : 입출력이 벡터인가 OK
+ x-축 프로젝션 : 선형인가 OK
+ 입력 2차원, 출력 2차원 : 2 x 2 표준행렬 구성하기   
   + 예를 들어, (3,2)를 입력으로 한다면 (3,0)을 출력으로 해야한다.
   + x축 기저는 (1,0)이며, y축 기저는 (0,1)임
   + x축 기저에 대한 프로젝션은 (1,0)이며, y축 기저에 대한 프로젝션은 (0,0)이므로, 2 x 2 표준 행렬은 다음과 같다.   
   
     <img src="https://latex.codecogs.com/gif.latex?A_{2\times&space;2}=\begin{bmatrix}&space;1&space;&&space;0\\&space;0&space;&&space;0&space;\end{bmatrix}" title="A_{2\times 2}=\begin{bmatrix} 1 & 0\\ 0 & 0 \end{bmatrix}" />   
   
### 예제 2) 2차원 벡터를 입력으로 받아, 해당 벡터를 반시계방향으로 theta 만큼 회전하는 기능을 구현하기
+ 변환인가? : 기능을 적용하더라도 그대로 벡터 OK
+ 반시계 방향 : 선형인가 OK
+ 입력 2차원, 출력 2차원 : 2 x 2 표준행렬 구성하기
   + x축 기저는 (1,0), y축 기저는(0,1)
   + x축 기저에 대한 반시계방향 후 출력은 (cosθ, sinθ)이며, y축 기저에 대한 반시계방향 후 출력은 (-sinθ, cosθ)임
   + 따라서 2 x 2 표준 행렬은 다음과 같다.   
   
     <img src="https://latex.codecogs.com/gif.latex?A_{2\times&space;2}=\begin{bmatrix}&space;cos\theta&space;&&space;-sin\theta\\&space;sin\theta&space;&&space;cos\theta&space;\end{bmatrix}" title="A_{2\times 2}=\begin{bmatrix} cos\theta & -sin\theta\\ sin\theta & cos\theta \end{bmatrix}" />   


