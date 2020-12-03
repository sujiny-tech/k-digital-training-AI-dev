def solution(v):
    x = []
    y = []
    #문제 접근 : 주어진 정점에 대해 하나씩 빠져있는 x, y좌표 구하기
    for p in v:
        #x좌표가 없으면 넣어주고
        if p[0] not in x:
            x.append(p[0])
        #있으면 제거(마지막에 남는게 답)
        else:
            x.remove(p[0])
        #y좌표가 없으면 넣어주고
        if p[1] not in y:
            y.append(p[1])
        #있으면 제거(마지막에 남는게 답)
        else:
            y.remove(p[1])
    return x + y