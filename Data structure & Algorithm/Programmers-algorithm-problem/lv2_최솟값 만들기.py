def solution(A,B):
    ans=0
    A=sorted(A) #오름차순
    B=sorted(B, reverse=True) #내림차순

    #최소가 되려면, 하나는 큰 값, 하나는 작은 값
    while A and B:
        a=A.pop() #작은 값
        b=B.pop() #큰 값
        ans+=(a*b)

    return ans