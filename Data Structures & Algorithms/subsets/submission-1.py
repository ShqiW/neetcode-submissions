class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, start):
        self.res.append(self.path[:])
        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.backtrack(nums, i+1)
            self.path.pop()
        