class Solution:
    def canJump(self, nums: List[int]) -> bool:
        further = 0
        n = len(nums)
        i = 0

        for i in range(n):
            if further < i:
                return False
            further = max(further, nums[i] + i)
            if further >= n-1:
                return True
        

