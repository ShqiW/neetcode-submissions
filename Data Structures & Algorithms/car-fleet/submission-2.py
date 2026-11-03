class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [3, 3] t-1 < t res += 1
        pairs = sorted(zip(position, speed), reverse=True)
        n = len(position)
        stk = []
        res = 0
        for pos, spd in pairs:          # ← 用 pairs 而不是 position/speed[i]
            time = (target - pos) / spd
            if not stk or stk[-1] < time:  # ← 加上 not stk 处理第一辆车
                res += 1
                stk.append(time)
        return res