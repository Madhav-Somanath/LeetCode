class MinStack:

    def __init__(self):
        
        self.stack =[]
        self.minval = sys.maxsize


    def push(self, x: int) -> None:
        
        if x <= self.minval:
            self.stack.append(self.minval)
            self.minval = x
        self.stack.append(x)
        

    def pop(self) -> None:
        
        if self.stack and self.stack.pop()==self.minval: 
            self.minval=self.stack.pop()
        

    def top(self) -> int:
        
        return self.stack[-1]
        

    def getMin(self) -> int:
        
        return self.minval