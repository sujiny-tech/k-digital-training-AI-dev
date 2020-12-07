# 선형 시스템(linear system)
+ 선형시스템(linear system) 문제 = 중등 교과과정에서 배운 연립일차방정식
+ ex) 가장 간단한 형태의 선형 시스템 : <img src="https://latex.codecogs.com/gif.latex?3x=6" title="3x=6" />   
+ 식이 많아지고, 미지수가 많아지면?
   > 중등과정에서 배웠던 소거법으로는 해를 찾는데에 손으로 직접 풀기 힘들다.   
   > 해를 찾는 과정이 복잡해진다.
   
+ 선형 대수(linear algebra)의 목표
   > 어떤 연립일차방정식(선형 시스템) 문제라도 정형적인 방법으로 표현하고 해결하는 방법을 배우는 것

+ <math>m x n</math> 선형 시스템 구성 요소
   + <math>m</math>개의 선형 방정식(Linear Equations) : 선의 형태, 미지수의 최고차항의 차수가 1인 일차 방정식
   + <math>n</math>개의 미지수(unknowns)
      + 선형 시스템
         + ex 1) 2X3 선형시스템   
           <img src="https://latex.codecogs.com/gif.latex?E_{1}&space;:&space;3x&plus;y&plus;z=4" title="E_{1} : 3x+y+z=4" />   
           <img src="https://latex.codecogs.com/gif.latex?E_{2}&space;:&space;x-2y-z=1" title="E_{2} : x-2y-z=1" />   
         + ex 2) 1x2 선형시스템   
           <img src="https://latex.codecogs.com/gif.latex?E_{1}&space;:&space;2x&plus;y=5" title="E_{1} : 2x+y=5" />   
           
      + 비선혛 방정식(non-linear equation)
         > ex 1) <img src="https://latex.codecogs.com/gif.latex?sinx&plus;y=2" title="sinx+y=2" />     
         > ex 2) <img src="https://latex.codecogs.com/gif.latex?3x&plus;y^2=3" title="3x+y^2=3" />      
         > ex 3) <img src="https://latex.codecogs.com/gif.latex?8xy&plus;2z=5" title="8xy+2z=5" />      
         
   + Ax=b 꼴 표현(대수적 표현)
      + 예를 들어, 식이 3개고 미지수가 3인 선형시스템있다고 하자.  
         <a href="https://www.codecogs.com/eqnedit.php?latex=E_{1}&space;:&space;3x&plus;5y=2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_{1}&space;:&space;3x&plus;5y=2" title="E_{1} : 3x+5y=2" /></a>    
         <a href="https://www.codecogs.com/eqnedit.php?latex=E_{2}&space;:&space;x-5y=7" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_{2}&space;:&space;x-5y=7" title="E_{2} : x-5y=7" /></a>   
         <a href="https://www.codecogs.com/eqnedit.php?latex=E_{3}&space;:&space;5y&plus;3z=-1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E_{3}&space;:&space;5y&plus;3z=-1" title="E_{3} : 5y+3z=-1" /></a>         
      + 이를 Ax=b로 표현하면 다음과 같다.   
         <a href="https://www.codecogs.com/eqnedit.php?latex=\begin{bmatrix}&space;3&space;&&space;5&space;&&space;0\\&space;1&space;&&space;-5&space;&&space;0\\&space;0&space;&&space;5&space;&&space;3&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;3&space;&&space;5&space;&&space;0\\&space;1&space;&&space;-5&space;&&space;0\\&space;0&space;&&space;5&space;&&space;3&space;\end{bmatrix}" title="\begin{bmatrix} 3 & 5 & 0\\ 1 & -5 & 0\\ 0 & 5 & 3 \end{bmatrix}" /></a> <a href="https://www.codecogs.com/eqnedit.php?latex=\begin{bmatrix}&space;x\\&space;y\\&space;z&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;x\\&space;y\\&space;z&space;\end{bmatrix}" title="\begin{bmatrix} x\\ y\\ z \end{bmatrix}" /></a> <a href="https://www.codecogs.com/eqnedit.php?latex==&space;\begin{bmatrix}&space;2\\&space;4\\&space;-1&space;\end{bmatrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?=&space;\begin{bmatrix}&space;2\\&space;7\\&space;-1&space;\end{bmatrix}" title="= \begin{bmatrix} 2\\ 7\\ -1 \end{bmatrix}" /></a>   
   + m x n 선형시스템의 Ax=b 표현으로 정리하면,
      + 식은 행, 행은 식
      + m : 선형 방정식의 개수
      + n : 미지수 개수
      + A : m x n 행렬
      + x : n-벡터
      + b : m-벡터
      
## 선형시스템의 해(Solutions of a Linear System)
...
