def solution(dirs):
    answer = 0
    index = {"U": 0, "D": 1, "R": 2, "L": 3}
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited = set() #set으로 설정/ 이미 지나간 길인지 아닌지만 체크
    x,y=0,0 #시작점 초기화

    for d in dirs:
        i=index[d] #해당 인덱스
        nx, ny=x+dx[i], y+dy[i]

        #범위밖(예외처리)
        if nx<-5 or nx>5 or ny<-5 or ny>5:
            continue

        #아직 방문 안했으면 추가
        if (x,y,nx,ny) not in visited:
            visited.add((x,y,nx,ny))
            visited.add((nx,ny,x,y)) #같은간선이므로
            answer+=1

        x,y=nx,ny #현재지점 업데이트

    return answer
