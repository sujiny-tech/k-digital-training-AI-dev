# API to serve ML model
+ AWS EC2와 Python Flask 기반 모델 학습 및 추론을 요청/응답하는 API 서버 개발

### Interface
+ 사용자는 기계와 소프트웨어를 제어하기 위해 인터페이스를 **정해진 메뉴얼에 따라 활용하여 원하는 경험을 획득** 
+ **상호 합의된 메뉴얼** 에 따라 적절한 입력을 받아 **기대되는 출력을 제공** 할 수 있어야함 ❗❗
+ 대표적인 예) 리모컨 : 전원을 통해 tv를 킴(모니터에서 화면 출력) 

### API (Application Programming Interface)
+ 기계와 기계, 소프트웨어와 소프트웨어 간의 **커뮤니케이션을 위한 인터페이스** 를 의미
+ **사전에 정해진 정의** 에 따라 입력이 들어왔을 때 **적절한 출력을 전달** 해야함 ❗❗

### RESTful API for ML/DL model inference
+ REST 아키텍처를 따르는 API, [이전 강의 REST API]()

### Practical process of machine learning
+ 문제 정의, 데이터준비, 모델 학습 및 검증, 모델 배포, 모니터링 등의 과정을 통해 실제 서비스에 기계학습 모델 적용
   + **문제 정의** : 필요한 raw data 가져오고, 풀고자하는 문제를 정의
   + **데이터 준비** : raw data 가공, 모델학습을 위한 형태를 위해 작업 진행
   + **모델 학습** 및 **검증** : 모델학습 후, 검증을 통해 배포해도되는 모델인지 판단
   + **모델 배포** : 검증을 통해 나온 학습된 모델 파일을 배포
   + **모니터링** : 배포를 위한 API 서버 제공, 지속적인 모니터링 시스템을 통해 모델의 성능을 모니터링, 다양한 앱에 제공
   
   
💫 **다루고자 하는 실습(목표)**  : 저장된 모델 파일을 불러와서 예측해주는 API 서버를 만들기 ✨
   
   
### Model Serving
+ 학습된 모델을 REST API 방식으로 배포하기 위해서 학습된 모델의 Serialization과 웹 프레임워크를 통해 배포 준비 필요
   + Model Training (데이터 전처리, 모델학습 및 평가) -> Serializing Model(모델 저장) -> Serving Model(저장된 모델 불러서 추론 및 배포)
   + 모델 서빙할 때, **학습시 데이터 분포나 처리방법과의 연속성** 유지 필요 ❗❗

### Serialization & De-serialization
+ 학습된 모델의 재사용 및 배포를 위해서 저장하고 불러오는 것
+ **Serialization** 을 통해 ML/DL model object를 디스크에 write해서 어디든 전송하고 불러올 수 있는 형태로 변환
+ **De-serialization**을 통해 Python/다른환경에서 model을 불러와 추론 및 학습에 사용

### Skeleton of handler to serve model
+ 모델 불러오고, 불러온 모델을 모델 학습처럼 전처리하고, 그 결과를 사람이 이해할수있는 형태로 후처리 작업을 feature의 형태로 바꿔줌
+ 이 결과 역시도 확률적인 분포 및 수치적인 형태! 이를 **결과값에 대해 레이블링 하거나 보정을 하는 후처리 작업을 해야함** 
+ 이러한 과정을 **Handler** 로 진행
+ **코드의 관리** 및 **연속정 유지 측면** 에서 handler 만들어서 하는 게 좋음

### Model serving을 위한 다양한 Frameworks
+ handler한다 하더라도 결국 어떤 프레임워크에서 서빙할 건지가 중요
+ 특히 딥러닝 환경에서는 gpu 활용한다거나 분산적으로 진행하기 때문에 안정적으로 모델을 서빙하는 것이 중요 ❗❗
+ 실무에서는 일반적으로 **Tensorflow serving, TorchServe, TensorRT** 와 같은 프레임워크 사용

