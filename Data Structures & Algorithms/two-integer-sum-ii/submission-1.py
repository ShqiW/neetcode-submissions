class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            num = numbers[i]
            needed = target - num
            if needed in seen:
                idx = seen[needed]
                return [idx+1, i+1]
            seen[num] = i
        return []
        