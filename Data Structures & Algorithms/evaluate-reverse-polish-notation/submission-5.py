class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"

  
        stk = []

        for ch in tokens:
            if ch in ops:
                b = stk.pop()
                a = stk.pop()
                if ch == "+":
                    num = a + b
                elif ch == "-":
                    num = a - b
                elif ch == "*":
                    num = a * b
                else:
                    num = int(a/b)
                stk.append(num)
            else:
                stk.append(int(ch))
        return stk[-1]
