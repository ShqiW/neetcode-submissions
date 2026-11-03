class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_dict = {}
        for i in nums:
            if i not in duplicate_dict:
                duplicate_dict[i] = 1
            else:
                duplicate_dict[i] += 1
            if duplicate_dict[i] > 1:
                return True
        return False

         