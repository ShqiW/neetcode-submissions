class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2 

        dp = [0] * (target+1)

        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = max(dp[i], dp[i-num]+num)
        return dp[-1] == target
        