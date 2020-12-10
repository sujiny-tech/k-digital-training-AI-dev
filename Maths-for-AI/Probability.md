# 확률(probability)
+ 상대 도수에 의한 정의
   + 똑같은 실험을 많이 반복할 때 어떤 일이 일어날 비율 (상대도수의 극한)
     > ex) 상대도수의 극한

+ 고전적 정의
   + 표본 공간(sample space) = 모든 가능한 실험결과들의 집합 ex) 주사위 숫자 : {1,2,3,4,5,6}
   + 사건 = 관심있는 실험결과들의 집합 (표본공간의 부분집합)  ex) 주사위 숫자 중 짝수 : {2,4,6}
   + 어떤 사건 A가 일어날 확률 P(A) = 사건의 원소의 수/표본공간의 원소의 수 
   
+ 확률은 0(일어나지 않은 경우)에서 1 (반드시 일어날 경우)사이의 값을 가짐
+ 고전적 확률
   + 표본 공간의 원소의 수, 사건의 원소수 카운트 해야함 => 경우의수를 쉽게 세기 위해 **조합(Combination)** 사용

 
## 조합(Combination)
+ 어떤 집합에서 순서에 상관없이 뽑은 원소의 집합
   + n개 중 r개를 뽑는 조합의 수   

     <img src="https://latex.codecogs.com/gif.latex?nCr=\begin{pmatrix}&space;n\\&space;r&space;\end{pmatrix}=\frac{n!}{r!(n-r)!}" title="nCr=\begin{pmatrix} n\\ r \end{pmatrix}=\frac{n!}{r!(n-r)!}" />   

+ 예제) 확률의 계산
   + 검은공 3개, 흰공 4개 중 2개의 공을 무작위로 뽑을 때, 둘다 흰공이 나올 확률?
      + 1~7번까지 7개의 공
      + 1~3은 검은공/4~7은 흰공
      + 표본공간={(1,2), (1,3), ..., (6,7)} => 7C2 = 21 
      + 흰공 2개인 사건={(4,5), (4,6), (4,7), (5,6), (5,7), (6,7)} => 4C2 = 6 
      + 확률=6/21=2/7
 
   + 검은공 3개, 흰공 4개 중 3개의 공을 무작위로 뽑을 때, 흰공 1개 검은공 2개가 나올 확률?
      + 표본공간의 원소 수= 7C3 = 35 
      + 흰공 1, 검은공 2개 뽑는 경우의 수 = 4C1 X 3C2 = 12
      + 확률 = 12/35

## 덧셈 법칙(Addition Law)
+ 주사위를 던지는 실험에서 표본 공간 S={1,2,3,4,5,6}
   + 사건 A=주사위 숫자가 짝수인 사건 => P(A)=1/2
   + 사건 B=주사위 숫자가 4이상인 사건 => P(B)=1/2
   + 사건 A와 B가 일어날 확률     
      + <img src="https://latex.codecogs.com/gif.latex?A\cup&space;B=\left&space;\{&space;2,4,5,6&space;\right&space;\}" title="A\cup B=\left \{ 2,4,5,6 \right \}" />      
   
        > <img src="https://latex.codecogs.com/gif.latex?P(A\cup&space;B)=\frac{|A\cup&space;B|}{|S|}=4/6=2/3" title="P(A\cup B)=\frac{|A\cup B|}{|S|}=4/6=2/3" />   
   
   + 사건 A와 B가 동시에 일어날 확률   
      + <img src="https://latex.codecogs.com/gif.latex?A\cap&space;B=\left&space;\{&space;4,6&space;\right&space;\}" title="A\cap B=\left \{ 4,6 \right \}" />   
   
        > <img src="https://latex.codecogs.com/gif.latex?P(A\cap&space;B)=\frac{|A\cap&space;B|}{|S|}=2/6=1/3" title="P(A\cap B)=\frac{|A\cap B|}{|S|}=2/6=1/3" />   
   
   + <img src="https://latex.codecogs.com/gif.latex?P(A\cup&space;B)=P(A)&plus;P(B)-P(A\cap&space;B)" title="P(A\cup B)=P(A)+P(B)-P(A\cap B)" />   

      > <img src="https://latex.codecogs.com/gif.latex?P(A\cup&space;B)=\frac{1}{2}&plus;\frac{1}{2}-\frac{1}{3}=\frac{2}{3}" title="P(A\cup B)=\frac{1}{2}+\frac{1}{2}-\frac{1}{3}=\frac{2}{3}" />   

   + 예) 한명의 사람을 랜덤하겡 뽑을때 남자이거나 20세 미만일 확률?   
      + 1000명의 사람이 있는데, 남자의 비율이 40%, 20세 미만의 비율이 43%, 20세 미만이면서 남자인 사람의 비율이 15%라고 한다. 한 명의 사람을 랜덤하게 뽑을 때 남자이거나 20세 미만일 확률?
         + A : 남자일 사건 => P(A)=0.4
         + B : 20세 미만일 사건 => P(B)=0.43   
         + <img src="https://latex.codecogs.com/gif.latex?P(A\cap&space;B)=0.15" title="P(A\cap B)=0.15" />   
         + <img src="https://latex.codecogs.com/gif.latex?P(A\cup&space;B)=P(A)&plus;P(B)-P(A\cap&space;B)=0.4&plus;0.43-0.15=0.68" title="P(A\cup B)=P(A)+P(B)-P(A\cap B)=0.4+0.43-0.15=0.68" />   

## 서로 배반(Mutually Exclusive)
+ 두 사건의 교집합이 공집합일 경우
   + 사건 A와 사건 B가 서로 배반 => <img src="https://latex.codecogs.com/gif.latex?P(A\cap&space;B)=0" title="P(A\cap B)=0" />, <img src="https://latex.codecogs.com/gif.latex?P(A\cup&space;B)=P(A)&plus;P(B)" title="P(A\cup B)=P(A)+P(B)" />   
   
   + 예) 주사위를 던져서 홀수나오는 사건과 4의 배수가 나오는 사건은 서로 배반이므로, 합집합은 각 확률을 더해준 것과 동일
   
## 조건부 확률(Conditional probability)
+ 어떤 사건 A가 일어났을 때, 다른 사건 B가 일어날 확률   
  <img src="https://latex.codecogs.com/gif.latex?P(B|A)=\frac{P(A\cap&space;B)}{P(A)}" title="P(B|A)=\frac{P(A\cap B)}{P(A)}" />   
  + 단, <img src="https://latex.codecogs.com/gif.latex?P(A)>0" title="P(A)>0" />   
  
  + 예) 주사위를 하나 던졌을 때, 4이상의 수가 나옴 => 그 수가 짝수이 확률?
     + 사건 A = 4이상의 수가 나오는 사건 P(A)=3/6=1/2
     + 사건 B = 짝수가 나오는 사건
     + <img src="https://latex.codecogs.com/gif.latex?P(A\cap&space;B)" title="P(A\cap B)" />=2/6=1/3   
     
     + <img src="https://latex.codecogs.com/gif.latex?P(B|A)=\frac{P(A\cap&space;B)}{p(A)}=\frac{1/3}{1/2}=\frac{2}{3}" title="P(B|A)=\frac{P(A\cap B)}{p(A)}=\frac{1/3}{1/2}=\frac{2}{3}" />   
     
## 곱셈법칙
+  <img src="https://latex.codecogs.com/gif.latex?P(A\cap&space;B)=P(B|A)P(A)" title="P(A\cap B)=P(B|A)P(A)" />   
+ 예) 어떤 학교에서 60%의 학생이 남학생이다. 그 학교 남학생의 경우 80%는 축구를 좋아한다. 그 학교에서 학생 1명을 랜덤하게 뽑았을 때 축구를 좋아하는 남학생일 확률은?   
   + 사건 A = 남학생일 경우  => P(A)=0.6
   + 사건 B = 축구를 좋아하는 경우 
   + 남학생 중 축구를 좋아하는 경우 => P(B|A)=0.8
   + <img src="https://latex.codecogs.com/gif.latex?P(A\cap&space;B)=P(B|A)P(A)=0.8\times&space;0.6=0.48" title="P(A\cap B)=P(B|A)P(A)=0.8\times 0.6=0.48" />   
  
+ 서로 독립인 경우 => P(B|A)=P(B)
   + <img src="https://latex.codecogs.com/gif.latex?P(A\cap&space;B)=P(B|A)P(A)=P(B)P(A)=P(A)P(B)" title="P(A\cap B)=P(B|A)P(A)=P(B)P(A)=P(A)P(B)" />   

   + 예) 주사위 2개를 던지는 실험에서 첫번째 주사위의 숫자가 짝수인 사건과 두번째 주사위의 숫자가 짝수인 사건은 서로 독립   
   
      + 첫번째와 두번째 숫자가 짝수인 경우   
      
         <img src="https://latex.codecogs.com/gif.latex?P(A\cap&space;B)=P(A)P(B)=\frac{1}{4}" title="P(A\cap B)=P(A)P(B)=\frac{1}{4}" />   
   
