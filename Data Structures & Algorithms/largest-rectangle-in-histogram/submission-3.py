class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = [] #[height, idx]
        res = 0
        for i, h in enumerate(heights):
            start = i
            while stk and stk[-1][0] > h:
                prev_h, prev_idx = stk.pop()
                res = max(res, prev_h * (i-prev_idx))
                start = prev_idx

            stk.append([h, start])
        
        while stk:
            h, idx = stk.pop()
            res = max(res, h * (len(heights)-idx))
        return res

                