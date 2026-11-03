# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k

#         def quickSelect(l, r):
#             pivot, p = nums[r], l
#             for i in range(l, r):
#                 if nums[i] <= pivot:
#                     nums[i], nums[p] = nums[p], nums[i]
#                     p += 1
#             nums[p], nums[r] = nums[r], nums[p]

#             if p > k:
#                 return quickSelect(l, p-1)
#             elif p < k:
#                 return quickSelect(p+1, r)
#             else:
#                 return nums[p]
#         return quickSelect(0, len(nums)-1)
import random

class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            rand_idx = random.randint(l, r)
            nums[rand_idx], nums[r] = nums[r], nums[rand_idx]  # 随机pivot换到末尾

            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) - 1)