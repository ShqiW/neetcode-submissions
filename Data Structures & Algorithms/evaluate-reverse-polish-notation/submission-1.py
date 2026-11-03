class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        res = 0

        for t in tokens:
            if t in "+-*/":
                a = stk.pop()
                b = stk.pop()
                if t == "+":
                    stk.append(a + b)
                elif t == "-":
                    stk.append(b - a)
                elif t == "*":
                    stk.append(a * b)
                elif t == "/":
                    stk.append(int(b/a))
            else:
                stk.append(int(t))
        return stk.pop()
        