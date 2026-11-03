class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtrack(nums, target, res, [], 0)
        return res
    
    def backtrack(self, nums, target, res, path, idx):
        if sum(path) == target:
            res.append(path[:])
            return 
        
        if sum(path) > target:
            return
        
        for i in range(idx, len(nums)):
            path.append(nums[i])
            self.backtrack(nums, target, res, path, i)
            path.pop()