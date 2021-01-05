# 결정이론(Decision Theory)

+ 새로운 값 <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}" title="\mathbf{x}" />가 주어졌을 때, 확률모델 <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x},&space;\mathbf{t})" title="p(\mathbf{x}, \mathbf{t})" />에 기반해서 최적의 결정을 내리는 것

   + 추론단계 : 결합확률분포 <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x},&space;C_{k})" title="p(\mathbf{x}, C_{k})" />를 구하는 것 
      > <img src="https://latex.codecogs.com/gif.latex?p(C_{k}|\mathbf{x})" title="p(C_{k}|\mathbf{x})" /> 를 직접 구하는 경우도 있음.   
      
   + 결정단계 : 상황에 대한 확률이 주어졌을 때, 어떻게 최적의 결정을 내릴것인가? (추론단계를 거쳤다면 결정단계는 매우 쉽다!)
   
   + 예제) X-Ray의 이미지로 암 판별
      + <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}" title="\mathbf{x}" /> : X-Ray 이미지
      + <img src="https://latex.codecogs.com/gif.latex?C_{1}" title="C_{1}" /> : 암인 경우
      + <img src="https://latex.codecogs.com/gif.latex?C_{2}" title="C_{2}" /> : 암이 아닌 경우
      + <img src="https://latex.codecogs.com/gif.latex?p(C_{k}|\mathbf{x})" title="p(C_{k}|\mathbf{x})" /> 를 통해 암 판별
         > <img src="https://latex.codecogs.com/gif.latex?p(C_{k}|\mathbf{x})&space;=&space;\frac{p(\mathbf{x},&space;C_{k})}{p(\mathbf{x})}&space;=&space;\frac{p(\mathbf{x},&space;C_{k})}{\sum_{k=1}^{2}&space;p(\mathbf{x},&space;C_{k})}=\frac{p(\mathbf{x},&space;C_{k})&space;p(C_{k})}{p(\mathbf{x})}" title="p(C_{k}|\mathbf{x}) = \frac{p(\mathbf{x}, C_{k})}{p(\mathbf{x})} = \frac{p(\mathbf{x}, C_{k})}{\sum_{k=1}^{2} p(\mathbf{x}, C_{k})}=\frac{p(\mathbf{x}, C_{k}) p(C_{k})}{p(\mathbf{x})}" />   
         
         > ∝ 우도(likelihood) X 사전확률(prior)
      + 직관적으로 볼 때, <img src="https://latex.codecogs.com/gif.latex?p(C_{k}|\mathbf{x})" title="p(C_{k}|\mathbf{x})" />를 **최대화시키는 k를 구하는 것** 이 좋은 결정   
      
## 이진분류(Binary Classification)
+ 결정영역 (decision region)   
   
   > <img src="https://latex.codecogs.com/gif.latex?\mathit{R}_{i}=\left&space;\{&space;x&space;:&space;\mathbf{pred}(x)=C_{i}&space;\right&space;\}" title="\mathit{R}_{i}=\left \{ x : \mathbf{pred}(x)=C_{i} \right \}" />   
      
+ 분류오류확률(probability of misclassification)   
   
   > 두가지 class에 대해   
    
   > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{mis})=p(x\in&space;\mathit{R}_{1},&space;C_{2})&space;&plus;&space;p(x\in&space;\mathit{R}_{2},&space;C_{1})=\int_{\mathit{R}_{1}}^{}p(x,&space;C_{2})dx&space;&plus;\int_{\mathit{R}_{2}}^{}&space;p(x,&space;C_{1})dx" title="p(\mathbf{mis})=p(x\in \mathit{R}_{1}, C_{2}) + p(x\in \mathit{R}_{2}, C_{1})=\int_{\mathit{R}_{1}}^{}p(x, C_{2})dx +\int_{\mathit{R}_{2}}^{} p(x, C_{1})dx" />   
      
+ 오류를 최소화하려면...
   + 다음 조건을 만족하면 x를 R1에 할당해야함   
      
      > <img src="https://latex.codecogs.com/gif.latex?p(x,&space;C_{1})>p(x,&space;C_{2})" title="p(x, C_{1})>p(x, C_{2})" />   
         
      > <img src="https://latex.codecogs.com/gif.latex?\Leftrightarrow&space;p(C_{1}|x)p(x)>p(C_{2}|x)p(x)" title="\Leftrightarrow p(C_{1}|x)p(x)>p(C_{2}|x)p(x)" />   
         
      > <img src="https://latex.codecogs.com/gif.latex?\Leftrightarrow&space;p(C_{1}|x)>p(C_{2}|x)" title="\Leftrightarrow p(C_{1}|x)>p(C_{2}|x)" />   
         
         
   + 조건이 반대일때는 x를 R2에 할당해야함   
      
      > <img src="https://latex.codecogs.com/gif.latex?p(x,&space;C_{1})<p(x,&space;C_{2})" title="p(x, C_{1})<p(x, C_{2})" />   
         
      > <img src="https://latex.codecogs.com/gif.latex?\Leftrightarrow&space;p(C_{1}|x)p(x)<p(C_{2}|x)p(x)" title="\Leftrightarrow p(C_{1}|x)p(x)<p(C_{2}|x)p(x)" />   
         
      > <img src="https://latex.codecogs.com/gif.latex?\Leftrightarrow&space;p(C_{1}|x)<p(C_{2}|x)" title="\Leftrightarrow p(C_{1}|x)<p(C_{2}|x)" />   
         
+ Multiclass 일 경우(일반화) 
 
   >  <img src="https://latex.codecogs.com/gif.latex?p(\textup{correct})=\sum_{k=1}^{K}&space;p(\mathbf{x}\in&space;R_{k},&space;C_{k})=\sum_{k=1}^{K}\int_{R_{k}}^{}&space;p(\mathbf{x},&space;C_{k})dx" title="p(\textup{correct})=\sum_{k=1}^{K} p(\mathbf{x}\in R_{k}, C_{k})=\sum_{k=1}^{K}\int_{R_{k}}^{} p(\mathbf{x}, C_{k})dx" />   
    
   > <img src="https://latex.codecogs.com/gif.latex?\mathbf{pred(}x\mathbf{)=argmax}_{k}&space;p(C_{k}|x)" title="\mathbf{pred(}x\mathbf{)=argmax}_{k} p(C_{k}|x)" />   
    
- - - - - - - - - - - - - - - - - - - - -
### 결정이론의 목표(분류의 경우) ✨
+ 결합확률분포 <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x},&space;C_{k})" title="p(\mathbf{x}, C_{k})" /> 가 주어졌을 때 최적의 결정영역들 <img src="https://latex.codecogs.com/gif.latex?R_{1},&space;...&space;,&space;R_{K}" title="R_{1}, ... , R_{K}" />를 찾는 것 !
   
+ <img src="https://latex.codecogs.com/gif.latex?\hat{C}(\mathbf{x})" title="\hat{C}(\mathbf{x})" /> : <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}" title="\mathbf{x}" />가 주어졌을 때 예측값(1, ..., K 중의 값)을 돌려주는 함수
   
   > <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}&space;\in&space;R_{j}&space;\Leftrightarrow&space;\hat{C}(\mathbf{x})=j" title="\mathbf{x} \in R_{j} \Leftrightarrow \hat{C}(\mathbf{x})=j" />
      
   > 즉, 결합확률분포 <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x},&space;C_{k})" title="p(\mathbf{x}, C_{k})" /> 가 주어졌을 때 최적의 함수 <img src="https://latex.codecogs.com/gif.latex?\hat{C}(\mathbf{x})" title="\hat{C}(\mathbf{x})" />를 찾는 것 ❗

   + **"최적의 함수"** 는 어떤 기준으로 ?  
 
#### 기대손실 최소화(Minimizing the Expected loss)
+ 모든 결정이 동일한 리스크를 갖는 건 X 
   + 암이 아닌데 암인 것으로 진단 
   + 암인데 암이 아닌 것으로 진단 : 큰 리스크를 가짐

+ 결정에 따른 리스크를 정량화 시켜서 표현 → **손실 행렬(loss matrix)**
   + <img src="https://latex.codecogs.com/gif.latex?L_{k,j}" title="L_{k,j}" /> : <img src="https://latex.codecogs.com/gif.latex?C_{k}" title="C_{k}" />에 속하는 <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}" title="\mathbf{x}" />를 <img src="https://latex.codecogs.com/gif.latex?C_{j}" title="C_{j}" />로 분류할 때 발생하는 손실(비용)
   
   + 데이터에 대한 모든 지식이 확률분포로 표현됨
   + 우리가 관찰할 수 있는 샘플(암을 가진 환자의 x-Ray 이미지)은 확률분포 p(x,Ck)를 통해 생성된 것
   + 손실행렬이 주어졌을 때, 다음과 같은 기대손실을 최소화하는 것을 목표 ❗
   
      > <img src="https://latex.codecogs.com/gif.latex?E[L]=\sum_{k}&space;\sum_{j}&space;\int&space;_{R_{j}}&space;L_{k,j}p(\mathbf{x},C_{k})d&space;\mathbf{x}" title="E[L]=\sum_{k} \sum_{j} \int _{R_{j}} L_{k,j}p(\mathbf{x},C_{k})d \mathbf{x}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?\int&space;_{\chi}&space;\sum_{k=1}^{K}&space;L_{k\hat{C}(\mathbf{x})}&space;p(\mathbf{x},&space;C_{k})d&space;\mathbf{x}=\int&space;_{\chi}&space;\left&space;(&space;\sum_{k=1}^{K}&space;L_{k\hat{C}&space;(\mathbf{x})}&space;p(&space;C_{k}|\mathbf{x})&space;\right&space;)p(\mathbf{x})d&space;\mathbf{x}" title="\int _{\chi} \sum_{k=1}^{K} L_{k\hat{C}(\mathbf{x})} p(\mathbf{x}, C_{k})d \mathbf{x}=\int _{\chi} \left ( \sum_{k=1}^{K} L_{k\hat{C} (\mathbf{x})} p( C_{k}|\mathbf{x}) \right )p(\mathbf{x})d \mathbf{x}" />   
      
      + 이는 <img src="https://latex.codecogs.com/gif.latex?\hat{C}(\mathbf{x})" title="\hat{C}(\mathbf{x})" />의 범함수(function)이고, 이를 최소화 시키는 함수 <img src="https://latex.codecogs.com/gif.latex?\hat{C}(\mathbf{x})" title="\hat{C}(\mathbf{x})" />를 찾으면 됨.
      
         > <img src="https://latex.codecogs.com/gif.latex?\hat{C}(\mathbf{x})=\mathbf{&space;argmin}_{j}&space;\sum_{k=1}^{K}&space;L_{kj}p(C_{k}|\mathbf{x})" title="\hat{C}(\mathbf{x})=\mathbf{ argmin}_{j} \sum_{k=1}^{K} L_{kj}p(C_{k}|\mathbf{x})" />   
      
      + 만약 손실행렬이 0-1 loss인 경우 (주대각선 원소들은 0 나머지 1)
      
         > <img src="https://latex.codecogs.com/gif.latex?\hat{C}(\mathbf{x})=\mathbf{&space;argmin}_{j}&space;1&space;-&space;p(C_{k}|\mathbf{x})&space;=&space;\mathbf{&space;argmin}_{j}&space;p(C_{k}|\mathbf{x})" title="\hat{C}(\mathbf{x})=\mathbf{ argmin}_{j} 1 - p(C_{k}|\mathbf{x}) = \mathbf{ argmin}_{j} p(C_{k}|\mathbf{x})" />   
      
      
   
+ 예제) 의료진단
   > <img src="https://latex.codecogs.com/gif.latex?C_{k}&space;\in&space;\left&space;\{&space;1,2&space;\right&space;\}&space;\Leftrightarrow&space;\left&space;\{&space;sick,&space;healthy&space;\right&space;\}" title="C_{k} \in \left \{ 1,2 \right \} \Leftrightarrow \left \{ sick, healthy \right \}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?L=\begin{bmatrix}&space;0&space;&&space;100&space;\\&space;1&space;&&space;0&space;\end{bmatrix}" title="L=\begin{bmatrix} 0 & 100 \\ 1 & 0 \end{bmatrix}" />   
   
   + 이 경우, 기대 손실은 다음과 같다.
   
   > <img src="https://latex.codecogs.com/gif.latex?E[L]=\int&space;_{R_{2}}&space;L_{1,2}&space;p(\mathbf{x},&space;C_{1})d&space;\mathbf{x}&space;&plus;&space;\int&space;_{R_{1}}&space;L_{2,1}&space;p(\mathbf{x},&space;C_{2})d&space;\mathbf{x}" title="E[L]=\int _{R_{2}} L_{1,2} p(\mathbf{x}, C_{1})d \mathbf{x} + \int _{R_{1}} L_{2,1} p(\mathbf{x}, C_{2})d \mathbf{x}" />   
   
   > <img src="https://latex.codecogs.com/gif.latex?=\int&space;_{R_{2}}&space;100&space;p(\mathbf{x},&space;C_{1})d&space;\mathbf{x}&space;&plus;&space;\int&space;_{R_{1}}&space;p(\mathbf{x},&space;C_{2})d&space;\mathbf{x}" title="=\int _{R_{2}} 100 p(\mathbf{x}, C_{1})d \mathbf{x} + \int _{R_{1}} p(\mathbf{x}, C_{2})d \mathbf{x}" />   
   
   + 위에서 설명한 <img src="https://latex.codecogs.com/gif.latex?\sum_{k=1}^{K}&space;L_{kj}p(C_{k}|\mathbf{x})" title="\sum_{k=1}^{K} L_{kj}p(C_{k}|\mathbf{x})" /> 을 계산해보면
   
      > <img src="https://latex.codecogs.com/gif.latex?j=1,&space;\sum_{k=1}^{K}L_{k,1}&space;p(C_{k}|\mathbf{x})=L_{11}p(C_{1}|\mathbf{x})&plus;L_{21}p(C_{2}|\mathbf{x})=p(C_{2}|\mathbf{x})" title="j=1, \sum_{k=1}^{K}L_{k,1} p(C_{k}|\mathbf{x})=L_{11}p(C_{1}|\mathbf{x})+L_{21}p(C_{2}|\mathbf{x})=p(C_{2}|\mathbf{x})" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?j=2,&space;\sum_{k=1}^{K}L_{k,2}&space;p(C_{k}|\mathbf{x})=L_{12}p(C_{1}|\mathbf{x})&plus;L_{22}p(C_{2}|\mathbf{x})=100p(C_{1}|\mathbf{x})" title="j=2, \sum_{k=1}^{K}L_{k,2} p(C_{k}|\mathbf{x})=L_{12}p(C_{1}|\mathbf{x})+L_{22}p(C_{2}|\mathbf{x})=100p(C_{1}|\mathbf{x})" />   
      
      + 두 결과값을 비교를 통해 판단   
      
         + <img src="https://latex.codecogs.com/gif.latex?100p(C_{1}|\mathbf{x})<p(C_{2}|\mathbf{x})" title="100p(C_{1}|\mathbf{x})<p(C_{2}|\mathbf{x})" />라면 건강하다 !
         
         + 안전한 진단을 위해서는 손실 행렬을 모델안에 포함시켜서 결정 !
         
### 결정이론의 목표(회귀의 경우) ✨
+ 목표값 <img src="https://latex.codecogs.com/gif.latex?t&space;\in&space;R" title="t \in R" />   
+ 손실함수   

   > <img src="https://latex.codecogs.com/gif.latex?L(t,&space;y(\mathbf{x}))=\left&space;\{&space;y(\mathbf{x}-t)&space;\right&space;\}^{2}" title="L(t, y(\mathbf{x}))=\left \{ y(\mathbf{x}-t) \right \}^{2}" />

   + 손실함수의 기댓값   
   
      > <img src="https://latex.codecogs.com/gif.latex?F[y]=E[L]=\int_{R}&space;\int_{\chi&space;}&space;\left&space;\{&space;y(\mathbf{x}-t)&space;\right&space;\}^{2}p(\mathbf{x},&space;t)d\mathbf{x}dt" title="F[y]=E[L]=\int_{R} \int_{\chi } \left \{ y(\mathbf{x}-t) \right \}^{2}p(\mathbf{x}, t)d\mathbf{x}dt" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?=\int_{\chi}&space;\left&space;(&space;\int_{R}&space;\left&space;\{&space;y(\mathbf{x}-t)&space;\right&space;\}^{2}p(\mathbf{x},&space;t)dt&space;\right&space;)d\mathbf{x}" title="=\int_{\chi} \left ( \int_{R} \left \{ y(\mathbf{x}-t) \right \}^{2}p(\mathbf{x}, t)dt \right )d\mathbf{x}" />   
      
      > <img src="https://latex.codecogs.com/gif.latex?=\int_{\chi}&space;\left&space;(&space;\int_{R}&space;\left&space;\{&space;y(\mathbf{x}-t)&space;\right&space;\}^{2}p(t|\mathbf{x})dt&space;\right&space;)p(\mathbf{x})d\mathbf{x}" title="=\int_{\chi} \left ( \int_{R} \left \{ y(\mathbf{x}-t) \right \}^{2}p(t|\mathbf{x})dt \right )p(\mathbf{x})d\mathbf{x}" />   
      
   + 손실 함수의 기댓값을 최소화시키는 예측값은?   
   
      + 최적의 예측 값은 <img src="https://latex.codecogs.com/gif.latex?y(\mathbf{x})=E_{t}[t|x]" title="y(\mathbf{x})=E_{t}[t|x]" />
      + 범함수(functional)의 최솟값을 구하는 방법을 통해 구함   
      
         + Euler-Lagrange Equation   
      
            > <img src="https://latex.codecogs.com/gif.latex?F[y]=\int_{a}^{b}&space;G(x,y(x),&space;y'(x))dx" title="F[y]=\int_{a}^{b} G(x,y(x), y'(x))dx" />   
            
            > <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;F}{\partial&space;y(x)}=\frac{\partial&space;G}{\partial&space;y}-\frac{\mathrm{d}&space;}{\mathrm{d}&space;x}&space;\frac{\partial&space;G}{\partial&space;y'}" title="\frac{\partial F}{\partial y(x)}=\frac{\partial G}{\partial y}-\frac{\mathrm{d} }{\mathrm{d} x} \frac{\partial G}{\partial y'}" />   
            
       + Euler-Lagrange Equation을 통해 회귀의 경우  
            
          > <img src="https://latex.codecogs.com/gif.latex?F[y]=E[L]=\int&space;\int&space;\left&space;\{&space;y(x)-t&space;\right&space;\}^{2}p(x,t)dxdt=\int&space;\left&space;(&space;\int&space;\left&space;\{&space;y(x)-t&space;\right&space;\}^{2}&space;p(x,t)dt&space;\right&space;)dx" title="F[y]=E[L]=\int \int \left \{ y(x)-t \right \}^{2}p(x,t)dxdt=\int \left ( \int \left \{ y(x)-t \right \}^{2} p(x,t)dt \right )dx" />   
               
          > <img src="https://latex.codecogs.com/gif.latex?G=\left&space;(&space;\int_{R}&space;\left&space;\{&space;y(\mathbf{x}-t)&space;\right&space;\}^{2}&space;p(t|\mathbf{x})dt&space;\right&space;)p(\mathbf{x})" title="G=\left ( \int_{R} \left \{ y(\mathbf{x}-t) \right \}^{2} p(t|\mathbf{x})dt \right )p(\mathbf{x})" />
             
          > <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;G}{\partial&space;y}=p(\mathbf{x})\frac{\partial&space;}{\partial&space;y}\left&space;(&space;\int_{R}&space;\left&space;\{&space;y(\mathbf{x}-t)&space;\right&space;\}^{2}&space;p(t|\mathbf{x})dt&space;\right&space;)" title="\frac{\partial G}{\partial y}=p(\mathbf{x})\frac{\partial }{\partial y}\left ( \int_{R} \left \{ y(\mathbf{x}-t) \right \}^{2} p(t|\mathbf{x})dt \right )" />
             
          > <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;G}{\partial&space;y}=0&space;\Rightarrow&space;\frac{\partial&space;}{\partial&space;y}\left&space;(&space;\int_{R}&space;\left&space;\{&space;y(\mathbf{x}-t)&space;\right&space;\}^{2}&space;p(t|\mathbf{x})dt&space;\right&space;)=0" title="\frac{\partial G}{\partial y}=0 \Rightarrow \frac{\partial }{\partial y}\left ( \int_{R} \left \{ y(\mathbf{x}-t) \right \}^{2} p(t|\mathbf{x})dt \right )=0" />
             
          > <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;y}\left&space;(&space;\int_{R}&space;\left&space;\{&space;y(\mathbf{x}-t)&space;\right&space;\}^{2}&space;p(t|\mathbf{x})dt&space;\right&space;)=\frac{\partial&space;}{\partial&space;y}\left&space;(&space;y(\mathbf{x})^{2}\int_{R}&space;p(t|\mathbf{x})dt&space;&plus;2y(\mathbf{x})\int_{R}tp(t|\mathbf{x})dt&plus;\int_{R}t^{2}p(t|\mathbf{x})dt&space;\right&space;)" title="\frac{\partial }{\partial y}\left ( \int_{R} \left \{ y(\mathbf{x}-t) \right \}^{2} p(t|\mathbf{x})dt \right )=\frac{\partial }{\partial y}\left ( y(\mathbf{x})^{2}\int_{R} p(t|\mathbf{x})dt +2y(\mathbf{x})\int_{R}tp(t|\mathbf{x})dt+\int_{R}t^{2}p(t|\mathbf{x})dt \right )" />
             
          > <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;}{\partial&space;y}\left&space;(&space;y(\mathbf{x})^{2}&space;&plus;2y(\mathbf{x})E_{t}[t|\mathbf{x}]&plus;\int_{R}t^{2}p(t|\mathbf{x})dt&space;\right&space;)" title="\frac{\partial }{\partial y}\left ( y(\mathbf{x})^{2} +2y(\mathbf{x})E_{t}[t|\mathbf{x}]+\int_{R}t^{2}p(t|\mathbf{x})dt \right )" />   
             
          > <img src="https://latex.codecogs.com/gif.latex?2y(\mathbf{x})&space;-2E_{t}[t|\mathbf{x}]=0" title="2y(\mathbf{x}) -2E_{t}[t|\mathbf{x}]=0" />   
             
          > <img src="https://latex.codecogs.com/gif.latex?\therefore&space;y(\mathbf{x})=E_{t}[t|\mathbf{x}]" title="\therefore y(\mathbf{x})=E_{t}[t|\mathbf{x}]" />  
             
             

   




