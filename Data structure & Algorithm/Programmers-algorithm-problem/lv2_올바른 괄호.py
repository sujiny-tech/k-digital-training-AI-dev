def solution(s):
    stack=[]
    
    #맨처음엔 while문으로 뽑아서 비교했는데 비효율적임,
    #그냥 안뽑고 for문으로 처리하는 것이 효율적임.
    for i in range(len(s)):
        if s[i]=="(":
            stack.append(s[i]) #(일때 stack에 쌓아주고
        else:
            if not stack:
                return False #)일때, stack없으면 짝이 안맞으니까 Flase
            stack.pop() #stack있으면 pop
            
    #stack에 쌓여있는게 없으면 짝이 맞는거, 쌓여있으면 짝 안맞음
    return len(stack)==0
