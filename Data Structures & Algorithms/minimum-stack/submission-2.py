class MinStack:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []
        

    def push(self, val: int) -> None:
        self.stk1.append(val)
        
        if not self.stk2:
            self.stk2.append(val)
        else:
            cur_min = self.stk2[-1]
            if val < cur_min:      
                self.stk2.append(val)
            else:
                self.stk2.append(cur_min)
        
        

    def pop(self) -> None:
        if self.stk1:
            self.stk1.pop()
            self.stk2.pop()
        

    def top(self) -> int:
        if self.stk1:
            return self.stk1[-1]
        return None
        

    def getMin(self) -> int:
        if self.stk2:
            return self.stk2[-1]
        return None
        
