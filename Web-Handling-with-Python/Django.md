# Django
+ **Python기반 웹 프레임워크** 
   > Instagram, Pinterest 등이 이를 사용함   
+ 하나의 project에 **여러 app으로 구성** 되어있음

## flask와의 차이점
+ 추구하고자 하는 방향이 다름 ❗❗
+ ```flask``` : **"마이크로"** 웹 프레임워크로 최소한의 기능을 가짐, **추가적인 모듈을 붙여가면서 빌드업** 
+ ```django``` : **거의 모든것이 내장** 되어있는 구조 (flask보다 프로젝트 사이즈가 큼)

## django의 장/단점
+ **장점** ⭐
   + python기반이여서 **배우기 쉬움** 
   + **개발속도** 가 빠르며 **코드 완성도** 높게 유지, **확장성** 이 좋음
   + 사용자 인증, 관리 등 **내장**
   + **개발 비용 크게 절감** 시킬 수 있음   
   
+ **단점** 💥
   + **객체 지향 프로그램** 에 대한 이해도 필요
   + 성능이 다른 프레임워크(node.js)등 보다 좋지 못함

 
## django의 MVT Pattern (Model, View, Template)    
✔ 개발에서의 **design pattern** ? 
   > 개발의 패턴, 코드의 모듈화를 이용해 각 코드가 독립적으로 동작해서 유기적으로 원하는 목표를 달성하게 해주는 구조   
   + 일반적으로 **MVC Pattern (Model, View, Controller)** 이 많이 활용되었음.   
      + ```MVC Pattern``` : 데이터(model), 사용자 인터페이스(view), 데이터 처리 로직(controller)으로 나누어 한 요소가 다른 요소들에게 영향을 주지 않도록 설계하는 방식   
   
   + django는 이러한 방식을 바탕으로 **django만의 특색있는 pattern** 을 만들었음.
   
### **Model** 
+ 데이터베이스에 저장되는 **데이터**
+ 원래 DB를 다루려먼 SQL 언어를 알아야되는데, django는 이를 몰라도 DB 작업이 가능(ORM 제공)❗
   + ```ORM (Object-Relational Mapping)``` : SQL 언어 대신 데이터베이스 연결해주는 방법   
         
### **View**
+ **웹 요청 처리** (전달받은 데이터 가공처리)후 그 결과를 template에 전달   
   
### **Template**
+ **사용자에게 보여지는 부분**  
+ [Template 언어](https://django-doc-test-kor.readthedocs.io/en/old_master/topics/templates.html) : 변수(단독사용가능), 필터(정보 가공을 해서 표현 가능), 태그(여러 조건을 걸어주거나 반복) 등
  
  
## django로 웹 사이트 만들기
+ django 다운로드
   ```python
   pip install django
   ```

+ project 생성 (가상환경 진입 후)
   ```python
   django-admin startproject <project_name>
   ```
   + 프로젝트 안에 자동으로 <project_name> direcotry 만들어짐
   + 해당 directory의 파일들
      + ```__init__.py``` : 해당 directory가 python 모듈로써 인식되게 하는 역할
      + ```asji.py```, ```wsgi.py``` : 이후 서버에서 실제로 django 프로젝트를 가동할 때 다루게 될 부분
      + ```settings.py``` : 전반적인 django 프로젝트의 설정사항을 반영하는 파일(secret_key, debug, allowe_host...)
      + ```urls.py``` : url을 관리하는 부분 
   
+ 생성된 project안의 manage.py를 이용해 서버 가동
   ```python
   python manage.py runserver
   ```

+ 생성된 프로젝트 폴더로 이동 후 app 생성
   ```python
   python manage.py startapp <app_name>
   ```
   + <app_name> directory 만들어짐
   + 해당 directory 파일들
      + ```__init__.py``` : 이전과 동일
      + ```admin.py``` : admin 페이지에 관한 부분
      + ```apps.py``` : 해당 app에 대한 설정 관리하는 부분
      + ```models.py``` : 해당 app 모듈 안에 쓰일 데이터베이스의 스키마 등등을 클래스 형태로 작성해줄 수 있음
      + ```tests.py``` : 해당 app의 테스트케이스 설명하는 부분
      + ```views.py``` : 해당 app에서 view를 어떻게 관리할건지에 관한 코드 작성하는 부분
   
+ project와 app 연결
   + <project_name>/settings.py 수정해주기
      ```python
      INSTALLED_APPS=[
              ...
              ...
              <app_name>
      ]
      ```

+ Template 만들기(사용자가 보는 화면)
   + <app_name> 폴더 안에 template 폴더 생성 후 내부에 html 파일 생성
      + ```<html_name>.html``` : html 소스 작성 템플릿 언어 작성   
      
         ✨ [html 문법](https://ko.wikipedia.org/wiki/HTML_%EC%9A%94%EC%86%8C) & [정리 잘한 다른사람의 블로그 참고하기](https://ikkison.tistory.com/43)   
         
         ✨ [Template 문법](https://django-doc-test-kor.readthedocs.io/en/old_master/topics/templates.html) : 위의 Template 언어링크와 동일
      
      
- - - - - - - - - - - - -
### django 프로젝트의 큰 틀 💫  

0) 기본 프로젝트 생성 및 장고 설치, 장고 프로젝트 생성
1) 설정(데이터베이스, S3)
2) 데이터베이스 초기화
3) 관리자 계정 만들기   
      
4. 앱 만들기
5. 모델 설계(데이터베이스)   
   
6) 뷰 만들기(기능, 계산)
7) 템플릿 만들기(화면에 표시될 내용/양식)
8) URL 만들기 (CRUD)   
