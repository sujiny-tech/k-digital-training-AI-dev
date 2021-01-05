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
    
### 결정이론의 목표(분류의 경우) ✨
   + 결합확률분포 <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x},&space;C_{k})" title="p(\mathbf{x}, C_{k})" /> 가 주어졌을 때 최적의 결정영역들 <img src="https://latex.codecogs.com/gif.latex?R_{1},&space;...&space;,&space;R_{K}" title="R_{1}, ... , R_{K}" />를 찾는 것 !
   
   + <img src="https://latex.codecogs.com/gif.latex?\hat{C}(\mathbf{x})" title="\hat{C}(\mathbf{x})" /> : <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}" title="\mathbf{x}" />가 주어졌을 때 예측값(1, ..., K 중의 값)을 돌려주는 함수
   
      > <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}&space;\in&space;R_{j}&space;\Leftrightarrow&space;\hat{C}(\mathbf{x})=j" title="\mathbf{x} \in R_{j} \Leftrightarrow \hat{C}(\mathbf{x})=j" />
      
      > 즉, 결합확률분포 <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{x},&space;C_{k})" title="p(\mathbf{x}, C_{k})" /> 가 주어졌을 때 최적의 함수 <img src="https://latex.codecogs.com/gif.latex?\hat{C}(\mathbf{x})" title="\hat{C}(\mathbf{x})" />를 찾는 것 ❗

      + **"최적의 함수"** 는 어떤 기준으로 ?  
 
### 기대손실 최소화(Minimizing the Expected loss)
+ 모든 결정이 동일한 리스크를 갖는 건 X 
   + 암이 아닌데 암인 것으로 진단 
   + 암인데 암이 아닌 것으로 진단 : 큰 리스트를 가짐

+ 결정에 따른 리스크를 정량화 시켜서 표현 → **손실 행렬(loss matrix)**
   + <img src="https://latex.codecogs.com/gif.latex?L_{k,j}" title="L_{k,j}" /> : <img src="https://latex.codecogs.com/gif.latex?C_{k}" title="C_{k}" />에 속하는 <img src="https://latex.codecogs.com/gif.latex?\mathbf{x}" title="\mathbf{x}" />를 <img src="https://latex.codecogs.com/gif.latex?C_{j}" title="C_{j}" />로 분류할 때 발생하는 손실(비용)
   
   + 데이터에 대한 모든 지식이 확률분포로 표현됨
   + 우리가 관찰할 수 있는 샘플(암을 가진 환자의 x-Ray 이미지)은 확률분포 p(x,Ck)를 통해 생성된 것
   + 손실행렬이 주어졌을 때, 다음과 같은 기대손실을 최소화하는 것을 목표 ❗
   
      > <img src="https://latex.codecogs.com/gif.latex?E[L]=\sum_{k}&space;\sum_{j}&space;\int&space;_{R_{j}}&space;L_{k,j}p(\mathbf{x},C_{k})d&space;\mathbf{x}" title="E[L]=\sum_{k} \sum_{j} \int _{R_{j}} L_{k,j}p(\mathbf{x},C_{k})d \mathbf{x}" />   
      
      
   
   
   
   
   
