def solution(n, m, image):
    answer = 0
    # 붙어있는게 몇개냐 > bfs접근법(동서남북)
    # 예전에 풀었던 얼음얼리기였던거같은데
    visited = [[1]*m]*n  # 색깔 처리한거
    def dfs(row, col, color):
        if row <= 0 or row > n or col <= 0 or col > m or image[row][col]==0:
            return

        image[row][col]=0

        visited[row][col] = 0

        dfs(row, col + 1, color)
        dfs(row, col - 1, color)
        dfs(row + 1, col, color)
        dfs(row - 1, col, color)
        
    #방문했는지
    for i in range(n):
        for j in range(m):
            if visited[i][j]!=0 :
                print(image[i][j])
                dfs(i, j, image[i][j])
                print("방문:", visited)
                answer += 1
    print(visited, image)
    return answer

print(solution(3,2,[[1,2],[1,2],[4,5]]))

##ing.....
