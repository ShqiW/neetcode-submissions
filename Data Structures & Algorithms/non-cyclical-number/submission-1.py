class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquare(n)
        while slow != fast:
            fast = self.sumSquare(fast)
            fast = self.sumSquare(fast)
            slow = self.sumSquare(slow)
        return True if fast == 1 else False

    

    def sumSquare(self, n):
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
        return res


# class Solution:
#     def isHappy(self, n):
#         visit = set()
#         while n not in visit:
#             visit.add(n)
#             n = self.sumSquare(n)
#             if n == 1:
#                 return True
#         return False
    
#     def sumSquare(self, n):
#         res = 0
#         while n:
#             res += (n % 10) ** 2
#             n //= 10
#         return res

        