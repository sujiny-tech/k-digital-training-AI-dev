# 오류 역전파 알고리즘(Backpropagation algorithm)
> **출력의 오류를 역방향(왼쪽)으로 전파**하며 **경사도를 계산**하는 알고리즘

+ 목적함수의 정의
   + **특징 벡터 집합 X**과 **부류 벡터 집합 Y**(라벨)
   + 부류 벡터는 one-hot 코드로 표현됨
   + 설계 행렬로 쓰면,
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{X}=\begin{pmatrix}&space;\mathbf{x}_1^T\\&space;\mathbf{x}_2^T\\&space;...\\&space;\mathbf{x}_n^T&space;\end{pmatrix},&space;\mathbf{Y}=\begin{pmatrix}&space;\mathbf{y}_1^T\\&space;\mathbf{y}_2^T\\&space;...\\&space;\mathbf{y}_n^T&space;\end{pmatrix}" title="\mathbf{X}=\begin{pmatrix} \mathbf{x}_1^T\\ \mathbf{x}_2^T\\ ...\\ \mathbf{x}_n^T \end{pmatrix}, \mathbf{Y}=\begin{pmatrix} \mathbf{y}_1^T\\ \mathbf{y}_2^T\\ ...\\ \mathbf{y}_n^T \end{pmatrix}" />   
      
   + 기계 학습의 목표 : 모든 **샘플을 옳게 분류하는 함수 f**를 찾는 것 ⭐

   + 목적함수
      + **평균 제곱 오차**로 정의 (일반적으로)

+ 오류 역전파 알고리즘의 설계

   + 연산 그래프 (computational graph)
      > 계산 과정을 그래프로 나타낸 것
      
      + 장점
         + 역전파를 통해 미분을 효율적으로 계산할 수 있음 ⭐
      
   + 연쇄 법칙(chain rule)의 구현
      + **반복되는 부분식들**을 **저장**하거나 **재연산을 최소화**   
      
      
      > <img src="https://user-images.githubusercontent.com/72974863/105625123-50cba600-5e6a-11eb-94d4-9082b6ccdc8b.png">   
      
      > [이미지 출처✨](http://blog.daum.net/biuea1/18)   
      
      + 덧셈과 곱셈에 대한 역전파 
         > [아래의 이미지 출처 : 다른사람 블로그 & Deep Learning from Scratch (책) ✨](https://codingneedsinsanity.tistory.com/24)
      
         + 덧셈
            > <img src="https://user-images.githubusercontent.com/72974863/105625517-3941ec80-5e6d-11eb-9dec-8a1a64e40122.png">   
         
         + 곱셈 
            > <img src="https://user-images.githubusercontent.com/72974863/105625538-4fe84380-5e6d-11eb-84c2-f8414c21f58b.png">   
         
         + 활성화 함수 계층 
            + ReLU 계층
               > <img src="https://user-images.githubusercontent.com/72974863/105625614-d0a73f80-5e6d-11eb-964f-dc6e61e9555e.png">   
               
               > 0보다 같거나 작은 경우엔 0
               

            + Sigmoid 계층
               > <img src="https://user-images.githubusercontent.com/72974863/105625577-9a69c000-5e6d-11eb-958b-73617ab6dff0.png">   
               
               > sigmoid의 경우, 입력과 출력만으로 계산 가능하다는 것을 볼 수 있음.
               
               > <img src="https://user-images.githubusercontent.com/72974863/105625752-a1450280-5e6e-11eb-8e5f-06712025b4ee.png" width="50%" height="50%">   
               
               > 위를 통해 사실 sigmoid 계층의 역전파는 순전파의 출력(y)만으로 계산 가능 ❗   
               
               
    
    
> ✔ 강의를 통해 신경망의 back-prop을 보았고, 스칼라부터 벡터, 텐서버전, 미니배치단위까지 확인하였음 ⭐     

> ✔ 예전에 책을 통해 공부했었지만, 다시 공부해야할 필요성을 느껴 조만간 책을 다시 볼 계획 ⭐
