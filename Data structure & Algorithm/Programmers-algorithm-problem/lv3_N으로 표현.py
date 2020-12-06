def solution(N, number):
    #dynamic programming....
    
    s=[set() for x in range(8)] #1<=N<=9
    
    #미리 i번 반복한 수(N...N)에 대해 추가해줌
    for i,v in enumerate(s, start=1):
        v.add(int(str(N)*i))
        
    #N을 반복한 수에 대해
    for i in range(len(s)):
        #i번 전까지 반복한 수에 대해
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    
                    #zero division error(op2==0이면)
                    if op2!=0:
                        s[i].add(op1//op2)
                        
        #number 존재하면 break                
        if number in s[i]:
            answer=i+1
            break
   #전부 검사했을때, -1 반환         
   else:
       answer=-1
       
   return answer    
