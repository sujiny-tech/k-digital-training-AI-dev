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
> 예전에 문제를 풀때, 나는 정렬을 이용해서 풀이했음 (아래 코드)
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
1. 탐욕법(Greedy Algorithm)
   + 알고리즘의 각 단계마다 최적이라고 생각되는 것을 선택하는 방법
   + 현재의 선택이 최종 답의 최적성을 해치지않을 때, 탐욕법으로 최적해 도출 가능

2. 탐욕법 적용 가능한가?
   + 빌려줄 학생들을 "정해진 순서"로 살펴야되고, "동일한 순서"로 우선하여 빌려줄 방향을 정해야함
   
3. 문제 해결 방법 (1)
   + 학생의 수는 기껏해야 30!
   + 학생 수만큼 배열 확보하고, 여기에 각자 갖고 있는 체육복 수 기록
   + 번호 순서대로 "스캔"하면서 빌려줄 관계를 정한다.
      + 여벌을 갖고온 학생 처리 : reserve 배열 길이에 비례
      + 체육복을 잃어버린 학생 처리 : lost 배열 길이에 비례
      + 체육복 빌려주기 : 전체 학생 수(n)에 비례
      > 알고리즘의 복잡도 = O(n)
   + 해당 풀이 코드는 아래와 같다.
   ```python
   def solution(n, lost, reserve):
       uni=[1]*(n+2) #앞뒤 1칸씩 더 늘려서 : 인덱스 에러를 피하기 위해 
       
       #체육복 갖고 있는 학생들 체크 : O(n) - 여벌을 갖고있는 학생수 1명이상 n명이하
       for i in reserve:
           uni[i]+=1
           
       #체육복 잃어버린 학생들 체크 : O(n) - 도난당한 학생수 1명이상 n명이하
       for i in lost:
           uni[i]-=1
           
       #시작은 1번부터 ~ n번까지 : O(n)
       for i in range(1, n+1):
           #앞 학생이 체육복 없고, 현재 학생이 2개 갖고 있을 때
           if uni[i-1]==0 and uni[i]==2:
               uni[i-1:i+1]=[1,1] #앞번호 학생에게 빌려준다.
               
           #뒷 번호 학생이 체육복이 없고, 현재 학생이 2개 갖고 있을 때 
           elif uni[i+1]==0 and uni[i]==2:
               uni[i:i+2]==[1,1] #뒷 번호 학생에게 빌려준다.
               
       #체육복 갖고 학생들의 수 (앞뒤1칸씩 늘린거 빼고) : O(n)
       return len([x for x in uni[1:-1] if x>0])
   ```
   
4. 문제 해결 방법 (2)
   + 만약 전체 학생수가 매우 크고, 여벌의 체육복을 갖고온 학생이 매우 적다면?
   + 여벌의 체육복을 갖고 온 학생들의 번호를 정렬하고, 이를 하나하나 순서대로 살펴보면서 빌려줄 수 있는 다른학생을 찾아서 처리한다.
      + 여벌의 체육복을 갖고 온 학생들(k)의 번호 정렬 : O(klogk) 
      + 빌려줄 수 있는 다른 학생을 찾기 -> 해시를 적용해서 상수 시간에 처리가능 : O(k)xO(1)
      > 알고리즘의 복잡도 = O(klogk)
   + 해당 풀이 코드는 아래와 같다.
      + set 이용 ! > [set 정리된 다른 사람의 블로그](https://m.blog.naver.com/PostView.nhn?blogId=lovespreads&logNo=221359758054&proxyReferer=https:%2F%2Fwww.google.com%2F)
      + set은 해시 테이블로 구현되어있어서 키를 접근할 때 상수시간걸림
      > dictionary는 키에 대해 값이 매핑되어있는 반면, set은 어떤 원소가 속해있느냐 아니냐를 판단해주는 자료구조
      ```python
      def solution(n, lost, reserve):
          #일반적으로 set을 구성하려고 하는 배열의 길이에 비례
          s=set(lost)&set(reserve) #가져왔는데 잃어버린 학생들
          l=set(lost)-s #현재 체육복 1개도 없는 학생들
          r=set(reserve)-s #여벌 체육복 있는 학생들
          
          #이전 방법에 비해, r의 학생수(k명)만큼 반복 : sorted(r)=> O(klogk)
          #따라서 O(klogk)
          for x in sorted(r):
              if x-1 in l:
                  l.remove(x-1)
              elif x+1 in l:
                  l.remove(x+1)
                  
          return n-len(l)
      ```
   
      + 기존에 풀었던 나의 코드...
      ```python
      def solution(n, lost, reserve):
          #이 부분만 다름
          set_lost=set(lost)-set(reserve) #lost에서 reserve와 겹치는 원소 빼기->정말 체육복없는 학생들
          set_reserve=set(reserve)-set(lost) #reserve에서 lost와 겹치는 원소 빼기->정말 여벌 체육복이 있는 학생들
          
          for i in set_reserve:
              if i-1 in set_lost:
                  set_lost.remove(i-1)
              elif i+1 in set_lost:
                  set_lost.remove(i+1)
                  
          return n-len(set_lost)
      ```
      
------------------------------------------------------------------

## #3. [가장 큰 수](https://programmers.co.kr/learn/courses/30/lessons/42746)
1. 문제 해결 방법
   + 빈 문자열로 수를 초기화 ""
   + 가장 크게 만들수 있는 수 고르기 O(n^2) > __크게 만드는 것 우선으로 정렬 O(nlogn)!__
   + 그 수를 현재 수에 이어 붙이기
   + 모든 수를 다 사용할때까지 반복
   
   + 해당 풀이 코드는 아래와 같다.
   ```python
   def solution(numbers):
       #문자열로 변환/ numbers 배열의 크기가 n일 때, O(n)
       num=[str(x) for x in numbers]
       
       #원소가 0이상 1,000이하이므로 원소는 최대 4자리수, 내림차순으로 정렬 O(nlogn)
       num.sort(key=lambda x: (x*4)[:4], reserve=True)
       
       #000일 때, 0으로 처리해야함 > 방법 1 !!
       if num[0]=='0':
           ans='0'
       else:
           ans=''.join(num)
           
       #000일 때, 0으로 처리해야함 > 방법 2
       #ans=str(int(''.join(num)))
       
       return ans
   ```
   > 전체 알고리즘 복잡도 = O(nlogn)
   
------------------------------------------------------------------

## #4. [큰 수 만들기](https://programmers.co.kr/learn/courses/30/lessons/42883)
1. 문제 해결 방법 (탐욕법)
   + 앞자리에서부터 하나씩 담다가, 큰수가 나오면 담았던 작은수들 빼주기 (빼주는 숫자개수 k 생각하면서)
   + 주의 : 주어진 숫자 자체가 큰수라면 뒤에서 k개 빼줘야함
   + 가장 단순한 방법 : 모든 조합을 따져서 큰 수를 고르는 것 > 너무 가짓수가 많음 (combinatorial explosion)
   + 위에서 설명한 방법 : 자릿수가 n이라 하면, n에 비례 O(n)
    > 각각 자리의 수에서 더해지는거나 빠지는거 기껏해야 1번 (구체적으로 말하면 n의 2배에 가까울 수 있음)
    
   + 해당 풀이 코드는 아래와 같다.
   ```python
   def solution(number, k):
       #파이썬 자료형에 대한 다른 사람의 블로그 > [파이썬 자료형](https://hyeonakim.github.io/python/2018/07/22/python-structure-8/)
       #리스트는 가변:mutable
       #문자열(string)은 불변:immutable
       collect=[] #숫자를 담기 위해
       
       #number길이가 n이라 하면, for문 횟수에 따른 알고리즘 복잡도 : O(n)
       for i, num in enumerate(number):
           #collect에 숫자가 담아져있고, 현재 숫자가 클 때(담겨진 마지막 숫자보다), 숫자를 빼는 횟수 k가 0보다 크면,
           while len(collect)>0 and collect[-1]<num and k>0:
               collect.pop() #담겨진 마지막 숫자 꺼내기
               k-=1 #숫자 빼는 횟수 -1
               
           #더이상 뺄 횟수가 x
           if k==0:
               collect+=list(number[i:]) #그 뒤에 있는 숫자 붙이기
               break
               
           collect.append(num)
           
       #k가 남아있으면, 뒤에서 k개 버리기
       collect=collect[:-k] if k > 0 else collect
       
       return ''.join(collect)
   ```


