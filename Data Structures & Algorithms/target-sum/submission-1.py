class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        target_sum = (total+target)//2

        if abs(target) > total:
            return 0
        if (total+target) % 2 == 1:
            return 0
        
        dp = [0]*(target_sum+1)
        dp[0] = 1

        for num in nums:
            for j in range(target_sum, num-1, -1):
                dp[j] += dp[j-num]
        return dp[-1]