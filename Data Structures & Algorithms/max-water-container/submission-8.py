class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1
        res = 0
        while l < r:
            l_h, r_h = heights[l], heights[r]
            res = max(res, (r-l)*min(l_h, r_h))
            if l_h <= r_h:
                l += 1
            else:
                r -= 1
        return res