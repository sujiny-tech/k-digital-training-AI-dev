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
      + ```settings.py``` : 전반적인 django 프로젝트의 설정사항을 반영하는 파일(secret_key, debug, database...)
      + ```urls.py``` : url을 관리하는 부분 (django로 작성된 사이트의 목차) 
      + ```wsgi.py``` : 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점
   
+ 생성된 project안의 manage.py를 이용해 서버 가동
   ```python
   python manage.py runserver
   ```
   + 기본적으로 내부 IP의 8000번 포트로 개발 서버를 띄움.
   + 포트 바꾸기
      ```python
      python manage.py runserver 8080  #8080로 변경
      ```
   + 외부접속 허용
      ```python
      python manage.py runserver 0.0.0.0:8000
      ```
      + 외부에서는 서버를 띄운 컴퓨터에 할당된 IP+포트번호를 통해 접속 가능
      + 공유기를 연결하여 사용하는 경우, 공유기에서 외부 접속을 막고 있기 때문에 **포트포워딩** 필요함
         + [관련 내용 - 정리잘한 다른사람의 블로그 참고하기 ✨](https://compunication.tistory.com/5)

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
      
+ 모델 선언 및 활성화
   + 모델 선언 - app_name/models.py에 모델 객체 선언 (이러이러한 필드를 갖는 데이터베이스를 만들겠다~)
      + 모델의 필드 타입
         + 문자열 : CharField (max_length 입력해줘야함)
         + 숫자 : IntegerField, SmallIntegerField
         + 논리형 : BooleanField 
         + 시간/날짜 : DataField...   
         
      + django는 기본적으로 Primary Key 생성함 (id)
         + 데이터가 추가될 때마다 자동으로 증가   
         
   + 모델 활성화
      + 모델의 변경사항 파악
         ```python
         python manage.py makemigrations <app_name>
         ```   
         > migration : django가 모델의 변경사항과 데이터베이스 스키마를 저장하는 방법을 의미
         
      + 자동으로 migration 실행, 데이터베이스 스키마 관리
         ```python
         python manage.py migrate <app_name>
         ```
   
+ Template 만들기(사용자가 보는 화면)
   + <app_name> 폴더 안에 template 폴더 생성 후 내부에 html 파일 생성
      + ```<html_name>.html``` : html 소스 작성 템플릿 언어 작성   
      
         ✨ [html 문법](https://ko.wikipedia.org/wiki/HTML_%EC%9A%94%EC%86%8C) & [정리 잘한 다른사람의 블로그 참고하기](https://ikkison.tistory.com/43)   
         
         ✨ [Template 문법](https://django-doc-test-kor.readthedocs.io/en/old_master/topics/templates.html) : 위의 Template 언어링크와 동일
      
+ view를 통해 모델(데이터베이스) or URL과 템플릿(html) 연결해주기

- - - - - - - - - - - - -
## django 프로젝트의 큰 틀 💫  

0) 기본 프로젝트 생성 및 장고 설치, 장고 프로젝트 생성
1) 설정(데이터베이스, S3)
2) 데이터베이스 초기화
3) 관리자 계정 만들기   
      
4. 앱 만들기
5. 모델 설계(데이터베이스)   
   
6) 뷰 만들기(기능, 계산)
7) 템플릿 만들기(화면에 표시될 내용/양식)
8) URL 만들기 (CRUD)   
- - - - - - - - - - - - - -

## Django 관련 이슈 및 해결방안 😂



<details>
<summary>django 프로젝트에 부트스트랩 적용 시 css 및 font 등 적용이 안될 때 ❗ </summary>   
<div markdown="1">   
   
   + 부트스트랩(bootstrap) : 동적 웹사이트를 위한 CSS 프레임워크 중 한 종류
   + **css 파일 링크 문제** : 이전에 사용한 css를 브라우저가 캐시에 보관해놓고 사용해서 링크된 css 변화점을 기억하지 못함
   + 해결 방법 👍
      + **인터넷 사용기록삭제(브라우저 캐시 삭제)** 
      + 다른 css로 인식하게 만들기 : 링크코드 뒤에 ?after 등 아무 문자열 추가
   + [도움받은 다른 사람의 블로그 ✨](https://meaownworld.tistory.com/89)
   
</div>
</details>
 
<details>
<summary>django favicon 설정하고 싶을 때 ❗ </summary>   
<div markdown="1">   
   
   + ```favicon``` : Favorites + Icon의 합성어로 **홈페이지 제목 영역에 표시되는 작은 아이콘** 
   + 설정 방법 👍 : link 태그를 통해 설정
      + head 내부에 ```<link rel="icon" type="image/png" href="아이콘으로 쓰고 싶은 이미지 경로">```
      + png 파일을 사용할 때, type="image/png"로 설정
      + ico(아이콘)파일을 사용할때는 type="image/x-icon"으로 설정
   
</div>
</details> 

<details>
<summary>django 계정 비밀번호 까먹었을 때 ❗ </summary>   
<div markdown="1">   
   
   + 해결 방법 👍
      + 방법 1 : ```python manage.py changepassword <user_ID>```
      + 방법 2 : ID도 모를 경우, shell에서 변경
         + ```python manage.py shell``` 실행
         ```python
         >>> from django.contrib.auth.modesl import User
         >>> User.objects.filter(is_superuser=True) #superuser ID 확인하기
         >>> super_id=User.objects.get(username="ID")
         >>> super_id.set_password("변경할 비밀번호")
         >>> super_id.save()
         >>> exit()
         ```
   + [도움받은 다른 사람의 블로그 ✨](https://kitle.xyz/post/58/)
   
</div>
</details> 

<details>
<summary>django 데이터베이스 초기화시키고 싶을 때 ❗ </summary>   
<div markdown="1">   
   
   + 해결 방법 👍
      + 1. migrations 파일 삭제 (migrations dir안 init.py 모듈 제외한 모든 파일 삭제)
         + ```find . -path "*/migrations/*.py" -not -name "__init__.py" -delete```
         + ```find . -path "*/migrations/*.pyc"  -delete```
      + 2. 데이터베이스 제거
         + db.sqlit3파일 삭제(다른 db엔진 사용시 해당 데이터베이스 삭제)
      + 3. 새 스키마 생성
         + python manage.py createsuperuser #admin 계정 생성
         + python manage.py makemigrations
         + python manange.py migrate
   
</div>
</details> 

<details>
<summary>django csv 파일 bulk_creat을 통해 모델(데이터) 추가하기 ❗ </summary>   
<div markdown="1">
   
   + ```bulk_creat``` : 다량의 데이터를 한번에 데이터베이스에 넣기
   + django project 최상위 경로로 bulk.py를 생성 (이를 통해 모델 추가)
   + 기본 설정 수행(django 내부 설정, 모델 인식 및 환경설정)
   + csv 파일을 읽고 받아와서 모델의 instances 추가시켜주기
   + [도움받은 다른 사람의 블로그 ✨](https://juneyr.dev/2018-02-19/make-bulk-update-from-csv-django)

</div>
</details> 

<details>
<summary>django table class 종류 ❗ </summary>   
<div markdown="1">
   
   + .col-xs-* : 항상 가로로 배치
   + .col-sm-* : 768px이하에서 세로로 표시
   + .col-md-* : 992px이하에서 세로로 표시
   + .col-lg-* : 1200px이하 에서 세로로 표시
   + [도움받은 다른 사람의 블로그 ✨](https://unikys.tistory.com/371)
   
</div>
</details> 

<details>
<summary>django 프로젝트 AWS EC2 서버배포하기 ❗ </summary>   
<div markdown="1">
   
   + [도움받은 다른 사람의 블로그 ✨](https://nerogarret.tistory.com/46?category=800142)
   
</div>
</details> 

