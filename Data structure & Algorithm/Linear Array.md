# 선형 배열
+ 데이터들이 선(line)처럼 일렬로 늘어선 형태
+ 보통 프로그래밍에서 배열(array)은 같은 종류(int, str,...)의 데이터를 담아놓은 그릇
+ python에서는 서로 다른 종류의 데이터를 담을수있는 리스트(list)라는 데이터형 존재

## python 리스트 연산

리스트 길이에 관계없이 빠르게 실행가능한 연산
1. 원소 덧붙이기 .append()
2. 원소 하나를 꺼내기 .pop()

리스트 길이에 비례해서 시간이 걸리는 연산
1. 원소 삽입하기 .insert()
2. 원소 삭제하기 .del()
--------
#### 연습 문제 1. 정렬된 리스트에서 원소 삽입

```python
def solution(L, x):
    index=0
    for i in range(len(L)):
        if L[i]>=x:
            index=i
            break
    if index!=0:
        L.insert(index, x)
    else:
        if L[-1]<x:
            L.aapend(x)
        else:
            L.insert(0, x)
     return L
```
--------

### 연습 문제 2. 리스트에서 원소 찾아내기

```python
def solution(L, x):
    answer = []
    for i in range(len(L)):
        if L[i]==x:
            answer.append(i)
    if answer==[]:
        return [-1]
    else:
        return answer
```
