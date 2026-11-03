class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in visited:
                return [visited[needed], i]
            else:
                visited[nums[i]] = i
        return []