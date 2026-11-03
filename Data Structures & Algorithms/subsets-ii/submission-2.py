class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        path = []


        def backtrack(path, start_idx):
            res.append(path[:])

            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                backtrack(path, i+1)
                path.pop()
        backtrack(path, 0)
        return res