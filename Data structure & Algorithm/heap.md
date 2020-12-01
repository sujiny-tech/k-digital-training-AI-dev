# 힙(Heap)

+ 이진 트리의 한 종류로써 이진 힙(Binary heap)이라고도 함.
   + 조건 1. 루트(root) 노드가 언제나 최댓값 or 최솟값을 가짐 -> 최대힙(max heap), 최소 힙(min heap)
   + 조건 2. 완전 이진 트리여야함
+ 재귀적으로 정의됨 (어느 노드를 루트로 하는 서브트리도 모두 최대/최소 힙)

## 이진 탐색 트리와의 비교
1. 원소들은 완전히 크기 순으로 정렬되어있는가?
> 이진 탐색 트리의 경우에 O, 힙은 X
2. 특정 키 값을 가지는 원소를 빠르게 검색할 수 있는가?
> 이진 탐색의 경우는 key 값을 가지고 왼쪽/오른쪽을 찾아가기때문에 O, 힙은 어떤 특정 key값을 탐색하는데 좋은방법은 존재 x
3. 부가의 제약 조건은 어떤 것인가?
> 힙은 완전 이진 트리여야한다는 제약조건 존재

## 최대 힙(Max Heap)의 추상적 자료구조
1. 연산의 정의
   + __init__() : 빈 최대 힙 생성
   + insert(item) : 새로운 원소 삽입
   + remove() : 최대 원소(root node)를 반환과 동시에 노드 삭제

2. 데이터 표현의 설계
   + 배열을 이용한 이진 트리의 표현(노트번호 m을 기준)
      + 왼쪽 자식의 번호 : 2m
      + 오른쪽 자식의 번호 : 2m+1
      + 부모 노드의 번호 : m//2
      + 완전 이진 트리이므로, 노드의 추가/삭제는 마지막 노드에서만 발생
      
 ### 코드 구현
 1. __init__()
 ```python
 class MaxHeap:
     def __init__(self):
         self.data=[None] # 빈 힙 생성 (0번 인덱스는 None)
 ```
 
 2. insert(item)
    + 트리의 가장 마지막 자리에 새로운 원소를 임시로 저장
    + 부모 노드와 키 값을 비교하여 위로, 위로 이동
    + 원소의 개수가 n인 최대 힙에 새로운 원소 삽입
    > 부모 노드와의 대소 비교 최대 횟수 : log2n -> 최악의 경우 O(logn)
    ##### 힌트 : Python에서 두 변수 값 바꾸기
       ```python
       a,b=b,a
       ```
    ### 연습 문제 1. 최대힙의 삽입 연산 구현
    ```python
    class MaxHeap:
        def insert(self, item):
            #비어있다면,
            if self.data[-1]==None:
                self.data.append(item)
            #원소가 있다면,
            else:
                self.data.append(item)
                cur=len(self.data)-1
            
                #1이 되면 종료.
                while cur>1:
                    cur_parent=cur//2
                
                    #순서가 올바른가
                    if self.data[cur_parent]<self.data[cur]:
                        self.data[cur_parent], self.data[cur]=self.data[cur], self.data[cur_parent]
                        cur=cur_parent
                    #작거나 같으면, 올바르게 삽입
                    else:
                        break
            
    ```
 3. remove()
    + 루트 노드(=원소들 중 최댓값)의 제거
    + 트리 마지막 자리 노드를 임시로 루트 노드의 자리에 배치
    + 자식 노드들과의 값 비교와 아래로, 아래로 이동
    > insert()와 방향이 반대, 자식이 둘일때, 더 큰 키값을 기준으로 해야함
    + 원소 개수가 n인 최대 힙에서 최대 원소 삭제
    > 자식 노드들과 대소 비교 최대 횟수 : 2log2n -> 복잡도 O(logn)
    
    ### 연습 문제 2. 최대힙의 삭제 연산 구현
    ```python
    class MaxHeap:
        def maxHeapify(self, i):
            #i 노드를 기준으로 시작
            left=2*i
            right=2*i+1
            smallest=i
            
            #자신 i, 왼쪽 left, right 중 최대 찾기
            #해당 인덱스를 smallest에 담음
            if left<len(self.data) and self.data[left]>self.data[smallest]:
                smallest=left
            if right<len(self.data) and self.data[right]>self.data[smallest]:
                smallest=right
                
            #현재 노드 i보다 큰 키값을 가지는 경우
            if smallest!=i:
                #현재, 최대값 노드 바꾸기
                self.data[i], self.data[smallest]=self.data[smallest], self.data[i]
                #재귀적으로 maxHeapify 호출
                self.maxHeapify(smallest)
                
        def insert(self, item):
            #값이 존재하는 경우
            if len(self.data)>1:
                #self.data[1] : 루트
                #self.data[-1] : 맽 끝 데이터
                self.data[1], self.data[-1]=self.data[-1], self.data[1]
                data=self.data.pop(-1)
                self.maxHeapify(1) #루트노드부터 재귀적으로
            else:
                data=None
            return data
    ```

## 최대/최소 힙의 응용
+ 우선 순위 큐(priority queue)
   + enqueue 할 때, "느슨한 정렬"을 이루고 있도록 함 : O(logn)
   + dequeue 할 때, 최댓값을 순서대로 추출 : O(logn)
   + 양방향 연결 리스트보다 시간적으로 효율적임
+ 힙 정렬(heap sort)
   + 정렬되지 않은 원소들을 아무 순서로나 최대 힙에 삽입 : O(logn)
   + 삽입후, 힙이 텅텅 빌때까지 하나씩 삭제 : O(logn)
   + 원소들이 삭제된 순서가 원소들의 정렬순서
   + 정렬 알고리즘의 복잡도 : O(nlogn)

#### 힙 정렬 코드 구현
```python
def heapsort(unsorted):
    H=MaxHeap()
    for item in unsorted:
        H.insert(item)
    sorted=[]
    d=H.remove()
    while d:
        sorted.append(d)
        d=H.remove()
    return sorted
```
 
