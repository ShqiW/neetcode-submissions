class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ")": "(",
            "]":"[",
            "}":"{"
        }

        stk = []

        for c in s:
            if c in match:
                if not stk or stk[-1] != match[c]:
                    return False
                stk.pop()
            else:
                stk.append(c)
        return not stk