# 검정(Test)

+ 가설 검정(Hypothesis Test)
   + 통계적 추측의 하나로, "모집단 실제의 값이 ~다" 라는 주장과 관련해 표본의 정보를 통해 가설이 합당한지 여부를 판정
   + 귀무가설 (증명된 바 없는 주장, 가설) : 귀무가설이 참이라는 가정하에 검정 수행   
   
      <img src="https://latex.codecogs.com/gif.latex?H_{0}:\mu&space;=&space;\mu_{0}" title="H_{0}:\mu = \mu_{0}" />   
          
   + 대립가설 (새로운 주장, 실제 입증하고 싶은 가설)   
      + 뭘 검정할건지, 대립가설 채택을 위해 통계적 증거 확보해야함, 증거없으면 귀무가설 채택
   
      <img src="https://latex.codecogs.com/gif.latex?H_{1}:\mu&space;>&space;\mu_{0}" title="H_{1}:\mu > \mu_{0}" />    
      
      
+ 검정의 단계
   + 귀무가설, 대립가설 설정
   + 유의 수준(alpha) 설정
   + 검정통계량 계산
      + n이 30이상인 경우, 중심극한정리 사용   
   
        <img src="https://latex.codecogs.com/gif.latex?Z=\frac{\bar{X}-\mu}{s/\sqrt{n}}\sim&space;N(0,1)" title="Z=\frac{\bar{X}-\mu}{s/\sqrt{n}}\sim N(0,1)" />   
      
      + 모집단이 정규모집단이고, 모표준편차가 주어진 경우   
      
        <img src="https://latex.codecogs.com/gif.latex?Z=\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}\sim&space;N(0,1)" title="Z=\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}\sim N(0,1)" />   
      
   + 기각역 or 임계값 계산
   + 주어진 데이터로부터 유의성 판정
   
   
## 모평균의 검정   

+ 예) 어떤 농장에서 자신들이 생산하는 계란의 평균무게=10.5라고 홍보. 이에 생산된 계란 30개의 추출된 표본은 다음과 같다. 
   w=[10.7, 11.7, 9.8, 11.4, 10.8, 9.9, 10.1, 8.8, 12.2, 11.0, 11.3, 11.1, 10.3, 10.0, 9.9, 11.1, 11.7, 11.5, 9.1, 10.3, 8.6, 12.1, 10.0, 13.0, 9.2, 9.8, 9.3, 9.4, 9.6, 9.2]이다. 
   이 광고 타당한지 유의수준 5%로 검정하시오.   
   
   + 귀무가설 <img src="https://latex.codecogs.com/gif.latex?H_{0}:\mu=10.5" title="H_{0}:\mu=10.5" />     
   
   + 대립가설 <img src="https://latex.codecogs.com/gif.latex?H_{1}:\mu&space;\neq&space;10.5" title="H_{1}:\mu \neq 10.5" />   
   
   + 유의수준 = 0.05
   + 검정통계량 (표본의 평균/표준편차) = (10.43, 1.11)
     + 표준화 시키면 다음과 같다.   
     
        <img src="https://latex.codecogs.com/gif.latex?Z=\frac{\bar{X-\mu}}{s/\sqrt{n}}=\frac{10.43-10.5}{1.11\sqrt{30}}=-0.351" title="Z=\frac{\bar{X-\mu}}{s/\sqrt{n}}=\frac{10.43-10.5}{1.11\sqrt{30}}=-0.351" />   
        
   + 유의성 판정   
   
      + <img src="https://latex.codecogs.com/gif.latex?z_{\alpha/2}=z_{0.025}=1.96>\left&space;|&space;-0.351&space;\right&space;|" title="z_{\alpha/2}=z_{0.025}=1.96>\left | -0.351 \right |" />   
      
      + 즉, <img src="https://latex.codecogs.com/gif.latex?z_{\alpha/2}>|Z|" title="z_{\alpha/2}>|Z|" /> 이므로 귀무가설 기각 X
      
      
   ![검정_1](https://user-images.githubusercontent.com/72974863/101893394-08bd3080-3be8-11eb-9329-17c10ac57930.png)   

   + 만약 주어진 30개의 계란무게값에 0.5씩 모두 다 빼준다면?
   
      ![검정_2](https://user-images.githubusercontent.com/72974863/101893852-ab75af00-3be8-11eb-9571-95192b866fd2.png)    
      
      + 검정통계량이 -2.81xxx로 해당 절댓값보다 임계값이 크므로 귀무가설 기각 ❗ 

      
