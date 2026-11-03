class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        self.backtrack(candidates, 0, res, path, target)
        return res
    
    def backtrack(self, candidates, idx, res, path, target):
        total = sum(path)
        if total == target:
            res.append(path[:])
        elif total > target:
            return
        
        for i in range(idx, len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            self.backtrack(candidates, i+1, res, path, target)
            path.pop()