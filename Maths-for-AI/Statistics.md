# 통계학(Statistics)
+ 정의 : 데이터 수집(collection), 구성(organization), 분석(analysis), 해석(interpretation), 표현(presentation)에 관한 학문
   + 기술 통계학(descriptive statistics) : 측정/실험에서 수집한 데이터를 정리, 표현, 요약 등을 통해 자료의 특성을 구하는 방법을 다루는 분야
   + 추측 통계학(inferential statistics) : 모아놓은 데이터를 분석해서 불확실한 사실에 대해 추측하는 분야

+ 개념
   + 모집단(population) : 관심의 대상이 되는 개체 및 사건의 집합 ex) 전교 남학생의 키...
   + 모수(parameter) : 모집단의 수치적은 특성 ex) 키의 평균...
   + 표본(sample) : 모집단에서 선택된 개체나 사건의 집합 (모집단에서 일부 선택한 집합)
   
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
   import statistics
   a=[179, 180, 142, 155, 167, 189, 148, 166, 177, 183]
   statistics.mean(a)
   ```
+ 모평균 <img src="https://latex.codecogs.com/gif.latex?\mu" title="\mu" /> : 모집단 전체 자료에 대한 평균
+ 표본 평균 <img src="https://latex.codecogs.com/gif.latex?\bar{x}" title="\bar{x}" /> : 모집단에서 추출한 표본에 대한 평균

## 중앙값(median)
+ 평균의 경우, 극단값(튀는 값)의 영향을 많이 받음
