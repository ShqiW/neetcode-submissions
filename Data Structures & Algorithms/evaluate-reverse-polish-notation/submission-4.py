class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for t in tokens:
            if t in "+-*/":
                a = int(stk.pop())
                b = int(stk.pop())
                if t == "+":
                    stk.append(a+b)
                elif t == "-":
                    stk.append(b-a)
                elif t == "*":
                    stk.append(a*b)
                else:
                    stk.append(int(float(b/a)))
            else:
                stk.append(int(t))
        return stk[0]
        