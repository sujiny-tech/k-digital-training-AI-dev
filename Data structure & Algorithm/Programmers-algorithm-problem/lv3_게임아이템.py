import heapq
from collections import deque

def solution(healths, items):
    ans=[]
    items=sorted([(it[1], it[0], i+1) for i, it in enumerate(items)])
    items=deque(items) #(체력, 공격력, 번호) 체력 큰순으로 정렬
    
    healths.sort() #체력이 낮은 캐릭터부터
    heap=[]
    
    for health in healths:
        while items and health-items[0][0]>=100:
            item=items.popleft()
            heapq.heappush(heap, (-item[1], item[2])) #체력 깎여도 100 유지 되는 아이템 -> 체력 많이 올려주는 거 골라야되니까 최대힙으로
            
        #체력유지되니까 최대한 공격력 올려주는 아이템 
        if heap:
            ans.append(heapq.heappop(mid)[1])
            
    return sorted(ans)
