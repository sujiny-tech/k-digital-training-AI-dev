# 연결 리스트(Linked Lists)
+ 선형 배열은 인덱스에 따라 원소를 채워넣음
+ 반면 연결 리스트는 원소들을 줄줄이 엮어서 관리하는 방식
   + 노드 : 데이터, 링크(다음 노드를 가리킴)
   + 삽입과 삭제가 유연하다 ! (링크만 조절해주면 되니까)
   ```python
   class Node:
       def __init__(self, item):
           self.data=item
           self.next=None
   ```
   + 연결 리스트 : 맨 처음링크(head), 맨끝 링크(tail), 노드의 수
   ```python
   class LinkedList:
       def __init__(self):
           self.head=None
           self.tail=None
           self.nodeCount=0
   ```
+ 연결 리스트의 추상적 자료구조 구현하기 !
   + 추상적 자료구조(Abstract Data Structures)
      + 데이터 : 정수형, 실수형, 문자열, 레코드 ...
      + 연산 : 삽입, 삭제, 순회... / 정렬, 탐색...
      
   + k번째 원소  : 배열 O(1) vs 연결리스트 O(n) ->선형탐색과 유사하므로
   ```python
   def getAt(self, k):
       #0<k<nodeCount 범위 밖일 때
       if k<=0 or k>self.nodeCount:
           return None
           
       i=1 #노드 수 카운트
       cur=self.head
       
       #k가 될 때까지
       while i<k:
           cur=cur.next
           i+=1
           
       return cur #k번째 노드 반환
   ```
   + 리스트 순회 **(연습문제)**
   ```python
   def traverse(self):
       ans=[] #지나온 데이터 담을 리스트
       cur=self.head #맨 처음 링크인 head부터
       
       while cur:
           ans.append(cur.data) #해당 노드의 값 append
           cur=cur.next #다음 링크로 바꿔주기
           
       return ans
   ```
   + 원소 삽입
      + 삽입하려는 위치기 맨 앞일 때 (prev 필요x, head 조정필요)
      + 삽입하려는 위치가 맨 끝일 때 (tail 조정필요)
   ```python
   def insertAt(self, k, newNode):
       #범위 밖일 때
       if k<1 or k>self.nodeCount+1:
           return False
           
       #맨 앞에 삽입할때 : O(1)
       if k==1:
           newNode.next=self.head
           self.head=newNode
           
       #중간일 때 : O(n)
       else:
           prev=self.getAt(k-1) #k번쨰 이전인 k-1번 노드 찾기
           newNode.next=prev.next #순서 잘 따지기
           prev.next=newNode
               
       #맨 끝일 때 : O(1)
       if k==self.nodeCount+1:
           self.tail=newNode
       
       self.nodeCount+=1 #노드 카운트 1 증가
       return True
   ```
   + 원소 삭제
   ```python
   def popAt(self, k):
       if k<1 or k>self.nodeCount:
           raise IndexError
       #head
       if k==1:
           #head만 존재할 때
           if self.nodeCount==1:
               cur=self.getAt(1)
               self.head=None
               self.tail=None
               self.nodeCount=0
               
           #다른 노드들도 존재할 때
           else:
               cur=self.head #k가 1이니까
               self.head=cur.next #다음노드를 head로
               cself.nodeCount-=1 #노드 개수 1 감소
           return cur.data #해당 데이터 반환
           
       #not head
       else:
           prev=self.getAt(k-1) #k이전의 노드 (k-1)
           cur=prev.next #k번째 노드
           prev.next=cur.next #k-1노드와 k+1노드 연결
           
           #맨 끝 tail일 때
           if k==self.nodeCount:
               self.tail=prev #tail 조정
           self.nodeCount-=1 #노드 개수 1 감소
           
           return cur.data #해당 데이터 반환
   ```
   + 두개의 연결 리스트 병합
   ```python
   def concat(self, L):
       self.tail.next=L.head #L의 맨처음 노드 이어주기
       #L의 tail이 존재할 때
       if L.tail:
              self.tail=L.tail
       self.nodeCount+=L.nodeCount #L의 노드만큼 증가
   ```
   + but, 삽입과 삭제시 유연하다는 장점을 살리지 못함 > 아래와 같이 더미노드 추가해서 확장!
   
## 더미노드를 가지는 연결 리스트
+ 더미 노드(dummy node) : 데이터를 담고있지 않는 노드
```python
class LinkedList:
    def __init__(self):
        self.nodeCount=0
        self.head=Node(None) #head는 데이터가 없는 노드
        self.tail=None
        self.head.next=self.tail
        
```
+ 리스트 순회
```python
def travers(self):
    ans=[]
    cur=self.head
    
    #맨처음 데이터 없으니까 head.next부터 시작
    while cur.next:
        cur=cur.next
        ans.append(cur.dat)
    return ans
```
+ k번째 원소 찾기
```python
def getAt(self, k):
    #0<=k<=nodeCount 범위 밖일 때
    if k<0 or k>self.nodeCount:
        return None
        
    i=0
    cur=self.head
    while i<k:
        cur=cur.next
        i+=1
        
    return cur
```
+ 원소 삽입
```python    
def insertAfter(k, newNode):
    #k뒤에 newNode 삽입하기
    newNode.next=prev.next
    
    #tail 일때, tail로 지정해줘야함
    if k.next is None:
        self.tail=newNode
    k.next=newNode
    self.nodeCount+=1
    return True
    
def insertAt(self, k, newNode):
    #범위 밖일때
    if k<1 or k>self.nodeCount+1:
        return False
        
    #head뒤에 새 노드 삽일할때
    if k!=1 and k==self.nodeCount+1:
        prev=self.tail
    else:
        prev=self.getAt(k-1)
    return self.insertAfter(k, newNode)
```
+ 원소 삭제 **(연습문제)**
```python
def popAfter(self, k):
    cur=k.next
    
    #이전 노드 k가 tail일때, 삭제할 노드 x이므로 None반환
    if k.next is None:
        return None
    
    #맨끝의 노드를 삭제할때, tail 조정 필요
    if cur.next is None:
        if self.nodeCount==1:
            self.tail=None
        else:
            self.tail=k
            
    k.next=cur.next
    self.nodeCount-=1
    
    return cur.data #해당  반환
    
def popAt(self, k):
    #범위 밖일때
    if k<1 or k>self.nodeCount:
        raise IndexError
        
    return self.popAfter(self.getAt(k-1)) #k이전의 노드를 인자로 해서 k-1뒤의 k번째 노드 삭제
    
```
+ 두 개의 연결 리스트 병합
```python
def concat(self, L):
    self.tail.next=L.head.next #L의 head 뒤인 데이터가 있는 첫번째 노드와 연결해주기
    #L의 tail이 존재할 때
    if L.tail:
        self.tail=L.tail
    self.nodeCount+=L.nodeCount #L의 노드 개수만큼 증가
```
