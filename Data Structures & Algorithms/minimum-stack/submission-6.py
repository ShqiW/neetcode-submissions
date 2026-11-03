class MinStack:

    def __init__(self):
        self.stk1 = []
        self.stk2 = [] # min_stk
        

    def push(self, val: int) -> None:
        self.stk1.append(val)
        if not self.stk2:
            self.stk2.append(val)
        else:
            self.stk2.append(min(val, self.getMin()))

        

    def pop(self) -> None:
        self.stk1.pop()
        self.stk2.pop()
        

    def top(self) -> int:
        if self.stk1:
            return self.stk1[-1]
        

    def getMin(self) -> int:
        if self.stk2:
            return self.stk2[-1]
        
