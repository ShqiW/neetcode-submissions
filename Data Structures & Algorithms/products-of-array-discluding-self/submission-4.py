class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        sub1 = [1] * len(nums)
        sub2 = [1] * len(nums)

        for i in range(1, len(nums)):
            sub1[i] = nums[i-1] * sub1[i-1]

        for i in range(len(nums)-2, -1, -1):
            sub2[i] = nums[i+1] * sub2[i+1]
        
        res = [1] * n
        for i in range(n):
            res[i] = sub1[i] * sub2[i]
        return res
        
        