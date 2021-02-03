# 순환 신경망(Recurrent Neural Network, RNN)


<details>
<summary><b>1. 순차 데이터</b></summary>   
<div markdown="1">   


+ **time series 데이터** 
   + 특징이 순서를 가지기 때문에 **순차 데이터(sequential data)**
   + 순차 데이터는 **동적**이며 보통 **가변** 길이를 가짐 (variabl-length input)
   
+ RNN과 LSTM (+GRU)
   + RNN은 시간성 정보를 활용하여 **순차 데이터**를 **처리하는 효과적인 학습 모델**
   + **매우 긴 순차 데이터 처리**에는 장기 의존성(long-term dependency)를 잘 다루는 **LSTM**을 주로 사용 ✨
   
+ 최근에는 RNN도 **생성 모델**로 사용 ❗
   > 예) CNN과 LSTM을 활용해 자연 영상에 주석 생성하는 문제 해결
   

<details>
<summary><b>응용 사례 ✨</b></summary>   
<div markdown="1">   

+ 심전도 신호 분석을 통해 심장 이상 유무 판정
+ 주식 시세 분석을 통해 사고 파는 시점 결정
+ 음석인식을 통한 지능적인 인터페이스 구축
+ 기계 번역기 또는 자동 응답 장치 제작
+ 유전자 열 분석을 통한 치료 계획 수립 ...

</div>
</details>

### 순차 데이터 표현
+ 대표젹인 순차 데이터인 문자열
   + 예) 기계번역에서 입력이 "April is the cruelest month."이고, 출력은 "4월이 가장 잔인한 달"일 때, 식 표기는?
      
+ **사전(dictionary)** 을 사용하여 표현
   + 사전 구축 방법
      + 사람이 **자주 사용하는 단어**를 **모아서 구축**
      + 주어진 **말뭉치를 분석**해서 **단어를 자동 추출하여 구축**
      
   + 사전을 사용한 텍스트 순차 데이터의 표현 방법 ✨
      
      <details>
      <summary><b>단어 가방(Bag of word, BoW)</b></summary>   
      <div markdown="1"> 
         
      + 단어 **각각의 빈도 수**를 카운트해서 m차원의 벡터로 표현
            
      + 한계 💥
         + 정보 검색에 주로 사용, but 기계 학습에는 부적절 ❗
            > 예를 들어, "April is the cruelest month"와 "The cruelest month is April"은 같은 특징 벡터로 표현 → **시간성 정보 사라짐**   
         
      </div>
      </details>
       
      <details>
      <summary><b>원핫 코드(one-hot code)</b></summary>   
      <div markdown="1">
         
      + **해당 단어의 위치**만 **1로 표시**
         
      + 한계 💥
         + **한 단어**를 표현하는데 m차원 벡터를 사용 → **비효율적임** 
         + **단어 간의 유사성 측정 불가능** ❗
         
      </div>
      </details>
         
         
      <details>
      <summary><b>단어 임베딩(word embedding)</b></summary>   
      <div markdown="1">
         
      + 가장 많이 사용하는 방법 ❗❗
         
      + **단어 사이의 상호작용을 분석**하여 **새로운 공간으로 변환** 
         > 보통 m보다 훨씬 낮은 차원으로 변환 
            
         + 변환 과정을 **학습**이 말뭉치를 훈련집합으로 사용하여 알아냄 ✨
            > 예) word2vec [Cho2014b] : 30000차원을 620차원으로 변환 ❗ 
            
         </div>
         </details>
        

### 순차 데이터 특성
+ 특징이 나타나는 순서 중요 ⭐
   + 나타나는 **순서가 달라지면 의미가 크게 바뀌**어서 **훼손**됨
   
+ 샘플마다 길이가 다름
   + RNN은 은닉층에 순환 연결을 부여하여 **가변 길이 수용** 
   

+ **문맥 의존성**
   + **비순차 데이터** 는 **공분산**이 특징 사이의 의존성을 나타냄
   
   + **순차 데이터* 에서는 공분산 의미 X, 대신 **문맥 의존성** 이 중요 ⭐
   
- - - - - - - - - - - - -
</div>
</details>


<details>
<summary><b>2. RNN</b></summary>   
<div markdown="1">   


### 순환 신경망 구조
+ 기존 깊은 신경망과 유사
   > 입력층, 은닉층, 출력층을 가짐   
   
+ **차이점** : 은닉층이 **순환 연결(recurrent edge)** 를 가짐 ⭐
   > 시간성, 가변길이, 문맥 의존성 모두 처리 가능

<img src="https://user-images.githubusercontent.com/72974863/106742058-da942400-665f-11eb-8673-0fcea1db4a58.png">   

[이미지 출처](https://ko.wikipedia.org/wiki/%EC%88%9C%ED%99%98_%EC%8B%A0%EA%B2%BD%EB%A7%9D)   

</div>
</details>   
  

ing... (31:19)  


### 참고
+ [다른 사람의 블로그 ✨](https://yoonjinxd.github.io/deeplearning/2019/07/30/%EC%88%9C%EC%B0%A8%EC%A0%81-%EC%A0%95%EB%B3%B4%EB%A5%BC-%EB%8B%A4%EB%A3%A8%EB%8A%94-%EB%94%A5%EB%9F%AC%EB%8B%9D-%EB%AA%A8%EB%8D%B8%EB%93%A4.html)   

