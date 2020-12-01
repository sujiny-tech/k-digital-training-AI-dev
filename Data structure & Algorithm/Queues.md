# 큐(Queue)
+ 자료 (data element)를 보관할 수 있는 선형 구조
+ 선입선출 (FIFO=First-In First-Out) 특징을 갖는 선형자료구조 : 줄서기와 동일
+ 한 쪽끝에서 밀어넣는 .enqueue 연산
+ 반대쪽에서 뽑아꺼내는 .dequeue 연산

## 큐의 추상적 자료구조 구현
1. 배열(array)을 이용하여 구현 : python 리스트와 메서드 이용
2. 연결리스트(linked list)를 이용하여 구현 : 양방향 연결리스트 이용

## 큐의 연산의 정의
1. size() : 현재 큐에 들어있는 데이터의 원소 수를 구함
2. isEmpty() : 현재 큐가 비어 있는지를 판단
3. enqueue(x) : 데이터 원소 x를 큐에 추가
4. dequeue() : 큐의 맨 앞에 저장된 데이터 원소 반환/제거
5. peek() : 큐의 맨 앞에 저장된 데이터 원소를 반환 (제거x)

## 배열로 구현한 큐의 연산 복잡도
1. size() : O(1)
2. isEmpty() : O(1)
3. enqueue() : O(1)
4. dequeue() : O(n) !!
5. peek() : O(1)
> 배열로 구현시, dequeue()를 통해 데이터 원소를 제거하면 뒤에 있는 원소들을 다시 앞으로 당겨줘야함. 
즉, 최악의 경우 n개의 원소를 담은 배열에서 맨앞의 원소를 제거할때, 전체 원소를 다시 앞으로 옮겨줘야함.

----------------

#### 예제 1. 배열로 큐 구현
```python
class ArrayQueue:
    def __init__(self, item):
        self.data=[]
    
    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        return self.size()==0
        
    def enqueue(self, item):
        self.data.append(item)
    
    def dequeue(self):
        return self.data.pop(0)
    
    def peek(self):
        return self.data[0]
```

----------------
#### 연습 문제 1. 양방향 리스트르로 큐 구현
```python
class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

#이전에 연습문제에서 풀어봄.
class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError('Index out of range')

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)


    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.nodeCount += L.nodeCount


class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return 
self.data.nodeCount

    def isEmpty(self):
        return 
self.data.nodeCount==0

    def enqueue(self, item):
        node = Node(item)
        
self.data.insertAt(self.size()+1, node)

    def dequeue(self):
        return 
self.data.popAt(1)

    def peek(self):
        return 
self.data.head.next.data

def solution(x):
    return 0
```
---------------------------------------------

# 큐의 활용
+ 자료를 생성하는 작업과 그 자료를 이용하는 작업이 비동기적으로 일어나는 경우, 연결하기 위해 사용
+ 자료를 생성(이용)하는 작업이 여러 곳에서 일어나는 경우
+ 자료를 처리해서 새로운 자료를 생성하고, 나중에 그 자료를 또 처리해야하는 작업의 경우

# 환형 큐 (Circular Queue)
+ 정해진 개수의 저장 공간을 빙 돌려가며 이용 (큐 길이를 기억하고 있어야 저장공간 확인가능)

## 환형 큐의 연산의 정의
1. size() : 현재 큐에 들어있는 데이터의 원소 수를 구함
2. isEmpty() : 현재 큐가 비어 있는지를 판단
3. isFull() : 큐에 데이터 원소가 꽉 차 있는지를 판단 ##
3. enqueue(x) : 데이터 원소 x를 큐에 추가
4. dequeue() : 큐의 맨 앞에 저장된 데이터 원소 반환/제거
5. peek() : 큐의 맨 앞에 저장된 데이터 원소를 반환 (제거x)

#### 연습문제 2. 배열로 구현한 환형 큐
```python
class ArrayQueue:
    def __init__(self, n):
        self.maxCount=n
        self.data=[None]*n
        self.count=0
        self.front=-1
        self.rear=-1
    
    #rear, front를 증가하는데 최대원소수를 넘을수있으므로 처리해줘야함.
    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.count==0
        
    def isFull(self):
        return self.count==self.maxCount
    
    def enqueue(self, item):
        if self.isFull():
            raise IndexError("Queue full")
            
        self.rear=(self.rear+1)%self.maxCount
        self.data[self.rear]=x
        self.count+=1
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue empty")
        self.front=(self.front+1)%self.maxCount
        x=self.data[self.front]
        self.count-=1
        return x
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Queue empty")
        return self.data[(self.front+1)%self.maxCount]
```
----------------------------------
# 우선순위 큐 (Priority Queue)
+ 큐가 FIFO 방식을 따르지 않고, 원소들의 우선순위에 따라 큐에서 빠지는 방식
+ 운영체제의 CPU 스케쥴러에 활용됨 (신기하니까 찾아봐야지)

## 우선순위 큐의 구현

두가지 방식 가능
1. Enqueue 할 때, 우선순위 순서 유지하도록 하는 방법
2. Dequeue 할 때, 우선순위 높은 것을 선택하는 방법
> 1번이 조금 더 유리 : 만약 큐에 무작위 순서로 있다고 할때, 모든 데이터의 상태를 살펴봐야함. 1번처럼 우선순위 순대로 나열되어있다면, 적절한 위치를 찾을때 모든 데이터의 상태를 살펴보지 않아도 되므로 1번이 조금 더 유리.

두가지 자료구조 사용가능
1. 선형 배열 이용
3. 연결 리스트 이용
> 시간적으로 연결리스트가 유리. enqueue 할 때, 중간에 데이터 원소를 집어넣을때 상대적으로 선형배열보다 유연함. 그러나 메모리측면(공간적)에서는 선형배열이 더 유리. 그러나 대부분 시간적으로 유리한 것을 선택한다!

#### 연습문제 3. 양방향 연결리스트로 우선순위 큐의 enqueue 메서드 구현하기
```python
#이전에 공부했던 부분
class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None

#양방향 연결리스트
class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)


    def concat(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail

        self.nodeCount += L.nodeCount
        
#여기서부터
class PriorityQueue:
    def __init__(self, x):
        self.queue=DoublyLinkedList()
    
    #양방향 연결 리스트에서의 getAt()메서드 이용 x
    #getAt() : pos까지 칸을 하나하나씩 카운트하면서 찾았었음. (호출될때 매번 처음부터 카운트해야함)
    def enqueue(self, x):
        newNode=Node(x)
        cur=self.queue.head #어디서 시작할건가
        while cur.next!=self.queue.tail and x<cur.next.data: #끝을 만나기전에, 우선순위(작은수가 우선순위 높음):
            cur=cur.next
        self.queue.insertAfter(curr, newNode)
    
    def dequeue(self):
        return self.queue.popAt(self.queue.getLenth())
    
    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data
        
```
