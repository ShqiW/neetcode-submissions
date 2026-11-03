class MinStack:

    def __init__(self):
        self.stk1 = []
        self.stk2 = [] # min_stk

    def push(self, val: int) -> None:
        if self.stk1:
            prev_min = self.stk2[-1]
            if val < prev_min:
                self.stk2.append(val)
            else:
                self.stk2.append(prev_min)
        else:
            
            self.stk2.append(val)    
        self.stk1.append(val)    

    def pop(self) -> None:
        if self.stk1:
            self.stk1.pop()
            self.stk2.pop()
        

    def top(self) -> int:
        if self.stk1:
            return self.stk1[-1]

    def getMin(self) -> int:
        if self.stk2:
            return self.stk2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()