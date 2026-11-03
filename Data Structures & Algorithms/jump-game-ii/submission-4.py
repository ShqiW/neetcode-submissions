class Solution:
    def jump(self, nums: List[int]) -> int:
        farest = 0
        cur_end = 0
        step = 0

        for i in range(len(nums)-1):
            farest = max(farest, cur_end+nums[i])
            if i == cur_end:
                step += 1
                cur_end = farest
        return step
