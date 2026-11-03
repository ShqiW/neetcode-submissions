class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        height = [0] + heights+[0]
        stk = []
        max_area = 0

        for i, h in enumerate(height):
            while stk and stk[-1][0] > h:
                prev = stk.pop()
                width = i - stk[-1][1] - 1
                max_area = max(max_area, prev[0] * width)

            stk.append([h, i])
        return max_area