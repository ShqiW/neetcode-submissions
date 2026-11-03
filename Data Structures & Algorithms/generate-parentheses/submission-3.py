class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def valid(s):
            open = 0
            for c in s:
                open += 1 if c =='(' else -1
                if open < 0:
                    return False
            return not open
        

        def dfs(s):
            if len(s) == 2 * n:
                if valid(s):
                    res.append(s)
                return 
            dfs(s+'(')
            dfs(s+')')
    
        dfs("")
        return res