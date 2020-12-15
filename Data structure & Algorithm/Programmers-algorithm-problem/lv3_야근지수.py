import heapq

def solution(n, works):
    # 야근 시작 시점(start)에서 남은 일의 작업량을 제곱하여 더해준 값
    # 야근피로도 최소화 시키기
    # 최댓값에 대해 1씩 감소
    heap = []

    # 주어진 시간 n보다 걸리는 시간(남은 일의 작업량)이 적으면 무조건 0
    if sum(works) < n:
        return 0

    # 그렇지 않은 경우, 최대 힙으로 구성
    for work in works:
        heapq.heappush(heap, -work)

    # 최대값을 pop 시켜서 +1 시켜줌
    while n > 0 and heap:
        num = (heapq.heappop(heap)) + 1
        heapq.heappush(heap, num)
        n -= 1
    
    # 야근 피로도 계산한 값 반환
    return sum([x ** 2 for x in heap])
