import math

def solution(progresses, speeds):
    ans=[] #동일한 날짜에 몇개씩 배포되나?
    cnt=[] #각 작업에 대해 몇일 걸리는지 담아놓을 배열

    for pro, sp in zip(progresses, speeds):
        diff=math.ceil((100-pro)/sp) #남은 진도에 대해 몇일 걸리나
        #이전 작업만큼 걸리거나 빠르게 처리가능하더라도, 이전 작업만큼 걸림
        if cnt!=[] and cnt[-1]>=diff:
            cnt.append(cnt[-1])
            ans[-1]+=1 #동일하므로 카운트 1

        #이전 작업보다 더 걸릴 경우
        else:
            cnt.append(diff)
            ans.append(1) #현재 똑같은 날에 배포되는게 없으므로 1 추가
    return ans