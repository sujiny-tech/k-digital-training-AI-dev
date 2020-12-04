class MyStack(object):
    def __init__(self):
        self.lst=list()
        
    def push(self, x):
        self.lst.append(x)
    
    def pop(self):
        return self.lst.pop()
    
    def size(self):
        return len(self.lst)

class MyQueue(object):
    def __init__(self, max_size):
        self.stack1=MyStack()
        self.stack2=MyStack()
        self.max_size=max_size
        
    def qsize(self):
        return self.stack1.size()
    
    def push(self, item):
        if self.qsize()==self.max_size:
            return False
        self.stack1.push(item)
        return True
    
    def pop(self):
        try:
            if self.stack1.size()==0:
                raise Exception("Empty Exception")
                
            #꺼낼때 stack2를 이용해서 꺼내라
            while self.stack1.size():
                self.stack2.push(self.stack1.pop()) #stack1 값들을 stack2에 거꾸로 담고
            val=self.stack2.pop() #맨 밑에 있던 첫번째 값 빼내고
            
            while self.stack2.size():
                self.stack1.push(self.stack2.pop()) #나머지 다시 stack1에 담아줌
            return val
            
        except Exception:
            return False
            
n, max_size=map(int, input().strip().split(' '))
queue=MyQueue(max_size)

for c in range(n):
    c=input().split(' ')
    if c[0]=="SIZE":
        print(queue.qsize())
    elif c[0]=="PUSH":
        print(queue.push(c[1]))
    else:
        print(queue.pop())
