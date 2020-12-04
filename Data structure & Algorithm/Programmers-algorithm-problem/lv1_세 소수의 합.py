import itertools

def solution(n):
    check=[False]+[True]*(n-1)
    primes=[]
    
    #에라토스테네스의 체
    #n의 최대 약수는 sqrt(n)...
    for i in range(2, n):
        #False 처리 안되있으면 소수
        if check[i]:
            primes.append(i)
            #소수의 배수는 합성수니까 fasle로 처리
            for j in range(2*i, n, i):
                check[j]=False
                
    #이 부분 solution 1. 안겹치게 for문 돌리기
    ans=0
    
    for i in range(len(primes)-2):
        for j in range(i+1, len(primes)-1):
            for k in range(j+1, len(primes)):
                if primes[i]+primes[j]+primes[k]:
                    ans+=1
    return ans
    
    #solution 2. itertools의 조합 이용
    #all_=list(itertools.combinations(primes, 3))
    #for x in all_:
    #    if sum(x)==n:
    #        ans+=1
    #return ans
    
