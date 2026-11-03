class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while  n not in seen:
            seen.add(n)
            n = self.getTotal(n)
        return n == 1
    

    def getTotal(self, num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit ** 2
            num //= 10
        return total