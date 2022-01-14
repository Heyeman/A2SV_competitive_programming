class MinStack:

    def __init__(self):
        self.stack  = []
        self.min = float('inf')
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()
        else:
            return False

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return False
        
        

    def getMin(self) -> int:
        self.min = float('inf')
        if len(self.stack) >0:
            for i in self.stack:
                if i < self.min:
                    self.min = i
            return self.min
                
        else:
            return False
                
            
            
     
