class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        return self.backtrack(nums, 0, [], res)

    def backtrack(self, nums, i, path, res):

        res.append(path[:])
        
        while i < len(nums):
            path.append(nums[i])
            self.backtrack(nums, i+1, path, res)
            path.pop()
            i += 1
        return res