class Solution:
    def isValid(self, s: str) -> bool:
        memo = {
            ')': '(',
            ']': '[',
            '}': '{'
            }
        
        stk = []
        for c in s:
            if c in memo:
                if stk:
                    item = stk.pop()
                    if item != memo[c]:
                        return False
                else:
                    return False
            else:
                stk.append(c)
        return True if not stk else False
            