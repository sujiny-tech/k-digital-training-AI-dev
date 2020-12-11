# 추정(Estimation)

## 모평균의 추정

+ 추정 : 표본을 통해 모집단의 특성이 어떠한지 추측하는 과정

+ 표본평균의 특성
   + 모집단이 정규분포인 경우, **표본평균** 사용(이를 통해 모평균 \mu의 추정)   
   + 대표본인 경우(n이 30이상인 경우), 중심극한정리에 의해 표본평균이 정규분포를 따른다고 가정   
   
+ 점 추정(Point Estimation)
   + 모집단의 값의 지점을 예측하는 점 추정(확률적인 근사치 예측)
   + 표본평균 = 모평균의 점추정값(추정량)
    ```python
    >>> import numpy as np
    >>> samples=[9,4,0,8,1,3,7,8,4,2]
    >>> print(np.mean(samples))
    4.6
    ```
    
+ 구간 추정(Interval Estimation)
   + 일정한 구간을 예측하는 방법 = (<img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />의 추정량) ± (추정량의 표준편차)   
   
   + 모평균의 <img src="https://latex.codecogs.com/gif.latex?100(1-\alpha&space;)%" title="100(1-\alpha )%" /> 신뢰구간(confidence interval)
      + 정규분포에서 <img src="https://latex.codecogs.com/gif.latex?\sigma" title="\sigma" />를 알 때,   
      
         + <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;\bar{x}-{z_{\frac{\alpha}{2}}}\frac{\sigma&space;}{\sqrt{n}}&space;,&space;\bar{x}&plus;{z_{\frac{\alpha}{2}}}\frac{\sigma&space;}{\sqrt{n}}\right&space;)" title="\left ( \bar{x}-{z_{\frac{\alpha}{2}}}\frac{\sigma }{\sqrt{n}} , \bar{x}+{z_{\frac{\alpha}{2}}}\frac{\sigma }{\sqrt{n}}\right )" />   
         
         + 정규분포가 아니거나, 표준편차가 알려지지 않은 경우에는 X
         
      + 표본의 크기가 클때 **중심극한 정리** 사용   
   
         + <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;\bar{x}-{z_{\frac{\alpha}{2}}}\frac{s&space;}{\sqrt{n}}&space;,&space;\bar{x}&plus;{z_{\frac{\alpha}{2}}}\frac{s&space;}{\sqrt{n}}\right&space;)" title="\left ( \bar{x}-{z_{\frac{\alpha}{2}}}\frac{s }{\sqrt{n}} , \bar{x}+{z_{\frac{\alpha}{2}}}\frac{s }{\sqrt{n}}\right )" />   
      
         + s : 표본 표준편차   
              
   + 예) 어떤 학교의 고1 남학생의 평균키를 추정하기 위해 36명을 표본으로 추출하여 그 표본평균과 표본표준편차를 계산하여 그 결과가 아래와 같다.   
      + <img src="https://latex.codecogs.com/gif.latex?\bar{x}=173.6,&space;s=3.6" title="\bar{x}=173.6, s=3.6" />   
      + 평균키에 대한 95% 신뢰구간은?   
      
         + sol) <img src="https://latex.codecogs.com/gif.latex?\alpha&space;=0.05" title="\alpha =0.05" />   
         
            <img src="https://latex.codecogs.com/gif.latex?z_{\frac{\alpha}{2}}=z_{0.025}=1.96" title="z_{\frac{\alpha}{2}}=z_{0.025}=1.96" />    
             
              > using 표준정규분포표   
            
            <img src="https://latex.codecogs.com/gif.latex?z_{\frac{\alpha}{2}}\frac{s}{\sqrt{n}}=1.96\times&space;\frac{3.6}{\sqrt{36})}=1.176" title="z_{\frac{\alpha}{2}}\frac{s}{\sqrt{n}}=1.96\times \frac{3.6}{\sqrt{36})}=1.176" />   
            
            + 따라서, 173.6(mu 추정량)±1.176(추정량의 표준편차)=(172.4, 174.8)  
            
               > 이 구간안에 mu(모평균)가 있을 확률이 95%이다.   
               
   + 예) 어떤 농장에서 생산된 계란 30개의 표본을 뽑았더니 그 무게는 다음과 같다.   
      + w=[10.7, 11.7, 9.8, 11.4, 10.8, 9.9, 10.1, 8.8, 12.2, 11.0, 11.3, 11.1, 10.3, 10.0, 9.9, 11.1, 11.7, 11.5, 9.1, 10.3, 8.6, 12.1, 10.0, 13.0, 9.2, 9.8, 9.3, 9.4, 9.6, 9.2]
      + 계란의 평균무게에 대한 95% 신뢰 구간을 구하시오.   
      
         <img src="https://user-images.githubusercontent.com/72974863/101874929-1dd89600-3bcd-11eb-8918-8cb3a6f27562.png" width="60%" hegiht="60%">   
         


               
## 모비율의 추정
+ 점 추정
   + 확률변수 X : **n개의 표본에서 특정 속성을 갖는 표본의 개수**
   + 모비율 p의 점 추정량   
   
      <img src="https://latex.codecogs.com/gif.latex?\hat{p}=\frac{X}{n}" title="\hat{p}=\frac{X}{n}" />   
      
   + 표본을 뽑을때마다 값이 달라지니까, 점추정량보다는 구간 추정이 많이 사용함 
   
   
+ 구간 추정
   + 모집단에서 특정 속성을 가지는 비율
   + n이 충분히 클 때, 근사적으로 정규분포를 따름   
   
      + <img src="https://latex.codecogs.com/gif.latex?n\hat&space;p>5,&space;n(1-\hat&space;p)>5" title="n\hat p>5, n(1-\hat p)>5" />일때 (대표본일때,)   
      
      + <img src="https://latex.codecogs.com/gif.latex?X\sim&space;N(np,&space;np(1-p))" title="X\sim N(np, np(1-p))" />   
      
   + 확률변수 X를 표준화시키면 근사적으로 표준정규분포를 따름   
   
      + <img src="https://latex.codecogs.com/gif.latex?Z=\frac{X-np}{\sqrt{n\hat&space;p(1-\hat&space;p)}}=\frac{\hat&space;p&space;-&space;p}{\sqrt{\frac{\hat&space;p(1-\hat&space;p)}{n}}}" title="Z=\frac{X-np}{\sqrt{n\hat p(1-\hat p)}}=\frac{\hat p - p}{\sqrt{\frac{\hat p(1-\hat p)}{n}}}" />   
      
      + <img src="https://latex.codecogs.com/gif.latex?P(|Z|\leq&space;z_{\alpha/2})=1-\alpha" title="P(|Z|\leq z_{\alpha/2})=1-\alpha" />임을 풀어쓰면,   
      
         <img src="https://latex.codecogs.com/gif.latex?P(-z_{\alpha/2}\leq&space;Z\leq&space;z_{\alpha/2})=P\left&space;(&space;-z_{\alpha/2}\leq&space;\frac{\hat&space;p-p}{\sqrt{\frac{\hat&space;p(1-\hat&space;p)}{n}}}\leq&space;z_{\alpha/2}&space;\right&space;)" title="P(-z_{\alpha/2}\leq Z\leq z_{\alpha/2})=P\left ( -z_{\alpha/2}\leq \frac{\hat p-p}{\sqrt{\frac{\hat p(1-\hat p)}{n}}}\leq z_{\alpha/2} \right )" />   
         
         <img src="https://latex.codecogs.com/gif.latex?=P\left&space;(&space;\hat&space;p-z_{\alpha/2}&space;\sqrt&space;{\frac{\hat&space;p(1-\hat&space;p)}{n}}\leq&space;p&space;\leq&space;\hat&space;p&plus;z_{\alpha/2}&space;\sqrt&space;{\frac{\hat&space;p(1-\hat&space;p)}{n}}&space;\right&space;)=1-\alpha" title="=P\left ( \hat p-z_{\alpha/2} \sqrt {\frac{\hat p(1-\hat p)}{n}}\leq p \leq \hat p+z_{\alpha/2} \sqrt {\frac{\hat p(1-\hat p)}{n}} \right )=1-\alpha" />   
         
      + 모비율 p의 100(1-alpha)% 신뢰구간   
      
         <img src="https://latex.codecogs.com/gif.latex?\left&space;(&space;\hat&space;p-z_{\alpha/2}&space;\sqrt&space;{\frac{\hat&space;p(1-\hat&space;p)}{n}},&space;\hat&space;p&plus;z_{\alpha/2}&space;\sqrt&space;{\frac{\hat&space;p(1-\hat&space;p)}{n}}&space;\right&space;)" title="\left ( \hat p-z_{\alpha/2} \sqrt {\frac{\hat p(1-\hat p)}{n}}, \hat p+z_{\alpha/2} \sqrt {\frac{\hat p(1-\hat p)}{n}} \right )" />   
         
   + 예) 대학년 1학년의 흡연율 조사를 위해 임의의 150명을 대상으로 흡연관련 설문조사 진행, 그 중 48명이 흡연
      + 흡연율 p의 95% 신뢰구간은?
         + 모비율 = 48/150=0.32
         + alpha = 0.5 -> alpha/2= 0.025
         + z(alpha/2)=1.96 (using 표준정규분포표)
         + 위의 모비율 신뢰구간 식에 의해 (0.32-1.96*0.038087, 0.32+1.96*0.038087) = (0.24534948, 0.39465052)   
         
         <img src="https://user-images.githubusercontent.com/72974863/101878855-ab1ee900-3bd3-11eb-8da9-7c06c82a4f28.png" width="65%" hegiht="65%">      
         
      
