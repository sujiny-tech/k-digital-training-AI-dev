def solution(s):
    stack=[]
    #왜 항상 나는 무조건 while문 돌려서 pop시키려고 하는걸까...😂
    for c in s:
        #쌓여져있고, 이전값보다 큰게 나타나면 pop
        while stack and stack[-1]<c:
            stack.pop()
        stack.append(c)
        
    return ''.join(stack)
