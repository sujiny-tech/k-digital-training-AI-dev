# 스택의 응용

+ 중위 표기법(Infix Notation) : 일상에서 사용하는 수식의 표기법, 연산자가 피연산자들의 사이에 위치
  > ex) (A+B) * (C+D)
+ 후위 표기법 (Postfix Notation) : 연산자가 피연산자들의 뒤에 위치
  > ex) AB+CD+*
  > ex) 중위 (A+(B-C)) * D -> 후위 ABC-+D*
  > ex) 중위 A * (B-(C+D)) -> 후위 ABCD+-*
  
### 연습문제 1. 중위 표현 수식 --> 후위 표현 수식

---------------------
#### 알고리즘의 흐름
> 왼쪽부터 한글자씩 읽어서
> 1. 피연산자이면 그냥출력
> 2. (이면 스택에 push
> 3. ) 이면 (이 나올때까지 스택에서 pop
> 4. 연산자이면 스택에서 이보다 높거나 같은 우선순위것들을 pop, 그리고 이 연산자는 스택에 push
> 5. 스택에 남아있는 연산자 모두 pop

#### 힌트
> 스택의 맨위에있는 연산자와 우선순위비교 : 스택 peek() 연산 이용 (꺼내지않고)
> 스택에 남아있는 연산자 모두를 pop()하는 순환문 : while not opStack.isEmpty():로 구성
---------------------
```python
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    S=list(S)
    
    while S:
        s=S.pop(0)
        if s.isalpha():
            answer+=s
        else:
            if s=="(":
                opStack.push(s)
            elif s==")":
                while opStack:
                    if opStack.peek()=="(":
                        opStack.pop()
                        break
                    answer+=opStack.pop()
            else:
                if opStack.isEmpty():
                    opStack.push(s)
                else:
                    if prec[s]<=prec[opStack.peek()]:
                        answer+=opStack.pop()
                    opStack.push(s)
    while not opStack.isEmpty():
        answer+=opStack.pop()
    return answer
 ```
 
 #### 테스트 케이스 7,8에 대해 실패 -> 다시 풀어보기
