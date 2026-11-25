class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        self.backtrack(nums, res, [], used)
        return res


    def backtrack(self, nums, res, path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            if not used[i]:
                path.append(nums[i])
                used[i] = True
                self.backtrack(nums, res, path, used)
                path.pop()
                used[i] = False
