# 가우스 소거법(Gauss elimination)

+ m x n 선형시스템의 해를 구하는 가장 대표적인 방법
   + **전방 소거법(Forward elimination)** : 주어진 선형시스템을 아래로 갈수록 더 단순한 형태의 선형 방정식을 가지도록 변형한다.
      + 이를 통해 나온 행렬 A의 형태는 역삼각형 모형으로 숫자들이 채워있음(즉, 역삼각형 외의 부분에 0으로 바뀌게 됨) 
      + 따라서, 마지막행은 가장 단순한 형태의 선형방정식이 나오게 됨   
              
   + **후방 대입법(back-substitution)** : 아래에서부터 위로 미지수를 실제값으로 대체한다.   
    
     <img src="https://latex.codecogs.com/gif.latex?\begin{bmatrix}&space;1&space;&&space;*&space;&&space;*\\&space;0&space;&&space;1&space;&&space;*\\&space;0&space;&&space;0&space;&&space;1&space;\end{bmatrix}\begin{bmatrix}&space;x\\&space;y\\&space;z&space;\end{bmatrix}&space;=\begin{bmatrix}&space;*\\&space;*\\&space;*&space;\end{bmatrix}&space;\Rightarrow&space;\left\{\begin{matrix}&space;x&plus;*y&plus;*z=*\\&space;y&plus;*z=*\\&space;z=*&space;\end{matrix}\right." title="\begin{bmatrix} 1 & * & *\\ 0 & 1 & *\\ 0 & 0 & 1 \end{bmatrix}\begin{bmatrix} x\\ y\\ z \end{bmatrix} =\begin{bmatrix} *\\ *\\ * \end{bmatrix} \Rightarrow \left\{\begin{matrix} x+*y+*z=*\\ y+*z=*\\ z=* \end{matrix}\right." />   
        
        
+ 소거법에 쓰이는 **기본행연산**(EROs; Elementary Row Operations)

   + 치환(Replacement) : <img src="https://latex.codecogs.com/gif.latex?r_{j}\leftarrow&space;r_{j}-mr_{i}" title="r_{j}\leftarrow r_{j}-mr_{i}" />   
      + j번째 행을 i번째 행에 m배하여 빼서 업데이트수행
      
   + 교환(Interchange) : <img src="https://latex.codecogs.com/gif.latex?r_{j}\leftrightarrow&space;r_{i}" title="r_{j}\leftrightarrow r_{i}" />   
      + j번째 행과 i번째 행의 위치 서로 바꿔주기
      
   + 스케일링(Scaling) : <img src="https://latex.codecogs.com/gif.latex?r_{j}\leftarrow&space;sr_{j}" title="r_{j}\leftarrow sr_{j}" />   
      + j번째 행을 s배 스케일링 수행
   
-------------------   
+ **전방소거법(Forward Elimination)의 가치** :star2:
   + 주어진 선형 시스템을 가장 풀기 쉬운 꼴로 변형해줌
      + **upper triangular form(상삼각형태)** 로 바꿔줌
      
   + 주어진 선형시스템의 **rank(랭크)** 를 알려줌 (rank : 미지수 개수)
      
   + 선형시스템이 **해가 있는지(consistent)/없는지(inconsistent)** 알려줌
   
+ 이에 더 나아가, 대각 원소를 기준으로 위쪽 원소들도 0으로 바꾸어 계산하는 방법이 Gauss-Jordan elimination
#### ✔ [가우스 소거법-위키백과](https://ko.wikipedia.org/wiki/%EA%B0%80%EC%9A%B0%EC%8A%A4_%EC%86%8C%EA%B1%B0%EB%B2%95)
