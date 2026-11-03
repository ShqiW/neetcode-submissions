class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for num in nums:
            if num-1 in seen:
                continue
            cur_num = num
            cur_len = 1
            
            while cur_num + 1 in seen:
                cur_len += 1
                cur_num += 1
            res = max(res, cur_len)
        return res
        