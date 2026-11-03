class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask


        max_int = 0x7FFFFFFF  # 32位有符号数的最大正数分界线

        return a if a <= max_int else ~(a ^ mask)
        
       