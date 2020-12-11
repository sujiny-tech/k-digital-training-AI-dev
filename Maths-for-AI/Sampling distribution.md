# 표본분포(Sampling distribution)

+ 통계적 추론
   + 표본조사를 통해 모집단에 대한 해석 (전수조사가 정확하지만, 실질적으로 불가능)
   + 그래서 표본조사진행하지만 반드시 오차가 발생
   + 따라서 적절한 표본 추출 방법 필요
   + 표본과 모집단과의 관계를 이해해야 함
   
+ 표본 추출 방법   
   + 단순랜덤추출법(random sampling)
   + 난수표 사용
   + 랜덤넘버 생성기 사용 
      ```python
      >>> import random
      >>> [random.randint(1,1000) for i in range(10)]
      [678, 341, 724, 973, 788, 498, 154, 866, 58, 289]
      ```
      ✨[colab](https://colab.research.google.com/notebooks/intro.ipynb#scrollTo=R1Bx-Sy0TKjd)
      
+ 표본조사를 통해 얻고자 하는 정보 : 모수 (parameter)
   + 모수 => 모평균, 모분산, 모비율 등
   + 모수를 추정하기 위해 표본을 선택해서 표본의 평균이나 분산등을 계산
   + 통계량(statistic) : 표본의 특성값(표본 평균, 표본 분산 등) 
   + 통계랑의 분포 = 표본 분포

+ 표본평균
   + 모평균을 알아내는데 쓰이는 통계량
   + 평균이 <img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" />이고, <img src="https://latex.codecogs.com/gif.latex?\sigma^{2}" title="\sigma^{2}" />인 **정규모집단** 에서 n개의 표본을 추출한다면,   
   
      <img src="https://latex.codecogs.com/gif.latex?\bar{X}\sim&space;N(\mu,&space;\frac{\sigma^{2}}{n})" title="\bar{X}\sim N(\mu, \frac{\sigma^{2}}{n})" />   
      
      + n=10일 때,   
      
       <img src="https://user-images.githubusercontent.com/72974863/101849476-16989480-3b9b-11eb-88d0-9a5ad7d85a42.png">  
       
            
      + 평균 10, 분산 3, n=10일 때,   
      
       <img src="https://user-images.githubusercontent.com/72974863/101849625-6e370000-3b9b-11eb-8178-274383ad6198.png">   


## 중심극한정리(central limit theorem)✨
+ 모집단이 어떤 분포인지 모르고 **n이 충분히 큰** 경우(30이상), **근사적** 으로 **정규분포** 를 따른다.

+ 예) 0~10사이의 수를 n번 뽑는 실험을 10000번 수행할 때
   + 균일하게 뽑힌다고 할 때([균등분포](https://ko.wikipedia.org/wiki/%EC%97%B0%EC%86%8D%EA%B7%A0%EB%93%B1%EB%B6%84%ED%8F%AC)를 따른다고 할 때)   
   
      + n=3인 경우   
      
         ![n_3](https://user-images.githubusercontent.com/72974863/101865868-c5000200-3bba-11eb-875c-a9d01db432f2.png)   
         
         
      + n=30인 경우   
         
         ![n_30](https://user-images.githubusercontent.com/72974863/101865895-d47f4b00-3bba-11eb-8500-71c5096006fa.png)   
         
 
   + 지수분포를 따른다고 할 때
      > lambda=3 : 1시간동안 1/3번 사건이 발생할 때(1회 발생할때까지 걸리는 시간이 보통 3시간)
   
      + n=3인 경우   
         
         ![n_3(지수)](https://user-images.githubusercontent.com/72974863/101865913-df39e000-3bba-11eb-8514-e10e836022a2.png)   
         
      + n=30인 경우   
         
         ![n_30(지수)](https://user-images.githubusercontent.com/72974863/101865933-e7921b00-3bba-11eb-8878-2ff301c086e2.png)   
         
      
