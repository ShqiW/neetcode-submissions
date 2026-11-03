class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = [] # [temp, idx]
        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][0] :
                stkT, stkI = stk.pop()
                res[stkI] = i - stkI
            stk.append([t, i])
        return res
        