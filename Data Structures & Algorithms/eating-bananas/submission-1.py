class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, sum(piles)
        while left <= right:
            mid = left + (right-left) // 2
            if self.f(piles, mid) < h:
                right = mid - 1
            elif self.f(piles, mid) > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def f(self, piles, k):
        hours = 0
        for p in piles:
            hours += p // k
            if p % k > 0:
                hours += 1
        return hours
        