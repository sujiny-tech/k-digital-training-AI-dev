# 코딩테스트 연습
> 문제 출처 : [프로그래머스](https://programmers.co.kr/learn/challenges)

## #1. [완주하지 못한 선수](https://programmers.co.kr/learn/courses/30/lessons/42576)
1. 자료구조/알고리즘의 선택
   + 만약 이름 대신 번호가 주어졌다면, 선형 배열(linear array)
   + 번호말고 다른것(문자열)로 접근할수있는 좋은 자료구조는 없나? : 해시(Hash)
      + 키(key)값을 해시함수(hash function)를 통해 해시테이블(hash table)로 넣어줌
      + 해시 버킷(hash bucket) : 해시테이블의 칸
      + 해시 함수(hash function) : 가급적이면!! 서로 다른 해시 버킷에 들어갈수있도록 보장해주는 함수
      + 해시 충돌(hash function) : 다른 키값이 같은 해시버킷으로 들어갈때 충돌됨.
      
2. python에서의 사전(dictionary)
: python에서는 dictionary을 구현할때 내부적으로 해시이용
> 사전의 원소들에 대해서 해시를 이용해서 O(1) 시간에 접근 가능!

+ 해시를 적용한 풀이해보자.
```python
def solution(participant, completion):
    d={}
    
    #for 문은 paticipant 배열의 크기에 비례 (사전이 해시로 구현되있어서)
    for x in participant:
        d[x]=d.get(x,0)+1  #get 메서드 : x가 존재하면 해당값을, 그렇지않으면 0을 리턴
    
    #이또한 completion 배열의 크기에 비례
    for x in completion:
        d[x]-=1
        
    #사전에 들어있는 모든 원소를 꺼내는 작업이니까 사전의 크기에 비례
    answer=[k for k, v in d.items() if v!=0]
    return answer[0]
```
> 배열의 크기가 N일때, 이에 비례하는 O(N) linear time 복잡도를 가짐.

+ 정렬을 이용한 풀이 가능하다.
> 예전에 문제를 풀때, 나는 정렬을 이용해서 풀이했는데 이는 아래 코드와 같다.
```python
def solution(participant, completion):
    answer = ''
    completion.append("z"*20)
    
    for p_, c_ in zip(sorted(participant), sorted(completion)):
        if p_!=c_:
            return p_
        
    return answer
```
- 정렬을 이용하면, O(NlogN) ... 
> 테스트는 통과하지만, 현실적으로 O(NlogN)과 O(N)의 복잡도를 갖는 알고리즘 실행시간을 일반적으로 변별하기 힘들어서 통과하는 것.

- 문제의 요점
> 해시를 통해 키값으로 원소 접근이 상수시간으로 가능하다는 점을 활용하여 알고리즘의 복잡도가 배열의 크기에 비례하는 알고리즘을 구성하는 것이 이 문제의 의도
   
------------------------------------------------------------------

## #2. [체육복](https://programmers.co.kr/learn/courses/30/lessons/42862)
1. 자료구조/알고리즘의 선택
   + 

2. 탐욕법(Greedy Algorithm)
   + 알고리즘의 각 단계마다 최적이라고 생각되는 것을 선택하는 방법
   + 현재의 선택이 최종 답의 최적성을 해치지않을 때, 탐욕법으로 최적해 도출 가능

3. 탐욕법 적용 가능한가?
   + 빌려줄 학생들을 "정해진 순서"로 살펴야되고, "동일한 순서"로 우선하여 빌려줄 방향을 정해야함
   
4. 문제 해결 방법 (1)
   + 학생의 수는 기껏해야 30!
   + 학생 수만큼 배열 확보하고, 여기에 각자 갖고 있는 체육복 수 기록
   + 번호 순서대로 "스캔"하면서 빌려줄 관계를 정한다.
      + 여벌을 갖고온 학생 처리 : reserve 배열 길이에 비례
      + 체육복을 잃어버린 학생 처리 : lost 배열 길이에 비례
      + 체육복 빌려주기 : 전체 학생 수(n)에 비례
      > 알고리즘의 복잡도 = O(n)
   
5. 문제 해결 방법 (2)
   + 만약 전체 학생수가 매우 크고, 여벌의 체육복을 갖고온 학생이 매우 적다면?
   + 여벌의 체육복을 갖고 온 학생들의 번호를 정렬하고, 이를 하나하나 순서대로 살펴보면서 빌려줄 수 있는 다른학생을 찾아서 처리한다.
      + 여벌의 체육복을 갖고 온 학생들(k)의 번호 정렬 : O(klogk) 
      + 빌려줄 수 있는 다른 학생을 찾기 -> 해시를 적용해서 상수 시간에 처리가능 : O(k)xO(1)
      > 알고리즘의 복잡도 = O(klogk)
      
+ 탐욕법으로 풀이한 코드는 다음과 같다.
```python


```
   
   
