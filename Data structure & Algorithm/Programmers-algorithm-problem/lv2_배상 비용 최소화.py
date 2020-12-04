import heapq

def solution(n, works):
    #solution 1. heap
    heap=[]
    
    #max heap
    for w in works:
    heapq.heappush(heap, -w)
    
    while n:
        num=heapq.heappop(heap)
        if num>0:
            heapq.heappush(heap, num-1)
        elif num==0:
            return 0
        else:
            heapq.heappush(heap, num+1)
        n-=1
    return sum([x**2 for x in heap])
    
    '''
    #solution 2. array sorting
    #but, 계속 정렬해야하므로 비효율적
    while n:
        works=sorted(works, reverse=True)
        if works[0]==0:
            return 0
        works[0]-=1
        n-=1
    return sum([x**2 for x in works])
    '''
