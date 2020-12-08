# 선형 시스템(linear system)
+ 선형시스템(linear system) 문제 = 중등 교과과정에서 배운 __연립일차방정식__
+ ex) 가장 간단한 형태의 선형 시스템 : <img src="https://latex.codecogs.com/gif.latex?3x=6" title="3x=6" />   
+ 식이 많아지고, 미지수가 많아지면?
   > 중등과정에서 배웠던 소거법으로는 해를 찾는데에 손으로 직접 풀기 힘들다.   
   > 해를 찾는 과정이 복잡해진다.
   
+ 선형 대수(linear algebra)의 목표
   > 어떤 연립일차방정식(선형 시스템) 문제라도 정형적인 방법으로 표현하고 해결하는 방법을 배우는 것

+ m x n 선형 시스템 구성 요소
   + **m**개의 선형 방정식(Linear Equations) : 선의 형태, 미지수의 최고차항의 차수가 1인 일차 방정식
   + **n**개의 미지수(unknowns)
      + 선형 시스템
         + ex 1) 2X3 선형시스템 : 2개의 선형 방정식, 3개의 미지수   
           <img src="https://latex.codecogs.com/gif.latex?E_{1}&space;:&space;3x&plus;y&plus;z=4" title="E_{1} : 3x+y+z=4" />   
           <img src="https://latex.codecogs.com/gif.latex?E_{2}&space;:&space;x-2y-z=1" title="E_{2} : x-2y-z=1" />
           
         + ex 2) 1x2 선형시스템 : 1개의 선형 방정식, 2개의 미지수   
           <img src="https://latex.codecogs.com/gif.latex?E_{1}&space;:&space;2x&plus;y=5" title="E_{1} : 2x+y=5" />   
           
      + 비선형 방정식(non-linear equation)
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
      + **m** : 선형 방정식의 개수
      + **n** : 미지수 개수
      + **A** : m x n 행렬
      + **x** : n-벡터
      + **b** : m-벡터
            
## 선형시스템의 해(Solutions of a Linear System)
+ 가장 단순한 형태의 선형 시스템은 다음과 같다.   
   + <img src="https://latex.codecogs.com/gif.latex?ax=b" title="ax=b" /> (단, <img src="https://latex.codecogs.com/gif.latex?a,&space;b" title="a, b" />는 스칼라)   
   + 이 선형시스템의 해는 3가지의 경우에 따라 존재한다.
      + 해가 하나인 경우(unique solution)
         + ex) <img src="https://latex.codecogs.com/gif.latex?3x=6" title="3x=6" />   
      + 해가 없는 경우(no solution)
         + ex) <img src="https://latex.codecogs.com/gif.latex?0x=6" title="0x=6" />  
         + **a=0**일 때, **역수(inverse)가 존재하지 않으므로** a가 **특이(singular)** 하다고 한다.
      + 해가 여러개인 경우(infinitely many solutions)
         + ex) <img src="https://latex.codecogs.com/gif.latex?0x=0" title="0x=0" />   
   + 해가 있으면, 선형 시스템이 **consistent** 하며
   + 해가 없으면, 선형 시스템이 **inconsistent** 하다.

+ 대수적 표현 Ax=b에서의 해는 3가지 경우가 존재한다.
   + 해가 하나인 경우   
      ex) <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;1&space;&&space;3&space;\\&space;-2&space;&&space;1&space;\end{bmatrix}\begin{bmatrix}&space;x_{1}\\&space;x_{2}&space;\end{bmatrix}&space;=&space;\begin{bmatrix}&space;2\\&space;3&space;\end{bmatrix}" title="\begin{bmatrix} 1 & 3 \\ -2 & 1 \end{bmatrix}\begin{bmatrix} x_{1}\\ x_{2} \end{bmatrix} = \begin{bmatrix} 2\\ 3 \end{bmatrix}" />      
      > 이때, <img src="https://latex.codecogs.com/gif.latex?x_{1}=-1,&space;x_{2}=1" title="x_{1}=-1, x_{2}=1" /> 이다.   
      
   + 해가 없는 경우   
      ex) <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;1&space;&3&space;\\&space;2&space;&6&space;\end{bmatrix}\begin{bmatrix}&space;x_{1}\\&space;x_{2}&space;\end{bmatrix}=\begin{bmatrix}&space;2\\&space;5&space;\end{bmatrix}" title="\begin{bmatrix} 1 &3 \\ 2 &6 \end{bmatrix}\begin{bmatrix} x_{1}\\ x_{2} \end{bmatrix}=\begin{bmatrix} 2\\ 5 \end{bmatrix}" />
      > 이때, 행렬 A는 singular 하며, 역행렬이 존재하지 않음.
      > 두개의 식이 평행함
      
   + 해가 여러개인 경우   
      ex) <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;1&space;&3&space;\\&space;2&space;&6&space;\end{bmatrix}\begin{bmatrix}&space;x_{1}\\&space;x_{2}&space;\end{bmatrix}=\begin{bmatrix}&space;2\\&space;4&space;\end{bmatrix}" title="\begin{bmatrix} 1 &3 \\ 2 &6 \end{bmatrix}\begin{bmatrix} x_{1}\\ x_{2} \end{bmatrix}=\begin{bmatrix} 2\\ 4 \end{bmatrix}" />
      > 이때, 행렬 A는 singular 하며, 역행렬이 존재하지 않음.
      > 두개의 식이 완전히 겹침
      
+ 대수적 표현에서도 해가 있으면 선형 시스템이 **consistent** 하며, 반대로 해가 없으면, 선형 시스템이 **inconsistent** 하다.

---------------------------------------------------------------
