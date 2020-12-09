# 벡터
+ n-벡터 : 크기와 방향을 가진 물리량

- - - - - - - - - - - - - - - - - -
### 벡터의 표현
   + 좌표계 없이 표현
      + 벡터 v : 화살표로 표현
      + v의 크기 : 화살표의 길이
      + v의 방향 : 화살표의 방향
      
   + 좌표계 도입하여 표현   
      + 벡터 v => <img src="https://latex.codecogs.com/gif.latex?\mathbf{v}=\left&space;(&space;v_{1},&space;v_{2},&space;...,&space;v_{n}&space;\right&space;)" title="\mathbf{v}=\left ( v_{1}, v_{2}, ..., v_{n} \right )" />   
      + v의 크기 : <img src="https://latex.codecogs.com/gif.latex?\left&space;\|&space;\mathbf{v}&space;\right&space;\|=\sqrt{v_{1}^{2}&plus;v_{2}^{2}&plus;&space;...&space;&plus;&space;v_{n}^{2}}" title="\left \| \mathbf{v} \right \|=\sqrt{v_{1}^{2}+v_{2}^{2}+ ... + v_{n}^{2}}" />   
      + v의 방향 : <img src="https://latex.codecogs.com/gif.latex?\frac{1}{\left&space;\|&space;\mathbf{v}&space;\right&space;\|}\mathbf{v}" title="\frac{1}{\left \| \mathbf{v} \right \|}\mathbf{v}" />    
         
         
   + **벡터의 크기와 방향**   

   <img src="https://user-images.githubusercontent.com/72974863/101560022-b7554b80-3a05-11eb-9b2f-5e308966b7b5.png">   
   
   
- - - - - - - - - - - - - - - - - -
### 벡터의 내적
   + 좌표계 없이 표현
      + 두 n-벡터 길이를 갖는 u와 v의 내적 : <img src="https://latex.codecogs.com/gif.latex?\mathbf{u}\cdot&space;\mathbf{v}=\left&space;\|&space;\mathbf{u}&space;\right&space;\|\left&space;\|&space;\mathbf{v}&space;\right&space;\|cos\theta" title="\mathbf{u}\cdot \mathbf{v}=\left \| \mathbf{u} \right \|\left \| \mathbf{v} \right \|cos\theta" />   
      + 이때, θ는 두 벡터간의 사이각을 의미 
   + 좌표계 도입하여 표현
      + <img src="https://latex.codecogs.com/gif.latex?\mathbf{u}=\left&space;(&space;u_{1},&space;u_{2},&space;...,&space;u_{n}&space;\right&space;)" title="\mathbf{u}=\left ( u_{1}, u_{2}, ..., u_{n} \right )" />, <img src="https://latex.codecogs.com/gif.latex?\mathbf{v}=\left&space;(&space;v_{1},&space;v_{2},&space;...,&space;v_{n}&space;\right&space;)" title="\mathbf{v}=\left ( v_{1}, v_{2}, ..., v_{n} \right )" />의 좌표값을 통해 다음과 같이 계산됨.   
      
        <img src="https://latex.codecogs.com/gif.latex?\mathbf{u}\cdot&space;\mathbf{v}=u_{1}v_{1}&plus;u_{2}v_{2}&plus;&space;...&space;&plus;&space;u_{n}v_{n}" title="\mathbf{u}\cdot \mathbf{v}=u_{1}v_{1}+u_{2}v_{2}+ ... + u_{n}v_{n}" />   


   + **벡터 u와 벡터 v**   

     <img src="https://user-images.githubusercontent.com/72974863/101560824-7bbb8100-3a07-11eb-9cb2-79c7e560e4ca.png">   
      
      
   + 벡터의 내적이 0이면 두 벡터는 직교(orthogonal) : <img src="https://latex.codecogs.com/gif.latex?\mathbf{u}\cdot&space;\mathbf{v}=0&space;\Leftrightarrow&space;\mathbf{u}\perp&space;\mathbf{v}" title="\mathbf{u}\cdot \mathbf{v}=0 \Leftrightarrow \mathbf{u}\perp \mathbf{v}" />   
      + 물리에서 벡터 u의 방향으로의 전진은 벡터 v 방향에서 전혀 측정되지 x (그 반대도 마찬가지)
      + 고교 과정에서 배운 xy-좌표계나 xyz-좌표계가 직교 좌표계였음
 
 
- - - - - - - - - - - - - - - - - -
### 투영(projection)
   + 두 벡터 u, a가 있을 떄, 벡터 u를 a위에 투영한 벡터를 <img src="https://latex.codecogs.com/gif.latex?proj_{a}\mathbf{u}" title="proj_{a}\mathbf{u}" />이라 하고, 다음과 같이 구함.   

     <img src="https://latex.codecogs.com/gif.latex?proj_{a}\mathbf{u}=\left&space;(&space;\mathbf{u}\cdot&space;\frac{1}{||\mathbf{a}||}||\mathbf{a}||&space;\right&space;)\left&space;(&space;\frac{1}{||\mathbf{a}||}\mathbf{a}&space;\right&space;)=\left&space;(&space;\frac{\mathbf{u}\cdot&space;\mathbf{a}}{||\mathbf{a}||^{2}}&space;\right&space;)\mathbf{a}" title="proj_{a}\mathbf{u}=\left ( \mathbf{u}\cdot \frac{1}{||\mathbf{a}||}||\mathbf{a}|| \right )\left ( \frac{1}{||\mathbf{a}||}\mathbf{a} \right )=\left ( \frac{\mathbf{u}\cdot \mathbf{a}}{||\mathbf{a}||^{2}} \right )\mathbf{a}" />   

      + 이때, 길이 = <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;\mathbf{u}\cdot&space;\frac{1}{||\mathbf{a}||}||\mathbf{a}||&space;\right&space;)=\left&space;(&space;\frac{\mathbf{u}\cdot&space;\mathbf{a}}{||\mathbf{a}||}&space;\right&space;)" title="\left ( \mathbf{u}\cdot \frac{1}{||\mathbf{a}||}||\mathbf{a}|| \right )=\left ( \frac{\mathbf{u}\cdot \mathbf{a}}{||\mathbf{a}||} \right )" />   
   
      + 방향 = <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;\frac{1}{||\mathbf{a}||}\mathbf{a}&space;\right&space;)" title="\left ( \frac{1}{||\mathbf{a}||}\mathbf{a} \right )" />   
   
      + (기저 a에 대한 좌표값)a = <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;\frac{\mathbf{u}\cdot&space;\mathbf{a}}{||\mathbf{a}||^{2}}&space;\right&space;)\mathbf{a}" title="\left ( \frac{\mathbf{u}\cdot \mathbf{a}}{||\mathbf{a}||^{2}} \right )\mathbf{a}" />   
   
   + 벡터 u를 a위에 투영하고 남은 보완 벡터(complement vector)는 <img src="https://latex.codecogs.com/gif.latex?\mathbf{u}-proj_{a}\mathbf{u}" title="\mathbf{u}-proj_{a}\mathbf{u}" />임.   
   
   
   + **투영(projection) 벡터와 보완(complement) 벡터**   
   
     <img src="https://user-images.githubusercontent.com/72974863/101585777-cf3bc800-3a23-11eb-9ce3-03cb73facd9b.png">   
   
   + 두 벡터 u,a가 있을 때, **투영과 보완** 의 개념을 통해 **직교분할 가능 O** 
      + 투영 벡터와 보완 벡터는 서로 직교함.   

- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# 직교 행렬(Orthogonal Matrix)

+ 직교행렬(orthogonal matrix) : 주어진 행렬의 모든 열벡터가 서로 직교하는 행렬, 이는 직교좌표계를 의미   
+ 정규직교행렬(orthonormal matrix) : 주어진 행렬이 직교행렬이고, 모든 열벡터의 크기가 1인 행렬, 이는 정규직교좌표계를 의미   



