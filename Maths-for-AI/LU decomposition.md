# 행렬 분해(matrix decomposition)
+ 숫자에서의 분해...
    + 숫자의 인수분해는 주어진 숫자를 여러 숫자의 곱으로 분해해서 표현하는 것
    + 인수분해한 상태로 숫자를 가지면, 여러모로 계산이 편해지는 경우 多
    
+ 행렬에서도 분해하면, 여러모로 계산이 편해지는 경우가 多
+ 대표적인 행렬 분해(matrix decomposition)는 다음과 같다. 
   + LU 분해(LU decomposition)
   + QR 분해(QR decomposition)
   + 특이값 분해(SVD, Singular Value Decomposition)

   
# [LU 분해(LU decomposition)](https://ko.wikipedia.org/wiki/LU_%EB%B6%84%ED%95%B4)   
+ **LU 분해** : 주어진 행렬을 하/상 삼각행렬(Lower triangular/Upper triangular matrx)로 나누는 것
   + Ax=b 문제를 LU분해를 하면,   
      
     <img src="https://latex.codecogs.com/gif.latex?Ax=b&space;\Rightarrow&space;(LU)x=b" title="Ax=b \Rightarrow (LU)x=b" /> <img src="https://latex.codecogs.com/gif.latex?\Rightarrow&space;L(Ux)=b&space;\Rightarrow&space;Ly=b" title="\Rightarrow L(Ux)=b \Rightarrow Ly=b" />   (단, <img src="https://latex.codecogs.com/gif.latex?Ux=y" title="Ux=y" />)   
   + 전방대치법(Forward-substitution) : <img src="https://latex.codecogs.com/gif.latex?Ly=b" title="Ly=b" />에서 y 구하기
   + 후방대치법(Back-substitution) : <img src="https://latex.codecogs.com/gif.latex?Ux=y" title="Ux=y" />에서 x 구하기
   
+ LU 분해는 가우스 소거법의 전방대치법을 행렬로 코드화 한 것
   + <img src="https://latex.codecogs.com/gif.latex?L" title="L" /> : 행렬 A를 전방소거하는데 쓰인 replacement와 scaling에 대한 EROs를 기록해 둔 행렬
   + <img src="https://latex.codecogs.com/gif.latex?U" title="U" /> : 남은 upper triangular matrix
   + <img src="https://latex.codecogs.com/gif.latex?P" title="P" /> : interchange에 대한 EROs를 기록해 둔 행렬(옵션)   
          
     <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;a_{11}&space;&&space;a_{12}&space;&&space;a_{13}&space;\\&space;a_{21}&space;&&space;a_{22}&space;&&space;a_{23}&space;\\&space;a_{31}&space;&&space;a_{32}&space;&&space;a_{33}&space;\end{bmatrix}=\begin{bmatrix}&space;l_{11}&space;&&space;0&space;&&space;0&space;\\&space;l_{21}&space;&&space;l_{22}&space;&&space;0\\&space;l_{31}&space;&&space;l_{32}&space;&&space;l_{33}&space;\end{bmatrix}\begin{bmatrix}&space;u_{11}&space;&&space;u_{12}&space;&&space;u_{13}&space;\\&space;0&space;&&space;u_{22}&space;&&space;u_{23}\\&space;0&space;&&space;0&space;&&space;u_{33}&space;\end{bmatrix}" title="\begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix}=\begin{bmatrix} l_{11} & 0 & 0 \\ l_{21} & l_{22} & 0\\ l_{31} & l_{32} & l_{33} \end{bmatrix}\begin{bmatrix} u_{11} & u_{12} & u_{13} \\ 0 & u_{22} & u_{23}\\ 0 & 0 & u_{33} \end{bmatrix}" />   

+ **LU 분해를 왜 쓸까?** 
   + 수치적 안정성
      > Ax=b의 해인 역행렬 <img src="https://latex.codecogs.com/gif.latex?A^{-1}" title="A^{-1}" />를 직접 구하는 것보다 좀 더 수치적으로 안정적이여서   
      
   + <img src="https://latex.codecogs.com/gif.latex?b" title="b" /> **가 자주 업데이트 되는 경우**
      > 이런 경우에는 행렬 <img src="https://latex.codecogs.com/gif.latex?A" title="A" />를 <img src="https://latex.codecogs.com/gif.latex?PLU" title="PLU" />로 미리 분해해두면 <img src="https://latex.codecogs.com/gif.latex?A^{-1}" title="A^{-1}" />가 업데이트될 때마다 선형시스템의 해를 실시간으로 구할 수 있어서
      
