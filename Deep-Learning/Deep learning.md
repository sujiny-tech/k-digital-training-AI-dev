# 심층학습(Deep learning)

<details>
<summary><b>심층학습 기초 I</b></summary>   
<div markdown="1">  
   
+ **다층 퍼셉트론**에 **은닉층을 여러개 추가**하면 깊은 신경망(deep neural networks)
   > 전통적인 다층 퍼셉트론 : 얕은 구조이므로 가공하지 않은 획득한 원래 패턴을 그대로 입력하면 **낮은 성능**   
   
   > 따라서 사람이 **수작업 특징**을 선택하거나 추출해서 신경망에 입력함 
   
+ 깊은 신경망의 학습
+ 새로운 응용을 창출하고 인공지능 제품의 성능을 획기적으로 향상
   > **학습**에 의해 **자동적**으로 **데이터로부터 특징(data-driven features) 추출** : **표현학습 representation learning** ⭐   
   
   > 현대 기계학습을 주도 ✨
   
   
+ 배경
   + 퍼셉트론의 한계 → 다층 퍼셉트론 (1980년대)
      + 1980년대에 이미 깊은 신경망 아이디어가 등장했으나, **실현 불가능** 💥
         + **경사 소멸 문제(gradient vanishing problem)**
            > 층이 깊어지면서 기울기가 중간에 0이 되어서 gradient 값이 소실되는 문제 발생   
            
         + 작은 훈련집합
         + 과다한 연산과 시간소요(낮은 연산의 범용 컴퓨터, 값비싼 슈퍼컴퓨터)
      
      + 일부 연구자들은 지속적 연구 진행
         + 학습률, 은닉 노드 수에 따른 성능 변화 양상, 모멘텀과 같은 최적 탐색 방법 모색, 데이터 전처리 영향, 활성함수의 영향, 규제 기법의 영향 등   
         
   + **성공 배경**
      + 혁신적 알고리즘 등장 ✨
         + **합성곱 신경망(convolutional neural networks, CNN)** 구조
            > 부분 연결과 가중치 공유를 통해 효율적인 신경망 학습 구조 제공 
            
            > 예) MNIST 인식 경쟁이나 ILSVRC 사진 인식 경쟁에서 **CNN이 DMLP보다 확연히 우월**
            
         + 경사 소멸 문제 해결을 위한 **ReLU 활성함수**
         + 과잉적합 방지하는데 효과적인 **다양한 규제기법**
         + 층별 예비학습(pretraining) 기법 개발
      + 값싼 **GPGPU** 등장
      + 학습 데이터 **양과 질의 향상**
      
+ 깊은 신경망의 표현학습 (또는 특징학습)      
   + **낮은 단계 은닉층** : 선이나 모서리와 같은 **간단한 (저급) 특징** 추출
   + **높은 단계 은닉층** : 추상적인 형태(abstractive representation)의 **복잡한 (고급) 특징** 추출
   
   + **표현학습이 강력해짐**에 따라 기존 응용에서 **획기적인 성능 향상 ↑**  
   
      + 영상 인식, 음성 인식, 언어 번역 등   
      
      + 새로운 응용 창출 ✨
         + 분류, 회귀 뿐만 아니라 **생성 모델 / pixel 수준의 영상 분할**
         + CNN과 LSTM의 **혼합 학습 모델**(예시: 자연 영상에 주석달기 응용) 등이 가능해짐


+ 깊은 다층 퍼셉트론 (깊은 신경망, DMLP)
   > **MLP의 동작을 나타내는 식**을 보다 많은 단계로 **확장**한 것

   + 기존 MLP 학습과 유사
      + 경사도 계산과 가중치 갱신을 **더 많은 단계**에 걸쳐 수행
   
   
+ 다층 퍼셉트론의 역사적 발전 양상    


> <img src="https://user-images.githubusercontent.com/72974863/105632344-ec264080-5e95-11eb-8595-d3c49f9fcd57.png">    


### 왜 심층학습이 강력한가? 🤔
   + **종단간(end-to-end) 최적화**된 학습 가능 ❗   
      > 고전적 방법에서는 여러 단계를 따로 설계 구현해야함(분할, 특징 추출, 분류를 따로 구현)
      
      > 심층학습은 전체 깊은 신경망을 **동시에 최적화** → **종단간 학습**   
      
   + **깊이**의 중요성
      > 은닉층의 개수가 증가함에 따라 표현력 증가 ❗   
      
   + **계층적 특징**(hierarchical features) ❗ 
      + 낮은 층에서는 공통적인 간단한 특징, 다음 층은 이전 층의 조합을 통해 점진적으로 추상화하는 형태   
      
</div>
</details>
    
## 컨볼루션 (합성곱) 신경망 (convolutional neural network, CNN)
+ **영상 인식**에 많이 쓰임   
   > 영상 분야에서 다양하게 활용 (분류 classification, 검출 detection, 검색 retrieval, 분할 segmentation) ✨

+ **컴퓨터 비전**의 어려운 점
   + **동일한 객체라도** 영상을 찍는 **카메라의 이동과 각도**에 따라 **모든 픽셀값이 변화**됨
   + **경계색(보호색)** 으로 **배경과 구분이 어려운 경우**가 존재
   + **조명** 에 따른 변화
   + **기형적인 형태의 영상** 이나 **일부가 가려진 영상** 존재
   + **같은 종류 간의 변화**가 큼    
   
+ **컨볼루션층(CONV)**
   + 선형함수인 컨볼루션과 비선형 함수인 활성함수의 조합   
         
      + 컨볼루션 (합성곱) 연산
           
         > 해당하는 요소끼리 곱하고 결과를 모두 더하는 **선형연산**    
           
         > 영상에서 **특징 추출을 위한 용도**로 사용 (공간 필터, spatial filtering)       
              
                 
         <details>
         <summary><b>✨ 2차원 컨볼루션 연산 과정 자세히 ✨</b></summary>   
         <div markdown="1">  
              
         > <img src="https://user-images.githubusercontent.com/72974863/105700096-b80d5700-5f4b-11eb-9316-80cbfaa81794.png" width="70%" height="70%">   
           
         > [이미지 출처](https://yceffort.kr/2019/01/29/pytorch-3-convolutional-neural-network)   
                 
                 
         > padding 처리한 conv_layer ↓↓↓  
                    
         > ![conv_layer](https://user-images.githubusercontent.com/72974863/105700367-205c3880-5f4c-11eb-980d-46895537e5f8.gif)   
                
           
         > [출처](https://towardsdatascience.com/intuitively-understanding-convolutions-for-deep-learning-1f6f42faee1)    
                    
         </div>
         </details>  
                 
      + 학습에 의해 결정된 **복수의 커널들(필터들)** 에 대응되는 특징들을 추출 → conv layer
         > 각 층의 입출력의 특징형상 유지 (특징맵) ⭐   
               
         > 영상의 공간정보 유지하면서 **공간적으로 인접한 정보의 특징을 효과적으로 인식** ⭐ 
               
         > 각 커널(필터)은 파라미터를 공유함으로써 상대적으로 학습 파라미터 매우 적음 (완전 연결 신경망에 비해) ⭐  
       
  <details>
  <summary><b>특징⭐</b></summary>   
  <div markdown="1">  
        
     + **padding** 
                 
        + **각 층의 입출력 특징 형상 유지** (가장자리에서 영상의 크기가 줄어드는 효과 방지)
                 
     + 편향 추가
                 
     + **가중치 공유**(weight sharing, parameter sharing)
        + 모든 노드가 **동일한 커널** 사용 ✨
                   
        + **모델의 복잡도가 크게 낮아짐** ✨
             
     + **다중 특징 맵 추출**   
                    
        + **커널의 값**에 따라 **커널이 추출하는 특징**이 달라짐    
           > 하나의 커널만 사용하면 너무 빈약한 특징 추출됨 💥   
        
     + **특징 학습** 💫
        > 커널을 사람이 설계하지 않고, 학습으로 찾음 ✨
                 
     + **큰 strid(보폭)**에 의한 **다운 샘플링(down-sampling)**
     
     + **3차원 이상 구조**에도 적용 가능
  </div>
  </details>   
        
      
+ **풀링층(POOL)**
   + 컨볼루션의 얻어진 특징을 통계적으로 압축   
      > **추출된 영상**의 **특징을 요약**하고 **강화**하는 층
      
   + 풀링 연산
      + 보폭을 크게하면 다운 샘플링 효과 ✨
      > 최대풀링, 평균 풀링, 가중치 평균 풀링 등
         
      > <img src="https://user-images.githubusercontent.com/72974863/105706354-c7dd6900-5f54-11eb-9198-ef8cccd73e40.png" width="60%" height="60%">   
      
     
      > [이미지 출처](http://taewan.kim/post/cnn/)    
         
         
         
      > max pool with 2x2 filters and stride 2 ↓↓↓
      
      > <img src="https://user-images.githubusercontent.com/72974863/105706461-e9d6eb80-5f54-11eb-866e-ee404ef94b28.png" width="60%" height="60%">      
      
      
      > [이미지 출처](https://wandb.ai/site/articles/intro-to-cnns-with-wandb)  
      
      
   <details>
   <summary><b>특징⭐</b></summary>   
   <div markdown="1">   
         
      + **평균 등 통계적 대표성을 추출**
      + 매개변수 x
      + 특징 맵의 수는 그대로 유지
      + 연산 효율화 (연산 횟수, 연결 가중치 개수 줄임)
      + 작은 변화에 둔감 ✨ → 물체 인식 및 영상 검색 등 효과적임
      
   </div>
   </details>  
      
+ 전체적인 구조   
   + **building block**을 이어 붙여 **깊은 구조로 확장**  
      
   > <img src="https://user-images.githubusercontent.com/72974863/105667011-e70cd400-5f1d-11eb-9b4c-a80b33f4705b.png" width="60%" height="60%">   
      
   > [이미지 출처](https://en.wikipedia.org/wiki/Convolutional_neural_network)
   
   
+ **초창기 CNN 사례** → LeNet-5   
   + 특징 추출 : conv-pool-conv-pool-conv의 5층을 통해 28x28 명암 영상을 120차원 특징벡터로 변환
   + 평균 풀링 사용
   + 분류 : 은닉층이 하나인 MLP
   + CNN 첫번째 성공 사례 : 필기 숫자 인식기를 만들어 수표 인식 자동화 시스템 구현 ❗
      
      
+ DMLP vs CNN
   + DMLP : 완전 연결 구조, 높은 복잡도, 학습 매우 느림, 과잉적합 우려
   + CNN : 컨볼루션 연산을 이용한 **부분연결(희소 연결)** 구조, 복잡도 크게 낮춤, 컨볼루션 연산은 **좋은 특징 추출**   
               
         
+ CNN 특징 ✨
   + **격자(grid) 구조를 갖는 데이터**에 적합
      > 영상, 음성 등
   + **수용장(receptive field**)은 **인간시각**과 유사
   + **가변 크기**의 **입력처리** 가능 ⭐ 
      > 완전 연결 신경망은 특징 벡터 크기가 달라지면 연산 불가능 💥   
            
      > 이에 비해, 컨볼루션층에서 보폭 조정하거나 풀링층에서 커널/보폭 조정으로 특징 맵 크기 조절 가능함   
         
- - - - - - - - - - - - - - -

## 💫 참고하기
⭐ [CNN CIFAR-10 훈련예제](http://cs.stanford.edu/people/karpathy/convnetjs/demo/cifar10.html)   

⭐ [CNN 시각화 예제](https://poloclub.github.io/cnn-explainer/)
