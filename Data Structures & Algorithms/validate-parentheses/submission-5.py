class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        stk = []
        for c in s:
            if c in match:
                if not stk:
                    return False
                elif stk[-1] != match[c]:
                    return False
                else:
                    stk.pop()
            if c in match.values():
                stk.append(c)
        return True if not stk else False