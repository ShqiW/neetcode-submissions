class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.backtrack(nums, 0, target)
        return self.res
    
    def backtrack(self, nums, start, target):
        if sum(self.path) == target:
            self.res.append(self.path[:])
        if sum(self.path) > target:
            return

        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.backtrack(nums, i, target)
            self.path.pop()

