import collections
import math

n=5
road=[[1,2,1], [2,3,3], [5,2,2], [1,4,2], [5,3,1], [5,4,2]]
k=3

def solution(n, road, k):
    graph = [[0] * (n + 1) for x in range(n + 1)]  # 그래프
    dist = [math.inf for x in range(n + 1)]  # 마을간의 거리

    def bfs(start):
        queue = collections.deque([start]) #시작점
        dist[start]=0 #거리 초기화

        while queue:
            p = queue.popleft()
            for x in range(1, len(graph)):
                # 연결된 마을인 경우
                if graph[p][x] != 0:
                    #이전에 다녀온 값보다 작고, k보다 작으면 바꿔주기
                    if dist[x]>dist[p]+graph[p][x] and dist[p]+graph[p][x]<=k:
                        dist[x]=dist[p]+graph[p][x]
                        queue.append(x)

        #k보다 작은 값의 개수만 반환
        return len([i for i in dist if i<=k])

    # 그래프 세팅
    for start, end, w in road:
        if graph[start][end] == 0 and graph[end][start] == 0:
            graph[start][end], graph[end][start] = w, w
        else:
            #적은 시간내에 배달이 가능한게 있다면, 최솟값으로 세팅
            if graph[start][end] > w:
                graph[start][end], graph[end][start] = w, w

    return bfs(1)

print(solution(n, road, k))