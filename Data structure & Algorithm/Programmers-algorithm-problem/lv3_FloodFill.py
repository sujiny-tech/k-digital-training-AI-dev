def solution(n,m,image):
    answer=0
    
    def bfs(row, col):
        Q=[]
        dx=[-1,0, 1,0]
        dy=[0,1,0,-1]

        Q.append([row, col, image[row][col]]) #추가
        image[row][col]=0 #방문 처리

        while Q:
            row, col, color=Q.pop(0)
            
            #동서남북 처리
            for i in range(4):
                nx=row+dx[i]
                ny=col+dy[i]
                
                #해당 인덱스에 대해,
                if 0<=nx and nx<len(image) and 0<=ny and ny<len(image[0]):
                    #같은 색이면
                    if image[nx][ny]==color:
                        image[nx][ny]=0
                        Q.append([nx, ny, color])
                        
    ##
    for i in range(n):
        for j in range(m):
            if image[i][j]!=0:
                bfs(i, j) #너비에 대해 다 방문처리하고
                answer+=1 #카운트+1
    return answer

print(solution(3,2,[[1,2],[1,2],[4,5]]))
