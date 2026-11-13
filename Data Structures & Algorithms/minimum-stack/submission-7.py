class MinStack:

    def __init__(self):
        self.stk1 = [] # store value
        self.stk2 = [] # store min_value

    def push(self, val: int) -> None:
        self.stk1.append(val)
        if not self.stk2:
            self.stk2.append(val)
        else:
            min_val = self.getMin()
            if val < min_val:
                self.stk2.append(val)
            else:
                self.stk2.append(min_val)        

    def pop(self) -> None:
        self.stk1.pop()
        self.stk2.pop()

        

    def top(self) -> int:
        return self.stk1[-1]
        

    def getMin(self) -> int:
        return self.stk2[-1]
        
