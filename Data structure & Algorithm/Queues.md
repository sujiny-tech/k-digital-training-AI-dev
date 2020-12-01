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
