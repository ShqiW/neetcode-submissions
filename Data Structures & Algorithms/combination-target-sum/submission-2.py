class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        self.backtrack(nums, target, res, subset, 0)
        return res

    def backtrack(self, nums, target, res, subset, i):
        if sum(subset) == target:
            res.append(subset[:])
            return

        if sum(subset) > target or i >= len(nums):
            return

        # 选 nums[i]：还停在 i，因为可以重复选
        subset.append(nums[i])
        self.backtrack(nums, target, res, subset, i)
        subset.pop()

        # 不选 nums[i]：跳到 i+1，以后不再考虑它
        self.backtrack(nums, target, res, subset, i + 1)