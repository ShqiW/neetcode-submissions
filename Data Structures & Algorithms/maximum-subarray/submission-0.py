class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        max_sum = prefix[0]
        min_prefix = 0

        for i in range(len(nums)):
            max_sum = max(max_sum, prefix[i]-min_prefix)
            min_prefix = min(min_prefix, prefix[i])
        return max_sum