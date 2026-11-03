class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        

        def rob_line(house):
            # prev1: stole
            # prev2: not stole
            prev1, prev2 = 0, 0
            for money in house:
                prev1, prev2 = max(money+prev2, prev1), prev1
            return prev1
        
        return max(rob_line(nums[1:]), rob_line(nums[:-1]))