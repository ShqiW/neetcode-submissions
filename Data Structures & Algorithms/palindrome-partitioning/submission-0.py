class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, path = [], []
        

        def backtrack(i):
            if i >= len(s):
                res.append(path[:])
            for j in range(i, len(s)):
                if self.isPalidrom(s, i, j):
                    path.append(s[i:j+1])
                    backtrack(j+1)
                    path.pop()

        
        backtrack(0)
        return res
    
    def isPalidrom(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True