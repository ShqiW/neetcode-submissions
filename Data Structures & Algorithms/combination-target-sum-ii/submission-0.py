class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.path_sum = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return self.res
        candidates.sort()
        self.backtrack(candidates, target, 0)
        return self.res
    
    def backtrack(self, candidates, target, start):
        if self.path_sum == target:
            self.res.append(self.path[:])
        if self.path_sum > target:
            return 
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            self.path.append(candidates[i])
            self.path_sum += candidates[i]
            self.backtrack(candidates, target, i+1)
            self.path.pop()
            self.path_sum -= candidates[i]
        
        