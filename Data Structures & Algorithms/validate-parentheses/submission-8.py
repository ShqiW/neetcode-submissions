class Solution:
    def isValid(self, s: str) -> bool:
        match = {
            "]": "[",
            ")": "(",
            "}": "{"
        }
        stack = []
        for c in s:

            if stack and c in match:
                last = stack.pop()
                if last != match[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0