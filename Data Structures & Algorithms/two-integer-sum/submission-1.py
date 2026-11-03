# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i = 0
#         j = len(nums)-1
#         while i < j:
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#             elif nums[i] + nums[j] < target:
#                 i += 1
#             else:
#                 j -= 1
# only works for sorted array

class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i


        