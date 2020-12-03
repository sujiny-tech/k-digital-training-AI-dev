import heapq

def solution(scoville, k):
    ans=0
    heapq.heapify(scoville) #힙으로 바꿔주기
    
    #최솟값이 k보다 작다면 진행
    while scoville[0]<K:
        try:
            heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)) #먼저 두개뽑아서 계산해서 넣어줌
            
        #인덱스 에러 발생하면 -1 (끝까지 k 안넘는다는 것)
        except IndexError:
            return -1
        ans+=1
        
    return ans
