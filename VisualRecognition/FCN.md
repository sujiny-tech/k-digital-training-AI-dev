# FCN(Fully Convolutional Network)

+ Semantic Segmentation 문제를 위해 제안된 딥러닝 모델
+ 기존 이미지 분류에서 우수한 성능을 보인 **CNN 기반 모델(AlexNet, VGG16, GoogLeNet)**을 **Segementation에 적합하게 변형시킨 모델** 
+ 특징
   + FC층 없이 **Convolution Layer로만 구성**
      + 정보손실 : 공간/위치정보를 잃음 (마지막에 FC층을 위해 3차원을 1차원벡터로 변형)
      + Input 이미지 크기 고정되어있음 (FC층의 weight 개수가 fix되어있어서 전단계 feature map크기가 고정되어있기 때문)
      
   + **Upsampling 사용** 
      

### Bilinear Interpolation
+ linear interpolation을 확장한 2차원 interpolation을 사용해서 이미지 확대
   > conv + pooling 을 여러번하게 되면 feature map 사이즈가 줄어드니까 다시 키우는 과정 필요하므로   
    
+ end-to-end 학습관점에서 고정된 값을 사용하는 것은 적합하지 않기 때문에 **학습을 기반으로 한 다른 방법 주로 사용**

### Transposed Convolution
+ conv 특성상 input으로 이미지 넣으면, output은 input보다 사이즈 작아짐 (입력사이즈와 똑같은 모든 픽셀정보가 담긴 output이 필요)
+ 따라서 **Transposed Convolution와 upsampling을 통해 output 사이즈 키움**   

> transposed convolution 동작
> ![image](https://cdn-images-1.medium.com/max/1200/1*Lpn4nag_KRMfGkx1k6bV-g.gif)   

## Skip Layer(Skip Connection/Skip Combing)
+ pooling으로 인해 feature map은 디테일이 많이 사라짐, 다시 크기를 키워도 정교하지 못함
+ 이를 해결하기 위해, **이전 층의 feature map을 이용하는 skip connetion 기법** 사용

> skip layer
> ![image](https://user-images.githubusercontent.com/72974863/110479043-50405380-8128-11eb-812f-45a42c35cffb.png)   


💫 참고
+ [Fully Convolutaionl Networks for Semantic Segmentation](https://arxiv.org/abs/1411.4038)
+ [다른 사람 블로그 참고하기](https://everyday-image-processing.tistory.com/32)
