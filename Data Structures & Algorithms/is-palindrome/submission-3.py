class Solution:
    def isPalindrome(self, s: str) -> bool:
        sb = []
        for c in s:
            if c.isalnum():
                sb.append(c.lower())
        

        left, right = 0, len(sb) - 1
        while left < right:
            if sb[left] != sb[right]:
                return False
            left, right = left + 1, right - 1
        return True