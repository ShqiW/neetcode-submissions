class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in dic:
                return [dic[needed], i]
            dic[nums[i]] = i
        