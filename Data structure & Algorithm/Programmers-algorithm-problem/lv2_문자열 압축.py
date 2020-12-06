def split_function(string, i):
    arr=[]
    start=0
    
    #i개 단위로 자르기
    while start<len(string):
        arr.append(string[start:start+i])
        if start+i>len(string):
            arr.append(string[start+i:])
            break
        else:
            start+=i
            
    ans=""
    diff_index=1 #뒤에꺼랑 비교할거니까
    start=0 #맨처음부터 시작
    cnt=1 #기본적으로 1개씩있으니까
    
    while start<len(arr) and diff_index<len(arr):
        #같을때 카운트+1
        if arr[start]==arr[diff_index]:
            cnt+=1
            if diff_index+1<len(arr):
                diff_index+=1
            else:
                #index넘으면 문자열개수+문자열로 압축
                ans+=str(cnt)+arr[start]
                diff_index+=1
        else:
            #다를때마다 압축시켜주기
            #이전에 같았다가 달라진거일수도있고
            if cnt>1:
                ans+=str(cnt)+arr[start]
                cnt=1
            else:
                #처음부터 다를수도있고
                ans+=arr[start]
                cnt=1
            #다시 세팅
            start=diff_index
            diff_index+=1
            #끝에 다다르면
            if diff_index==len(arr):
                ans+=arr[diff_index-1]
                
    return len(ans)

def solution(s):
    cnt = len(s) 
    
    #1개,2개,..mid개 단위로 잘라서 압축한 결과 중 min_val?
    for i in range(1, (len(s)//2)+1):
        cnt=min(cnt, split_function(s, i))
    
    return cnt
