# Semantic Segmentation / Instance Segmentation

+ Object Detection / Semantic Segmentation / Instance Segmentation의 차이 ✨
   + **Object Detection** : bounding box(bbox)로 대체적인 크기는 알 수 있음
      + [paperwithcode-Object Detection](https://paperswithcode.com/task/object-detection)   
      
   + **Semantic Segmentation** : 픽셀단위로 구분 가능, 사람마다 각자 구별은 x
      + [paperwithcode-Semantic Segmentation](https://paperswithcode.com/task/semantic-segmentation)   
      + 많은 양의 데이터를 갖고 있고, 많은 데이터를 출력하므로 object detection 보다 속도가 많이 떨어질수 밖에 없음
      + 응용 ⭐
         + 자율주행차 - 사람 및 사물의 위치나 모양을 측정하기 위해 사용
         + [google](https://ai.googleblog.com/2017/10/portrait-mode-on-pixel-2-and-pixel-2-xl.html) - 카메라 1대로 사람과 후경을 구분
         + 의료영상 - 기존 흑백 의료 이미지를 적절하게 segmentation을 하면 pseudo color를 입혀 구분
      
   + **Instance Segmentation** : 사람마다 구별 가능 (high level segmentation)
   
   
💫 [다른 사람 블로그 참고하기](https://medium.com/hyunjulie/1%ED%8E%B8-semantic-segmentation-%EC%B2%AB%EA%B1%B8%EC%9D%8C-4180367ec9cb)
