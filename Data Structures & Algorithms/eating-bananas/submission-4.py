from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        while l < r:
            mid = (l+r)//2
            time = self.cal_time(piles, mid)
            if time > h:
                l = mid + 1
            elif time <= h:
                r = mid
        return l


    def cal_time(self, piles, spd):

        return sum(ceil(pile / spd) for pile in piles)