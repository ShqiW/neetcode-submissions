class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        self.backtrack(n, 0, 0, stack, res)
        return res

    def backtrack(self, n, openN, closedN, stack, res):
        if openN == closedN == n:
            res.append("".join(stack))
            return
        if openN < n:
            stack.append("(")
            self.backtrack(n, openN + 1, closedN, stack, res)
            stack.pop()
        if closedN < openN:
            stack.append(")")
            self.backtrack(n, openN, closedN + 1, stack, res)
            stack.pop()
        
        