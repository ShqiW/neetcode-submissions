class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            
            for i in range(len(nums)):
                if not used[i]:
                    
                    path.append(nums[i])
                    used[i] = True
                    backtrack(path)
                    path.pop()
                    used[i] = False
                    
        backtrack([])
        return res