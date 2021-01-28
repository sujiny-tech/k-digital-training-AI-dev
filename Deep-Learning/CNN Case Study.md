# CNN 사례 연구(CNN Case Study)
+ 영상 분류(image classification) : 과거에는 매우 어렵고 도전적인 문제 💥   

   + **ImageNet**
      + 2만 2천여 종류에 대해 종류별로 수백~수만장의 사진을 인터넷에서 수집해서 1500만여장의 사진 구축 및 공개 (현재, 종류와 개수 추가됨)   
      
   + **ILSVRC(ImageNet Large Scale Visual Recognition Competition) 대회** - CVPR 학술대회에서 개최
      + 1000가지 종류에 대해 분류, 검출, 위치 지정 문제 : 1순위와 5순위 오류 성능 대결 😀
      + 120만장의 훈련 셋, 5만장의 검증 셋, 15만장의 테스트셋
      + 우승 : **AlexNet(2012) → Clarifi 팀(2013) → GoogLeNet & VGGNet(2014) → ResNet(2015)**   
      
         > 우승한 모델은 코드와 학습된 가중치를 공개함으로써 널리 사용되는 표준 신경망이 됨 ✨
         
         > <img src="https://user-images.githubusercontent.com/72974863/105812732-0bd27b80-5ff2-11eb-98d7-3601b1976c1d.png">   
         
         > [이미지 출처](https://semiengineering.com/new-vision-technologies-for-real-world-applications/)   
         

## AlexNet

<details>
<summary><b> 자세히 👀️ </b></summary>   
<div markdown="1">
   
+ 구조
   + **컨볼루션층 5개, 완전연결층(FC) 3개**   
      > 8개 층에 290400-186624-64896-43264-4096-4096-1000개의 노드 배치
   + 컨볼루션층 200만개, FC층 6500만개 가량의 파라미터
      > FC층에 30배 많은 파라미터 → **향후 CNN은 FC층의 파라미터를 줄이는 방향으로 발전** ❗❗   
      
   + 당시 GPU 메모리 제한때문에 GPU 2개로 분할해서 학습 수행
      > 3번째 컨볼루션 층은 GPU1, 2 결과를 함께 사용(inter-GPU connections)   
      
   + 컨볼루션 층에서 큰 stride로 다운 샘플링   
   
      
   > <img src="https://user-images.githubusercontent.com/72974863/105811810-869a9700-5ff0-11eb-86a5-b67ea8eb3da2.png">   
   
   > **중첩 최대 풀링(overlapped max pooling)** 사용, **1000개의 분류를 위해 소프트맥스(softmax) 함수** 사용   
   
   > [이미지 출처](https://paperswithcode.com/method/alexnet#)
   
+ 학습 성공 요인 ✨
   + 외적 요인
      + **ImageNet** 이라는 대규모 사진 데이터
      + **GPU** 를 사용한 병렬처리
    
   + 내적 요인
      + 활성함수로 **ReLU** 사용
      + **지역 반응 정규화(local response normalization) 기법** 적용   
         > **feature map에서 위치가 비슷한 것끼리** 값이 너무 튀지않게 전체적으로 평균값을 맞춰주는 것   
         
         > 요즘에는 batch normalication 많이 사용
         
      + 과잉적합 방지하는 여러 규제기법 적용
         > **데이터 확대**(cropping, mirroring으로 2048배 확대), **dropout**(fc층에서 사용)   
         
   + 테스트 단계에서 앙상블 적용
      + 입력된 영상을 잘라내기와 반전으로 통해 증가된 영상들의 **예측 평균**을 최종 인식
      + **2~3%만큼 오류율 감소** 효과


</div>
</details>


## VGGNet   

<details>
<summary><b> 자세히 👀️ </b></summary>   
<div markdown="1">
   
+ 핵심 아이디어
   + **3x3 작은 커널** 사용   
      > 이후 신경망 구조에 영향을 줌
      > **큰 크기 커널**은 **여러개의 작은 크기 커널**로 **분해** 가능
      
      > 구체적인 예로는 5x5커널을 2층의 3x3 커널로 분해하여 구현 → 그러면 5x5 커널인 경우 **25개**의 파라미터였으나, 3x3 커널인 경우 **18개**의 파라미터로 줄어듦   
      
      > 또한 3x3 커널은 1x3 커널과 3x1 커널로 분해하여 구현 → 그러면 원래 3x3 커널인 경우 **9개**의 파라미터였으나, 3x1 커널와 1x3 커널의 경우 **6개**의 파라미터로 줄어듦   
      
      > 따라서 **파라미터의 수는 줄어들면서** 신경망은 **깊어지는** 효과 ✨
      
      
   + 신경망을 **더 깊게** 만듦(신경망 깊이가 어떤 영향을 주는지 확인)
   + **컨볼루션층 8~16개**를 두어 AlexNet의 5개에 비해 2~3배 깊어짐
   
   + VGGNet16 (conv 13층 + fc 3층)   
      > <img src="https://user-images.githubusercontent.com/72974863/105945595-ece2f080-60a8-11eb-8b6a-d4888b97e359.png">   
      
      > 출처 : https://neurohive.io/en/popular-networks/vgg16/

+ VGGNet에서 1x1 커널 적용 실험을 수행하였으나 최종 선택은 X (GoogLeNet에서 사용됨)   
   + 1x1 커널
      + 차원 통합
      + **차원 축소 효과** 
         > 차원 축소를 통해 연산량 감소
         
      
</div>
</details>


## GoogLeNet

<details>
<summary><b> 자세히 👀️ </b></summary>   
<div markdown="1">
   
+ 핵심 : 인셉션 모듈(inception module)
   + 수용장의 **다양한 특징을 추출**하기 위해 NIN 구조를 확장하여 **복수의 병렬적인 컨볼루션층**을 가짐
   
   
      <details>
      <summary><b> NIN 구조 </b></summary>   
      <div markdown="1">
      
      + 기존 컨볼루션 연산을 MLPConv연산으로 대체   
         > 커널 대신 비선형 함수를 활성함수로 포함하는 **MLP**를 사용해서 **특징 추출이 유리함** 
         
         > <img src="https://user-images.githubusercontent.com/72974863/106133335-73cac280-61a8-11eb-8b9a-f60588e20317.png">   
      
         > [이미지 출처](http://openresearch.ai/t/network-in-network/39)   
         
      + 신경망의 micro neural network가 **주어진 수용장의 특징**을 추상화 시도
      
      + 전역 평균 풀링(global average pooling) 사용
      
         + FCNN 대신 최종단에 전역 평균 풀링을 사용
         + Average pooling만으로 classifier 역할을 할 수 있기 때문에 overfitting 문제를 회피하며 연산량이 줄어드는 이점이 있음.
      
      > <img src="https://user-images.githubusercontent.com/72974863/106134476-eee0a880-61a9-11eb-8077-02eb523751ee.png">   
      
      > [이미지 출처](http://openresearch.ai/t/network-in-network/39)
      
      </div>
      </details>
      
      
   + **NIN 개념을 확장한 신경망** = GoogLeNet   
   
     + 인셉션 모듈 
        + 마이크로 네트워크 MLPConv 대신 **4종류의 컨볼루션 연산** 사용 → **다양한 특징 추출**   
     
           + 1x1 컨볼루션을 사용하여 차원 축소
           + 3x3, 5x5 같은 다양한 크기의 컨볼루션을 통해 다양한 특징 추출   
           
           > <img src="https://user-images.githubusercontent.com/72974863/106135461-4e8b8380-61ab-11eb-8e54-3f0d3c770db2.png">   
        
           > [논문](https://arxiv.org/abs/1409.4842)
     + 인셉션 모듈을 9개 결합한 GoogLeNet
        + 파라미터가 있는 층 22개 + 없는 층(풀링) 5개 = 27개 층
           > 완전 연결층은 1개
           > 백만개의 파라미터를 갖고, VGGNet의 FC에 비하면 1%에 불과함 ✨
        + **보조분류기** (Auxiliary classifier)
           > 원 분류기의 오류 역전파 결과 + 보조 분류기의 오류 역전파 결과 → **경사 소멸 문제 완화** 
           > 학습할 때 도우미 역할, 추론할 때 제거 
        
    
</div>
</details>
    

## ResNet 

<details>
<summary><b> 자세히 👀️ </b></summary>   
<div markdown="1">
   
+ **잔류 학습(residual learning) 개념**을 통해 성능 저하를 피하면서 **층 수를 대폭 늘림**  
   + 지름길 연결(shortcut connection)을 두는 이유?
      + **깊은 신경망도 최적화 가능** 해짐
      
      + 깊어진 신경망으로 **정확도 개선** 가능
      
      + **경사 소멸 문제 해결** 
      
      > <img src="https://user-images.githubusercontent.com/72974863/106137266-d07cac00-61ad-11eb-9fc7-35d990d2edd3.png">   
      
   
+ VGGNet와 비교
   + 같은점 
      + **3x3 커널** 사용
   + 다른점
      + **잔류 학습** 사용
      + **전역 평균 풀링** 사용 (fc 제거)
      + **배치 정규화** 적용(dropout 적용 불필요)   
      
> <img src="https://user-images.githubusercontent.com/72974863/106138107-0cfcd780-61af-11eb-8baf-c8568bebbc1b.png">  

> [ResNet 관련 이미지 출처](https://hydragon-cv.info/entry/Deep-Residual-Learning-for-Image-Recognition)
     
     
</div>
</details>

- - - - - - - - - - - -
### 참고 💫 
+ [google inception 관련 - 다른 사람의 블로그 참고](https://norman3.github.io/papers/docs/google_inception.html)
 
+ [ResNet 관련 - 다른 사람 블로그 참고](https://hydragon-cv.info/entry/Deep-Residual-Learning-for-Image-Recognition)
