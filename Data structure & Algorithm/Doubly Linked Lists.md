# 양방향 연결 리스트(Doubly Linked Lists)
+ **양방향**으로 노드들이 **앞/뒤로 연결**되어있는 자료구조
+ 이전의 연결리스트에서는 한 방향으로 노드들을 탐색할 수 있었지만, 양방향 연결리스트는 노드에 대해 양방향으로 탐색가능.
+ Node 의 구조 확장
  ```python
  class Node:
      def __init__(self, item):
          self.data=item
          self.prev=None #뒤뿐만 아니라 앞으로도 
          self.next=None 
  ```
 + 리스트의 처음과 끝에 dummy node를 둔다.
    + head, tail 둘다 dummy node를 둠 -> 데이터를 담은 노드들이 모두 같은 형태로 이뤄짐(장점)
    
+ 양방향 연결 리스트의 초기화
  ```python
  class DoublyLinkedList:
      def __init__(self,item):
          self.head=Node(None)  #dummy node
          self.tail=Node(None)  #dummy node
         self.head.prev=None
          self.head.next=self.head
          self.tail.next=None
  ```
+ 리스트 순회(traversal)
  ```python
  def traverse(self):
      result=[]
      curr=self.head
      
      #tail도 dummy node가 들어있기 때문에 조건 변경해줌
      while curr.next.next:
          curr=curr.next
          result.append(curr.data)
          
      return result
  ```
  
+ 리스트 역순회(reverse)
  ```python
  def reverse(self):
      result=[]
      curr=self.tail
      
      #tail을 시작으로 거꾸로 순회
      while curr.prev.prev:
          curr=curr.next
          result.append(curr.data)
          
      return result
  ```
  
+ 원소의 삽입(insertion)
  ```python
  def insertAfter(prev, newNode):
      next=prev.next #이전의 다음
      newNode.prev=prev #새로운 노드의 이전은 prev
      newNode.next=next #새로운 노드의 다음은 next
      prev.next=newNode #prev의 다음은 새로운 노드(서로 연결)
      next.prev=newNode #next의 이전은 새로운 노드(서로 연결)
      self.nodeCount+=1 #카운트 +1
      
      return True
  ```
  
+ 특정 원소 얻어내기
  ```python
  def getAt(self, pos):
      if pos<0 or pos>self.nodeCount:
          return None
      
      #오른쪽에 있으면 tail로 찾아가기
      if pos>self.nodeCount//2:
          i=0
          curr=self.tail
          while i<self.nodeCount-pos+1:
              curr=curr.prev
              i+=1
              
      #왼쪽에 있으면 head로 찾아가기
      else:
          i=0
          curr=self.head
      
          while i<pos:
              curr=curr.next
              i+=1
      return curr
  ```
  
+ 특정 위치에 원소 삽입
  ```python
  def insertAt(self, pos):
      if pos<1 or pos>self.nodeCount+1:
          return False
      
      prev=self.getAt(pos-1) #pos-1의 해당 노드를 찾고, 그뒤에 새로운 노드 삽입(inserAfter)
      return self.inserAfter(prev, newNode)
  ```
  
------------------------------------------------------------------------------------
#### 연습문제 1. 특정 위치의 다음 노드에 노드 삽입
```python
def insertBefore(self, next, newNode):
    newNode.prev=next.prev #새로운 노드의 이전은 주어진 next 노드의 이전 노드
    next.prev.next=newNode #이전 노드(prev)의 다음은 새로운 노드
    next.prev=newNode #next의 이전은 새로운 노드
    newNode.next=next #새로운 노드의 다음은 next
    self.nodeCount+=1 #노드 카운트 +1
    return True
```

#### 연습문제 2. 노드 삭제
```python
def popAfter(self, prev):
    #prev의 다음 노드 삭제하기
    cur=prev.next #삭제할 노드
    prev.next=cur.next #이전 노드와 삭제할 노드의 다음노드 연결
    cur.next.prev=prev #서로 연결
    
    self.nodeCount-=1 #노드 개수 -1
    return cur.data

def popBefore(self, next):
    #next 이전 노드 삭제하기
    cur=next.prev #삭제할 노드
    prev=cur.prev #삭제할 노드의 이전
    prev.next=next #이전노드와 다음노드 연결
    next.prev=prev #서로 연결
    
    self.nodeCount-=1 #노드 개수 -1
    return cur.data

def popAt(self, pos):
    #해당 노드가 올바른 범위내에 있지 않은 경우
    if pos<1 or pos>self.nodeCount:
        raise IndexError
        
    return self.popAfter(self.getAt(pos-1))
```

#### 연습 문제 3. 리스트 병합
```python
def concat(self, L):
    self.tail.prev.next=L.head.next #현재 tail에 L 병합
    L.head.next.prev=self.tail.prev #L의 head 대신에 현재 리스트의 맨 끝 값과 연결
    self.tail=L.tail #tail을 L의 tail로 설정
    self.nodeCount+=L.nodeCount #리스트 L의 노드 개수만큼 더해줌
```
  
