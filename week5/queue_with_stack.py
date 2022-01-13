class MyQueue:

    def __init__(self):
        from collections import deque
        self.stack = deque(list())
        self.junk = list()

    def push(self, x: int) -> None:
        self.stack.append(x)
            
            

    def pop(self) -> int:
        if len(self.stack) > 0:
            self.var = self.stack[0]
            self.stack.popleft()
            return self.var
        else:
            return False
        
            
        

    def peek(self) -> int:
        if len(self.stack) > 0:
            return self.stack[0]
        else:
            return False

    def empty(self) -> bool:
        if len(self.stack) > 0:
            return False
        else:
            return True
        
