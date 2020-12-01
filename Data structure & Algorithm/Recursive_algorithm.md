# 재귀 알고리즘 (Recursive algorithm)
+ 주어진 문제에 대해, 같은 종류에서의 쉬운 문제의 답을 활용해서 풀수있는 방법
+ 즉, 같은 알고리즘의 반복을 통해 원하는 답을 얻어내는 방법
+ 문제를 재귀적으로 해결하기 위해서는 어느 조건에서 종료할지 분명하게 해야함

--------
#### 연습 문제 1. 피보나치 수열 (재귀적)

```python
def solution(x):
    #recursive solution
    
    answer = 0
    
    if x<2:
        return x
    else:
        answer=solution(x-1)+solution(x-2)
    
    return answer
```
--------

### 연습 문제 2. 피보나치 수열 (반복적)

```python
def solution(x):
    #iterative solution
    
    answer=0
    
    arr=[0,1]
    
    if x<2:
        return x
    
    for i in range(2, x+1):
        arr.append(arr[i-1]+arr[i-2])
        
    return arr[-1]
```
