class MinStack:

    def __init__(self):
        self.stack=[]
        self.stack_minimum=[]
        
        return
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if  not  self.stack_minimum or val<=self.stack_minimum[-1] :
            self.stack_minimum.append(val)
        
        return 
        

    def pop(self) -> None:
        if self.stack:
            element=self.stack.pop()
            if element==self.stack_minimum[-1]:
                self.stack_minimum.pop()
        else:
            return 
        return element
        

    def top(self) -> int:        
        return self.stack[-1] if self.stack else None
        

    def getMin(self) -> int:
        return self.stack_minimum[-1] if self.stack_minimum else None
        
