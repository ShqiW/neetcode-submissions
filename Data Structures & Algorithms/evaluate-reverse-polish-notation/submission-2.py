class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t not in "+-*/":
                stk.append(int(t))
            else:
                b = stk.pop()
                a = stk.pop()
                if t == "+":
                    stk.append(a+b)
                elif t == "-":
                    stk.append(a-b)
                elif t == "*":
                    stk.append(a*b)
                elif t == "/":
                    stk.append(int(a/b))
        return stk[0]