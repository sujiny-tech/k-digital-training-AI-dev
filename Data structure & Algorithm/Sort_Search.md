# 정렬 (Sort)
+ 여러 데이터들을 주어준 기준에 맞춰 정리하는 작업
+ python에서는 리스트에 내장된 정렬 함수와 메서도 존재
   1. 파이썬 내장 함수 sorted(list_name, key=lambda x: condition, reverse=boolean)
   2. 리스트 메서드 list.sort(key=lambda x: condition, reverse=boolean)

# 탐색(Search)
+ 여러 데이터들을 특정 원소를 찾아내는 작업
+ 기본적인 두가지 탐색 방법
   1. 선형 탐색(linear search) 
    : 순차적으로 모든 원소들을 탐색하여 원하는 원소를 찾아냄.
     배열의 길이에 비례하는 시간이 걸리므로, 최악의 경우 모든 원소를 검사함.
   2. 이진 탐색(binary serach) : 이미 정렬된 배열에서만 적용가능함. 
     정렬되었기 때문에, 중간값을 기반으로 값을 비교하는 과정을 반복해서 원하는 원소를 찾아낼수있음.
   
--------
#### 연습 문제 1. 이진탐색

1. 선형 탐색으로 구현했을때, 런타임 에러 (시간 초과) 발생
```python
def solution(L, x):
    answer = -1
    linear search
    for i in range(len(L)):
        if L[i]==x:
            return i
        if L[i]>x:
            return -1   
    return answer
```
--------

2. 이진 탐색으로 구현했을 때, 선형 탐색인 경우보다 효율적임.
```python
def solution(L, x):
    start, end=0, len(L)-1
    while start<=end:
        mid=(end+start)//2
        if L[mid]<x:
            start=mid+1
        elif L[mid]>x:
            end=mid-1
        else:
            return mid
    return -1
```
