class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) //2
            if self.f(piles, mid) > h:
                left = mid + 1
            elif self.f(piles, mid) < h:
                right = mid - 1
            else:
                right = mid - 1
        return left
    


    def f(self,piles, x):
        hours = 0
        for p in piles:
            hours += p //x
            if p % x > 0:
                hours += 1
        return hours