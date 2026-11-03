class MinStack:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []

        

    def push(self, val: int) -> None:
        self.stk1.append(val)
        val = min(val, self.stk2[-1] if self.stk2 else val)
        self.stk2.append(val)
        

    def pop(self) -> None:
        self.stk1 = self.stk1[:-1]
        self.stk2 = self.stk2[:-1]

    def top(self) -> int:
        return self.stk1[-1]
        

    def getMin(self) -> int:
        if self.stk2:
            return self.stk2[-1]
        
