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
           + 전위 순회(pre-order traversal) : 노드 x 방문 -> 왼쪽 서브트리 순회 -> 오른쪽 서브트리 순회
           + 후위 순회(post-order traversal) : 왼쪽 서브트리 순회 -> 오른쪽 서브트리 순회 -> 노드 x
            
        2. 넓이 우선 순회
    
