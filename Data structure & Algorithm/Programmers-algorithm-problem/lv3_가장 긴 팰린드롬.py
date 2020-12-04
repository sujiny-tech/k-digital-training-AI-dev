def solution(s):
    ans=0
    
    #solution 1. 비교(직관적으로)
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_str=s[i:j+1] #모든 경우에 대해 길이를 구한다
            if sub_str==sub_str[::-1]:
                ans=max(ans, len(sub_str))
                
    return ans
    #효율적인 알고리즘 > longest palindrom subsequence
    #이전에 풀었을때도 어려웠던 기억이 나는데 아직도 어렵ㄷ...😂
    #다시 문제 풀어봐야 함!!!!!!
