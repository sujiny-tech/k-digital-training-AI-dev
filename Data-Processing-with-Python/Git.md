## Git 이란

- 분산 버전관리 시스템

   + [참고-wiki](https://ko.wikipedia.org/wiki/%EA%B9%83_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4))
- - - - - - - -

## Git 시작하기

<img src="https://user-images.githubusercontent.com/72974863/102103246-1684e700-3e70-11eb-85b7-d36438a921dd.png" width="50%" hegiht="50%">

- git config 설정방법

    ✔ git config --list (config 정보 출력)

    ✔ git config --global user.name "name"

    ✔ git config --global user.email "email"

    ✔ git config --unset (--global) user.name/user.email (사용자 이름/이메일삭제)

- 로컬 저장소 생성(CLI 환경)

    ✔ git init

    <img src="https://user-images.githubusercontent.com/72974863/102103274-21d81280-3e70-11eb-94be-52969e8426fa.png">

- git 상태 확인

    ✔ git status

    <img src="https://user-images.githubusercontent.com/72974863/102103311-31eff200-3e70-11eb-8677-8f2ab13179df.png">

- git 파일 생성(혹은 수정)해서 commit에 반영할 파일 지정

    ✔ git add <file name>

    <img src="https://user-images.githubusercontent.com/72974863/102103355-3f0ce100-3e70-11eb-9f92-bed5a8c76c2e.png">

- git 로컬 저장소에 commit 남기기

    ✔ git commit -m <커밋 메세지>

    <img src="https://user-images.githubusercontent.com/72974863/102103412-4f24c080-3e70-11eb-80c2-6120d3784f74.png">

- git log 확인하기

    ✔ git log

    <img src="https://user-images.githubusercontent.com/72974863/102103457-5cda4600-3e70-11eb-91d9-fcb8f2039bc5.png">


- - - - - - - -

## Git의 branch

- 코드의 흐름을 분산 - 가지치기 - 병합
- git branch 생성

    ✔ git branch <branch_name>

    <img src="https://user-images.githubusercontent.com/72974863/102103723-ad51a380-3e70-11eb-8242-dc2e0c633552.png">

- git branch 전환

    ✔ git checkout <branch_name>

    <img src="https://user-images.githubusercontent.com/72974863/102103770-bb9fbf80-3e70-11eb-9872-e7a58109aa5a.png">

- git branch 병합하기

    ✔ git merge <branch_name>

    <img src="https://user-images.githubusercontent.com/72974863/102103795-c5292780-3e70-11eb-9c3b-0b5cbe71bc8f.png">

- git branch 삭제하기

    ✔ git branch -d <branch_name>

    <img src="https://user-images.githubusercontent.com/72974863/102103822-ceb28f80-3e70-11eb-86a6-a703cfb74bde.png">


- - - - - - - -

## Git과 Github

- 깃허브 master→main변경

    ✔ git branch -M main

- 원격 저장소 별칭 지정(추가)

    ✔ git remote add <remote_repository_name> <remote_repository_address>

    <img src="https://user-images.githubusercontent.com/72974863/102103959-f9044d00-3e70-11eb-98fe-1078dc4dda28.png">

- 원격 저장소 삭제

    ✔ git remote remove <별칭>

    <img src="https://user-images.githubusercontent.com/72974863/102104007-07eaff80-3e71-11eb-8a17-f6b1b12d51b6.png">

- 지정된 원격 저장소 별칭/주소 확인

    ✔ git remote -v
    
- 원격 저장소에 branch push하기

    ✔ git push <remote_repository_name> <branch_name>
    
- git 원격 저장소에서 로컬 저장소로 복사해오기

    ✔ git clone <remote_repository_address> <directory_name>

    <img src="https://user-images.githubusercontent.com/72974863/102103881-df630580-3e70-11eb-828e-7137ec5fde6a.png">

- - - - - - - - -

## Fork한 repository 업데이트 
- 먼저 fork한 원격 저장소(원본 저장소) 추가

    ✔ git remote add upstream <fork한 원본 저장소 주소>
       
    <img src="https://user-images.githubusercontent.com/72974863/102783926-ff4d7880-43de-11eb-8e7f-1b0db172dfcf.png">
   
       
- 원본 저장소(upstream)의 최신 내용 가져오기

    ✔ git fetch upstream
       
    <img src="https://user-images.githubusercontent.com/72974863/102784175-59e6d480-43df-11eb-971b-229745c0b3ee.png">

- 원본 저장소와 로컬 저장소(내가 가져온 저장소) 병합
   
    ✔ git merge <병합하고 싶은 branch>   
    
     - 원하는 branch에 병합      
       
       <img src="https://user-images.githubusercontent.com/72974863/102787300-35412b80-43e4-11eb-89b8-1cd96fd46ab4.png">  
          
- 변경할 파일이 있거나, 추가할 파일 있으면 진행 후 commit 남기기(git add/git commit -m)

- fork해서 가져온 내 원격 저장소(origin)에 반영해주기(push)
   
    ✔ git push origin <병합하고 싶은 branch>   
