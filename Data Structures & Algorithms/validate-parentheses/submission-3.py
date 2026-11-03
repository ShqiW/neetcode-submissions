class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stk = []
        for c in s:
            if c in d and not stk:
                return False
            if c in d:
                item = stk.pop()
                if item != d[c]:
                    return False
            else:
                stk.append(c)
        return len(stk) == 0
        