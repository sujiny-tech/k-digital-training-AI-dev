# 통계학(Statistics)
+ 정의 : 데이터 수집(collection), 구성(organization), 분석(analysis), 해석(interpretation), 표현(presentation)에 관한 학문
   + 기술 통계학(descriptive statistics) : 측정/실험에서 수집한 데이터를 정리, 표현, 요약 등을 통해 자료의 특성을 구하는 방법을 다루는 분야
   + 추측 통계학(inferential statistics) : 모아놓은 데이터를 분석해서 불확실한 사실에 대해 추측하는 분야

+ 기본 개념
   + **모집단(population)** : 관심의 대상이 되는 개체 및 사건의 집합 ex) 전교 남학생의 키...
   + **모수(parameter)** : 모집단의 수치적은 특성 ex) 키의 평균...
   + **표본(sample)** : 모집단에서 선택된 개체나 사건의 집합 (모집단에서 일부 선택한 집합)
   
+ 도수(Frequency)
   + 어떤 사건이 실험/관찰로부터 발생한 횟수
   + 표현 방법 : 도수분포표(Frequency Distribution Table), 막대그래프(질적 자료), 히스토그램(양적 자료)
   
+ 상대도수 : 도수를 전체 원소 개수로 나눈 것
   + 확률 계산에서 중요한 개념
   
+ 데이터 수집/수치적인 특성 파악을 위해, 파이썬에서 제공하는 scipy, numpy 모듈 설치

- - - - - - - - - - - - - 
## 평균(mean)
+ 대표적인 모수
   ```python
   >>> import statistics
   >>> a=[179, 180, 142, 155, 167, 189, 148, 166, 177, 183]
   >>> statistics.mean(a)
   168.6
   ```
+ 모평균 <img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" /> : 모집단 전체 자료에 대한 평균
+ 표본 평균 <img src="https://latex.codecogs.com/gif.latex?\bar{x}" title="\bar{x}" /> : 모집단에서 추출한 표본에 대한 평균

## 중앙값(median)
+ 평균의 경우, 극단값(튀는 값)의 영향을 많이 받음
   ```python
   >>> b=[179, 180, 142, 155, 167, 189, 148, 166, 177, 183, 100000]
   >>> statistics.mean(b)
   9244.181818181818
   ```
+ 주어진 자료를 높은쪽 절반과 낮은쪽 절반으로 나누는 값을 의미
+ 자료를 순서대로 나열했을 때 가운데 있는 값
+ 자료의 수 : n 
   > n이 홀수일 때, (n+1/2)번째 자료값이 중앙값 / n이 짝수일 때, n/2번째와 (n/2)+1번째 자료값의 평균이 중앙값
   ```python
   >>> a=[179, 180, 142, 155, 167, 189, 148, 166, 177, 183]
   >>> b=[179, 180, 142, 155, 167, 189, 148, 166, 177, 183, 100000]
   >>> statistics.median(a)
   172.0
   >>> statistics.median(b)
   177
   ```
    > 값이 튀더라도 전체적인 데이터의 특성을 잘 표현해줌 ❗❗
    
## 분산(variance)
+ 편차의 제곱의 합을 자료의 수로 나눈 값
   + 편차 : 값과 평균의 차이

+ 자료가 모집단 => 모분산   

   <img src="https://latex.codecogs.com/gif.latex?\sigma^{2}=\frac{1}{N}\sum_{i=1}^{N}\left&space;(&space;x_{i}-\mu&space;\right&space;)^{2}" title="\sigma^{2}=\frac{1}{N}\sum_{i=1}^{N}\left ( x_{i}-\mu \right )^{2}" />      

+ 자료가 표본 => 표본 분산   
   
   <img src="https://latex.codecogs.com/gif.latex?s^{2}=\frac{1}{n-1}\sum_{i=1}^{n}\left&space;(&space;x_{i}-\bar{x}&space;\right&space;)^{2}" title="s^{2}=\frac{1}{n-1}\sum_{i=1}^{n}\left ( x_{i}-\bar{x} \right )^{2}" />   
   
   > 자료의 개수가 n-1인 이유 : 모집단의 분산이나 표준편차를 잘 예측하기 위해 => 자세히 말하면 불편추정치(unbiased estimate)를 만들기 위해
   
   + staticse 모듈 사용
   ```python
   >>> statistics.variance(a) #표본 분산
   250.93333333333334
   >>> statistics.variance(b) #표본 분산
   906028264.5636362
   ```
   + scipy 모듈 사용
   ```python
   >>> import scipy
   >>> import scipy.stats
   >>> scipy.stats.tvar(a) #표본 분산
   250.93333333333334
   ```
   
## 표준편차(standard deviation)
+ 분산의 양의 제곱근
   + statistics 모듈 이용
      + 표준편차
         ```python
         >>> statistics.stdev(a)
         15.840875396686048
         >>> statistics.stdev(b)
         30100.303396537984
         ```
      
      + 모분산, 모표준편차
         ```python
         >>> statistics.pvariance(a)
         225.84
         >>> statistics.pstdev(a)
         15.02797391533536
         ```
   + numpy 이용
      ```python
      >>> import numpy
      >>> numpy.var(a)
      225.84
      >>> numpy.std(a)
      15.02797391533536
      
      >>> numpy.var(a, ddof=1) #ddof : Delta Degrees of Freedom = n에서 얼마 빼줄거니 => 1 빼주면 표본분산
      
      >>> numpy.std(a, ddof=1) #표본표준편차
      ```
      
## 범위(range)
+ 자료를 정렬하였을 때 가장 큰 값과 가장 작은 값의 차이
   ```python
   >>> max(a)-min(a)
   47
   >>> max(b)-min(b)
   99858
   >>> numpy.max(a)-numpy.min(a)
   47
   ```
   
## 사분위수(quartile)
+ 전체 데이터를 정렬했을 때, 1분위수(1/4), 2분위수(1/2), 3분위수(3/4)위치에 있는 값
   + Q1 : 제 1분위수
   + Q3 : 제 3분위수, Q2 = 중앙값
   + Q3-Q1 : 사분위범위(IQR, Interquartile range)
   ```python
   >>> numpy.quantile(a, .25) #사실은 quantile은 백분위수, 백분위수의 특별한 케이스 => 사분위수(quartile)
   157.75
   >>> numpy.quantile(a, .50)
   172.0
   >>> numpy.quantile(a, .75) #2번쨰 파라미터에 아무값이나 상관 x -> .60이라면 60퍼센트에 해당하는 값
   179.75
   ```
   
## z-scrore
+ 어떤 값이 **평균으로부터 몇 표준편차 떨어져있는지**를 의미하는 값 ❗❗
   + 모집단의 경우   
      
      <img src="https://latex.codecogs.com/gif.latex?z=\frac{x-\mu&space;}{\sigma&space;}" title="z=\frac{x-\mu }{\sigma }" />   
      
      ```python
      >>> scipy.stats.zscore(a)
      array([ 0.69204272,  0.75858529, -1.77003235, -0.90497895, -0.10646811,
           1.35746842, -1.37077693, -0.17301068,  0.55895758,  0.958213  ]) #mean(a):168.6, stdev=15.840875396686048 
      ```
      
      > a의 평균=168.6이고, 표준편차=15.840875396686048이므로 대충 184.44가 zscore=1...   
      
   + 표본의 경우   
      
      <img src="https://latex.codecogs.com/gif.latex?z=\frac{x-\bar{x}&space;}{s}" title="z=\frac{x-\bar{x} }{s}" />   
      
      ```python
      >>> scipy.stats.zscore(a, ddof=1) #주어진 데이터가 표본이면, ddof=1으로
      array([ 0.65652937,  0.7196572 , -1.67920013, -0.85853841, -0.10100452,
           1.28780762, -1.30043318, -0.16413234,  0.53027372,  0.90904067])
      ```
