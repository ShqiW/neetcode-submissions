class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)-1
        while left <= right:
            mid = (left + right) //2
            count = sum(num <= mid for num in nums)
            if count > mid:
                result = mid
                right = mid-1
            else:
                left = mid + 1
        return result