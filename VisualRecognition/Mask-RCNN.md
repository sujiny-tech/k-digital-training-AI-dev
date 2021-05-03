# Mask-RCNN
> **Faster RCNN**(Object detection) + **FCN**(Semantic segmentation) = **Mask_RCNN**(Instance segmentation)    

+ 구조
> ![image](https://user-images.githubusercontent.com/72974863/111015742-ba3d4f00-83ed-11eb-864c-53a02b7a0a56.png)   
> 출처 : devloppaper.com/mask-r-cnn/

+ Faster RCNN에는 masking하는 layer가 추가된 형태
   + 기존의 Faster RCNN(Object detection)에 각각의 ROI에 Mask segmentation을 해주는 작은 FCN을 추가
   
+ Faster RCNN에서는 ROI pooling을 사용하였으나, Mask-RCNN에서는 **ROI Align**을 적용하였음
   + **ROI Align** : CNN을 통과하면서 ROI pooling 영역의 위치에 생기는 소수점 오차를 bilinear interpolation을 통해 감소시킴 ❗
   + ROI pooling보다 더 정확한 픽셀 위치를 추출함 (논문에서 비교한 표

+ ROI 영역의 object의 mask 예측할 때, class별로 독립적으로 예측함.
   + 즉, k개의 class가 존재한다고 하면 mask를 k개 예측.

+ 논문 결과
> ![image](https://user-images.githubusercontent.com/72974863/111017123-dc869b00-83f4-11eb-9628-7483e58c0188.png)   
> 출처 : Mask-RCNN paper

- - - - - - - - - - - - - - - - - - -
+ 프로젝트 관련해서 찾아본 자료들(Instance segmentation 모델들 등...) : [notion에 정리했던 글 ✨](https://www.notion.so/CAMO-b6867ed2891a426f9cc4a870b83abb98)       
      
      
> ![image](https://user-images.githubusercontent.com/72974863/116871746-b55b8580-ac4f-11eb-986d-b5df6cfc56f6.png)     
> [출처 : papaerswithcode Instance segmentation on COCO test-dev](https://paperswithcode.com/sota/instance-segmentation-on-coco)   


💫 참고
+ [Mask-RCNN paper](https://arxiv.org/pdf/1703.06870.pdf)
+ [다른사람 블로그 참고하기](https://ganghee-lee.tistory.com/40)
