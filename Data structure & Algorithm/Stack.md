# 스택(Stack)
+ 자료(data element)를 보관할 수 있는 (선형) 구조
+ **후입선출**(LIFO; Last-In First-Out) 특징을 가지는 선형 자료구조
+ 예) 하노이의 탑, 쌓여져있는 접시 탑...
+ 스택 언더플로우(stack underflow) : 비어있는 스택에서 데이터 원소를 꺼내려 할때 발생하는 오류
+ 스택 오버플로우(stack overflow) : 꽉 찬 스택에 데이터 원소를 넣으려 할때 발생하는 오류

+ 스택의 연산
    + size() : 현재 스택에 들어있는 데이터 원소의 수?
    + isEmpty() : 현재 스택이 비어 있는가?
    + push(x) : 데이터 원소 x를 스택에 추가
    + pop() : 스택의 맨 위에 저장된 데이터 원소를 제거/반환
    + peek() : 스택의 맨위에 저장된 데이터 원소를 반환
    
+ 배열(array)을 이용하여 구현
   + python 리스트와 메서드들을 이용해서 구현 가능
   ```python
   class ArrayStack:
       def __init__(self):
           self.data=[]
       
       def size(self):
           return len(self.data) #스택의 크기 반환
       
       def isEmpty(self):
           return self.size()==0 #비어있으면 true, 아니면 false
           
       def push(self, item):
           self.data.append(item) #데이터 원소 추가
       
       def pop(self):
           return self.data.pop() #맨 끝에 있는 데이터 원소 삭제/반환
       
       def peek(self):
           return self.data[-1] #맨 마지막 원소 반환(삭제x)
   ```
   
+ 연결리스트(linked list)를 이용하여 구현
   + 앞서 구현한 양방향 연결리스트를 통해 구현 수행
   ```python
   from doublylinkedlist import Node #이전에 구현한 클래스 import
   from doublylinkedlist import DoublyLinkedList 
   class LinkedListStack:
   
       def __init__(self):
           self.data=DoublyLinkedList() #양방향 연결리스트로 데이터 세팅
       
       def size(self):
           return self.data.getLength() #해당 데이터의 개수(리스트의 길이)
       
       def isEmpty(self):
           return self.size()==0 #비어있으면 true, 아니면 false
           
       def push(self, item):
           node=Node(item) #새로운 노드 생성
           self.data.insertAt(self.size()+1, node) #뒤에 추가
       
       def pop(self):
           return self.data.popAt(self.size()) #맨 끝 데이터 꺼내서 반환
       
       def peek(self):
           return self.data.getAt(self.size()).data #맨 끝 데이터 삭제하지않고 반환
   ```

### 연습문제 1. 수식의 괄호 검사(스택)
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


def solution(expr):
    match = {')': '(',
             '}': '{',
             ']': '['}
             
    S = ArrayStack() #배열로 만든 스택
    
    #해당 문자열에 대해
    for c in expr:
        #열린 괄호라면 스택에 쌓고
        if c in '({[':
            S.push(c)
        #닫힌 괄호라면
        elif c in match:
            #스택이 비어있으면, 짝이 안맞으니까 올바르지 않음
            if S.isEmpty():
                return False
            else:
                #스택에서 하나꺼내서, 짝이 맞는지 확인
                t=S.pop()
                if t != match[c]:
                    return False
                    
    #스택이 비어있다면 짝이 맞는 올바른 괄호/아니면 잘못된 괄호                
    return S.size()==0  
```
--------------------------


# 스택의 응용

+ 중위 표기법(Infix Notation) : 일상에서 사용하는 수식의 표기법, 연산자가 피연산자들의 사이에 위치
  > ex) (A+B) * (C+D)
+ 후위 표기법 (Postfix Notation) : 연산자가 피연산자들의 뒤에 위치
  > ex) AB+CD+*
  > ex) 중위 (A+(B-C)) * D -> 후위 ABC-+D*
  > ex) 중위 A * (B-(C+D)) -> 후위 ABCD+-*
  
### 연습문제 2. 중위 표현 수식 --> 후위 표현 수식

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
                    ##이부분에 대해서 수정함.(기존에 반복수행하지 않음)
                    while opStack.size():
                        #우선순위 비교: 맨 위값보다 우선순위 낮으면
                        if prec[s]<=prec[opStack.peek()]:
                            answer+=opStack.pop()
                        else:
                            break
                    opStack.push(s)
                    
    while not opStack.isEmpty():
        answer+=opStack.pop()
    return answer
 ```
 
 #### 테스트 케이스 7,8에 대해 실패 -> 다시 풀어보기 !!! (해결)
 --------------------------------------------------
 
### 연습 문제 3. 후위 표현 수식 --> 중위 표현 수식

---------------------
 #### 알고리즘의 흐름
 > 왼쪽부터 한글자씩 읽어서
 > 1. 피연산자이면 스택에 push
 > 2. 연산자이면 스택에 pop-> (1), pop->(2), (2)연산(1) 계산후 스택에 push
 > 3. 수식의 끝에 도달하면 스택에서 pop-> 

 #### 힌트
 > infixToPostfix -> input parmeter=list
 > tokens=split 공백처리, 리스트 형태로 저장
 > postfix : 후위표현식으로 표현된 수식들
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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    while tokenList:
        c=tokenList.pop(0)
        if type(c) is int:
            postfixList.append(c)
        else:
            if c=="(":
                opStack.push(c)
            elif c==")":
                while opStack:
                    if opStack.peek()=="(":
                        opStack.pop()
                        break
                    postfixList.append(opStack.pop())
            else:
                if opStack.isEmpty():
                    opStack.push(c)
                else:
                    if prec[c]<=prec[opStack.peek()]:
                        postfixList.append(opStack.pop())
                    opStack.push(c)
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    valStack=ArrayStack()
    
    for token in tokenList:
        if type(token) is int:
            valStack.push(token)
            
        elif token=='*':
            num1=valStack.pop()
            num2=valStack.pop()
            valStack.push(num1*num2)
            
        elif token=='/':
            num1=valStack.pop()
            num2=valStack.pop()
            valStack.push(num2/num1)
            
        elif token=='-':
            num1=valStack.pop()
            num2=valStack.pop()
            valStack.push(num2-num1)
            
        elif token=='+':
            num1=valStack.pop()
            num2=valStack.pop()
            valStack.push(num2+num1)
        
    return valStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
 ```
