# 트리 (Trees)

+ 데이터의 검색/탐색에 아주 많이 사용되는 자료구조
+ 정점(node)와 간선(edge)을 이용해서 데이터의 배치 형태를 추상화한 자료구조
-----------------------------------------------------------
트리 용어들
+ 루트 노드(root node) : 맨위의 노드, 노드의 수준(level)이 높은 노드, 맨처음의 조상
+ 리프 노드(leaf node) : 자식노드가 없는 노드 (맨끝에 있는 노드)
+ 형제 노드(sibling node) : 같은 부모아래 자식으로 놓여있는 노드들간의 관계
+ 조상(ancestor) : 부모의 부모의...부모
+ 후손(descendant) : 자식의 자식의...자식
+ 노드의 수준(level) : 노드의 층
+ 트리의 높이(heght) : 최대 수준(level)+1 (깊이 depth라고 함)
+ 부분 트리(=서브트리 Subtree) : 일부 노드로 이뤄진 트리
+ 노드의 차수(Degree) : 자식(서브트리)의 수

-----------------------------------------------------------
트리의 종류
+ 이진 트리(Binary Tree) : 빈 트리(empty tree)이거나 모든 노드의 차수가 2이하인 트리
> 재귀적으로 정의 가능하다. (루트노드+왼쪽 서브트리+오른쪽 서브트리, 이때 왼쪽/오른쪽 서브트리=이진트리)

+ 포화 이진 트리(Full Binary Tree) : 모든 레벨에서 노드들이 모두 채워져있는 이진트리
> = 높이가 k이라면, 노드의 개수가 2^k-1인 이진트리

+ 완전 이진 트리(Complete Binary Tree) : 높이 k인 완전 이진트리
   + 레벨 k-2까지는 모든 노드가 2개의 자식을 가진 포화이진트리
   + 레벨 k-1에서는 왼쪽부터 노트가 순차적으로 채워져있는 이진트리

-----------------------------------------------------------
# 이진 트리(Binary Trees)

이진 트리의 추상적 자료구조
1. 연산의 정의
    + size() : 현재 트리에 포함되어 있는 노드의 수를 구함
    + depth() : 현재 트리의 깊이(높이)를 구함
    + 순회(traversal) #중요!

2. 이진 트리의 구현
    + 노드(Node) : 해당 노드의 데이터와 left, right 자식 노드를 가짐
    ```python
    class Node:
        def __init__(self, item):
            self.data=item #해당 노드의 데이터
            self.left=None #left child node
            self.right=None #right child node
    ```
    
    + 트리(Tree) : root 노드를 가짐
    ```python
    class BinaryTree:
        def __init__(self,r):
            self.root=t
    ```
    + size() : 트리 자체가 재귀적인 성질을 지니므로, 재귀적인 방법으로 size를 구할 수 있음.
       + 전체적인 트리의 크기 = 왼쪽/오른쪽노드의 사이즈 + 1(root node), 
       + 각각의 노드의 서브 트리사이즈를 구하기 위해 노드 클래스에서 size 메서드는 다음과 같다.
        ```python
        class Node:
            def size(self):
                l=self.left.size() if self.left else 0
                r=self.right.size() if self.right else 0
                return l+r+1
        ```
        
       + 이진트리에서의 size 메서드는 두번째 코드와 같다.    
        ```python
        class BinaryTree:
            def size(self):
                if self.root:
                    return self.root.size()
                else:
                    return 0
        ```
    + depth() : 재귀적인 방법으로 가능하다
       + 전체 이진 트리의 depth = max(left node의 깊이, right node의 깊이)+1
       + 연습 문제 1에서 구현하기로...
       
    + 순회 (Traversal)
        1. 깊이 우선 순회(depth first traversal)
           + 중위 순회(in-order traversal) : 왼쪽 서브트리 순회 -> 노드 x 방문 -> 오른쪽 서브트리 순회
              + 노드 클래스에서 중위 순회(inorder) 메서드는 다음과 같다.
              ```python
              class Node:
                  def inorder(self):
                      traversal=[]
                      if self.left:
                          traversal+=self.left.inorder()
                      traversal.append(self.data)
                      if self.right:
                          traversal+=self.right.inorder()
                      retrun traversal
              ```
              + 이진 트리 클래스에서 중위 순회(inorder) 메서드는 다음과 같다.
              ```python
              class BinaryTree:
                  def inorder(self):
                      traversal=[]
                      if self.root:
                          return self.root.inorder()
                      else:
                          return []
              ```
           
           + 전위 순회(pre-order traversal) : 노드 x 방문 -> 왼쪽 서브트리 순회 -> 오른쪽 서브트리 순회
              + 연습 문제 1에서 구현하기로...
           + 후위 순회(post-order traversal) : 왼쪽 서브트리 순회 -> 오른쪽 서브트리 순회 -> 노드 x
              + 연습 문제 1에서 구현하기로...
              
        #### 연습문제 1. 이진트리의 depth() 연산 구현
        ```python
        class Node:
           ...
           def depth(self):
               l_d=self.left.depth() if self.left else 0
               r_d=self.right.depth() if self.left else 0
               retrun max(l_d, r_d)+1
           ...
       class BinaryTree:
           ...
           def depth(self):
               if self.root:
                   return self.root.depth()
               else:
                   return 0
        ```
        
        #### 연습문제 2. 전위 순회
        ```python
        class Node:
            def preorder(self):
                traversal=[]
                #노드 x 방문
                traversal.append(self.data) 
                #왼쪽 서브트리 순회
                if self.left:
                    traversal+=self.left.preorder()
                #오른쪽 서브트리 순회
                if self.right:
                    traversal+=self.right.preorder()
                return traversal
         
        class BinaryTree:
            def preorder(self):
                 traversal=[]
                 if self.root:
                     return self.root.preorder()
                 else:
                     return []
        ```
        
        #### 연습문제 3. 후위 순회
        ```python
        class Node:
            def postorder(self):
                traversal=[]
                #왼쪽 서브트리 순회
                if self.left:
                    traversal+=self.left.postorder()
                #오른쪽 서브트리 순회
                if self.right:
                    traversal+=self.right.postorder()
                #노드 x 방문
                traversal.append(self.data) 
                return traversal
         
        class BinaryTree:
            def postorder(self):
                 traversal=[]
                 if self.root:
                     return self.root.postorder()
                 else:
                     return []
        ```
        ----------------------------------------------
        2. 넓이 우선 순회(Breadth First Traversal)
           + 수준(level)이 낮은 노드를 우선으로 방문
           + 같은 수준의 노드에서는 부모노드의 방문 순서에 따라 방문, 왼쪽노드를 오른쪽노드보다 먼저 방문
           + 한 노드를 방문할 때, 나중에 방문할 노드들을 순서대로 기록해야함
             > 큐(Queue) 이용 !
             
        #### 연습문제 4. 넓이 우선 
        ##### 힌트
        1. (초기화) traversal : 빈리스트/ q:빈큐
        2. 빈 트리가 아니면, root node를 q에 추가(enequeue)
        3. q가 비어있지않은동안
           1. node<-q에서 원소 추출(dequeue)
           2. node 방문
           3. node의 왼쪽, 오른쪽 자식이 있으면 q에추가
        4. q가 빈큐면 모든 노드 방문 
        ```python
        ...
        class BinaryTree:
            def __init__(self, r):
                self.root=r
            
            def btf(self):
                #초기화
                traversal=[]
                q=ArrayQueue()
                
                #빈 트리가 아니면,
                if self.root:
                    q.enqueue(self.root)
                
                #처음에 while q : 라고했을때 런타임 에러발생! 조심!
                while q.size()!=0:
                    node=q.dequeue() #원소 추출
                    traversal.append(node.data) #node 방문
                    
                    #왼쪽 노드 있니?
                    if node.left:
                        q.enqueue(node.left)
                        
                    #오른쪽 노드는?
                    if node.right:
                        q.enqueue(node.right)
                        
                return traversal
        ```
        
-----------------------------------------------------------
# 이진 탐색 트리(Binary Search Trees)
+ 모든 노드에 대해서, 왼쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 작고, 오른쪽 서브트리에 있는 데이터는 모두 현재 노드 값보다 크다.
+ 정렬된 배열을 이용한 이진 탐색보다 데이터 원소의 추가/삭제가 용이하지만, 공간 소요가 크다.

## 이진 탐색 트리의 추상적 자료구조
+ 각 노드는 (key, value)의 쌍 -> 키를 이용해서 검색 가능, 복잡한 데이터 레코드로 확장 가능

## 연산의 정의
1. insert(key, data) : 트리에 주어진 데이터 원소를 추가 
2. remove(key) : 특정 원소를 트리로부터 삭제
3. lookup(key) : 특정 원소를 검색
4. inorder() : 키의 순서대로 데이터 원소 나열
> 이진 트리에서 설명했던 중위순회와 동일
5. min(), max() : 최소 키, 최대 키를 가지는 원소들 탐색

## 코드 구현
1. 초기화, inorder(), min/max(), lookup(key)
   + lookup()
      + 입력 인자 : 찾으려는 대상 키
      + 리턴 : 찾은 노드와 그것의 부모 노드(각각 없으면 None)
      
   ```python
   class Node:
       def _init__(self, key, data):
           self.key=key
           self.data=data
           self.left=None
           self.right=None
       
       def inorder(self):
           traversal=[]
           if self.left:
               traversal+=self.left.inorder()
           traversal.append(self)
           if self.right:
               traversal+=self.right.inorder()
           return traversal
           
       def min(self):
           if self.left:
               return self.left.min()
           #가장 왼쪽이 작은 값이니까
           else:
               return self
               
       def max(self):
           if self.right:
               return self.left.min()
           #가장 오른쪽이 큰값이니까
           else:
               return self
        
       def lookup(self, key, parent=None):
           #왼쪽에 있어야하니까
           if key<self.key:
               if self.left:
                   return self.left.lookup(key, self)
               else:
                   return None, None
           elif key>self.key:
               if self.right:
                    return self.right.lookup(key, self)
               else:
                   return None, None
                   
           #key==self.key이므로
           else:
               return self, parent
           
           
   class BinSearchTree:
       def _init__(self):
           self.root=None
       
       def inorder(self):
           if self.root:
               return self.root.inorder()
           else:
               return []
               
       def min(self):
           if self.root:
               return self.root.min()
           else:
               return None
               
       def max(self):
           if self.root:
               return self.root.max()
           else:
               return None
       
       def lookup(self, key):
           if self.root:
               return self.root.lookup(key)
           else:
               return None, None
               
   ```

2. insert()
   + 입력 인자 : 키, 데이터 원소
   + 리턴 : x
   + 연습 문제에서 구현하는 걸로...
   
#### 연습 문제 5. 이신 탐색 트리 insert()메서드 구현
```python
class BinSearchTree:
    def insert(self, key, data):
        #root가 존재하면
        if self.root:
            self.root.insert(key, data)
            
        #빈 트리라면
        else:
            self.root=Node(key, data)
class Node:
    #재귀적으로 구현
    def insert(self, key< data):
        #왼쪽에 넣을려면
        if key<self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left=Node(key, data)
                 
        #오른쪽에 넣으려면
        elif key>self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right=Node(key, data)
        
        #중복된 키 존재!
        else:
            raise KeyError('The key already exists.')
```

3. remove()
   + 키(key)를 이용해서 노드 찾기 : 해당 키 없으면 삭제x, 찾은 노드를 제거하더라도 그 노드의 부모 노드도 알고 있어야 함!
   + 입력 인자 : 키
   + 리턴 : 삭제한 경우 True, 해당 키의 노드가 없는 경우 False
      + 삭제되는 노드가 말단(leaf)인 경우
         > 그냥 그 노드 없애고, 그 노드이 부모노드의 링크 조정 필요
         ```python
         ```
      + 하나의 자식을 가지고 있는 경우
         > 삭제 되는 노드자리에 그 자식 대신에 배치해야함. 자식이 왼쪽인지 오른쪽인지/부모 노드의 링크조정 필요
      + 자식을 둘 가지고 있는 경우
         > 삭제되는 노드보다 바로 다음으로 큰 키를 가지고 노드를 찾아서, 그자리에 노드를 대신 넣어주고 해당 노드 삭제
      + node 클래스에서 자식을 카운트하는 함수
      ```python
      class Node:
          def CountChildren(self):
              count=0
              if self.left:
                  count+=1 #왼쪽 자식 카운트
              if self.right:
                  count+=1 #오른쪽 자식 카운트
              return count
      ```
   + 연습 문제에서 구현하는 걸로...

#### 연습 문제 6. 이진 탐색 트리의 remove() 구현하기
```python
class BinSearchTree:
    ...
    def remove(self, key):
        node, parent = self.lookup(key) #해당 키에 따르는 노드와 부모 노드
        if node:
            nChildren = node.countChildren() #자식노드 개수 카운트
            
            # 말단 노드(leaf)일때
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if parent.right==node:
                        parent.right=None
                    else:
                        parent.left=None
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root=None
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    next_=node.left
                else:
                    next_=node.right
                    
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    #왼쪽
                    if node==parent.left:
                        parent.left=next_
                        
                    #오른쪽
                    else:
                        parent.right=next_
                        
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root=next_
                    
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent=successor ##
                    successor=successor.left
                    
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                if successor==parent.left:
                    parent.left=successor.left
                else:
                    parent.right=successor.right

            return True

        else:
            return False
            
```

------------------------------------------------------

## 이진 탐색 트리가 별로 효율적이지 못한 경우
+ 한쪽으로 치우친 트리(증가하는 키, 감소하는 키 삽입하는 경우) -> 선형 탐색과 동등한 정도의 복잡도를 가짐

## 보다 나은 성능을 보이는 이진 탐색 트리들
+ 높이의 균형을 유지함으로써 O(logn)의 탐색 복잡도 보장
+ 삽입, 삭제 연산이 보다 복잡
+ ex) [AVL tree](https://ko.wikipedia.org/wiki/AVL_%ED%8A%B8%EB%A6%AC), [Red-balck tree](https://ko.wikipedia.org/wiki/%EB%A0%88%EB%93%9C-%EB%B8%94%EB%9E%99_%ED%8A%B8%EB%A6%AC)
