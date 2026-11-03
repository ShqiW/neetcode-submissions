class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_prod, min_prod, result = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]

            if curr < 0:
                max_prod, min_prod, = min_prod, max_prod
            
            max_prod = max(curr, max_prod*curr)
            min_prod = min(curr, min_prod*curr)

            result = max(result, max_prod)
        return result

