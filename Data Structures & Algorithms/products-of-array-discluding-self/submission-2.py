class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2,,8, 48]
        # [48,48,24, 6]

        # [-1,-1,0,0,0]
        # [0,6,6,3,3]

        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]
        
        suffix = [0] * n 
        suffix[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        res = [0] * n
        res[0] = suffix[1]
        res[n-1] = prefix[n-2]
        for i in range(1, n-1):
            res[i] = prefix[i-1] * suffix[i+1]
        return res
        
