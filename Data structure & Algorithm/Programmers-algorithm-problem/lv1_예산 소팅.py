def solution(d, budget):
    ans=0 #지원받을 수 있는 부서 개수
    sort_d=sorted(d) #예산이 담긴 배열 정렬
    #작은 값부터 최대한 더해가면 최대한 많이 지원해주니까
    
    while sort_d:
        num=sort_d.pop(0) #일단 꺼내서 예산에서 삭감해보고
        #마이너스 되면 break
        if budget-num<0:
            break
        #아직 예산이 남아있으면
        else:
            budget-=num #예산 업데이트
            ans+=1 #지원받을 수 있는 부서 1 증가
    return ans