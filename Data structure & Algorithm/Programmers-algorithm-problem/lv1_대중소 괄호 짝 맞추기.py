def solution(s):
    stack=[]
    #lv2_올바른 괄호의 확장버전?
    #dictionary 사용
    d={")":"(",
       "{":"}",
       "[":"]"}
       
    for i in range(len(s)):
        if s[i] in "({[":
            stack.append(s[i]) #열린 괄호는 스택에 쌓고
            
        #닫힌 괄호이면서, 스택에 뭔가 쌓여있을 때
        elif stack and s[i] in ")}]":
            if stack[-1]!=d[s[i]]:
                return False #스택의 맨 끝원소랑 비교
            stack.pop() #짝이면 pop
            
        #닫힌 괄호이면서, 스택없으면 짝이 없는거
        else:
            return False
            
    return len(stack)==0
            
    
    
