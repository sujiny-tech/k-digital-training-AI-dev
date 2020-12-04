def solution(s):
    stack=[]
    #습관인가 while문을 써서 pop해서 뽑아쓰는데
    #안뽑아도 되는곳에선 for문 활용하자.
    for c in s:
        #쌓여있는게 없으면 append
        if not stack:
            stack.append(c)
        else:
            #이전에 쌓인거랑 같으면, 스택에서 pop
            if stack[-1]==c:
                stack.pop()
            else:
                #다르면 스택에 append
                stack.append(c)
                
    #스택에 남아있으면 짝이 안맞는거
    if len(stack)!=0:
        return 0
    return 1
