class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        total = max(nums[:k])

        r = k-1
        
        res = [total]

        while r < len(nums)-1:
            r += 1
            l += 1
            max_num = max(nums[l:r+1])
            
            res.append(max_num)
        return res
