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
   
      > <img src="https://latex.codecogs.com/gif.latex?p(\mathbf{mis})=p(x\in&space;\mathit{R}_{1},&space;C_{2})&space;&plus;&space;p(x\in&space;\mathit{R}_{2},&space;C_{1})=\int_{\mathit{R}_{1}}^{}p(x,&space;C_{2})dx&space;&plus;\int_{\mathit{R}_{2}}^{}&space;p(x,&space;C_{1})dx" title="p(\mathbf{mis})=p(x\in \mathit{R}_{1}, C_{2}) + p(x\in \mathit{R}_{2}, C_{1})=\int_{\mathit{R}_{1}}^{}p(x, C_{2})dx +\int_{\mathit{R}_{2}}^{} p(x, C_{1})dx" />   
      
   + 오류를 최소화하려면
