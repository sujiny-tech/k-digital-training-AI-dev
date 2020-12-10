#오늘 세션에서 설명해주신 빙고에 대해 문제풀어보기 ❗❗

def solution(board, nums):
    l=len(board)
    hor=[0]*l
    ver=[0]*l
    dia=[0]*2

    map=dict()

    #board에서의 각 숫자에 대해 좌표 매핑
    for i in range(l):
        for j in range(l):
            map[board[i][j]]=(i,j)

    #지워지는 숫자에 대해 +1
    for ele in nums:
        x,y=map[ele]
        if x==y:
            dia[0]+=1
        if y==l-x-1:
            dia[1]+=1
        hor[x]+=1
        ver[y]+=1

    #수평, 수직, 대각에 대해 빙고인 부분(l) 카운트
    return hor.count(l)+ver.count(l)+dia.count(l)