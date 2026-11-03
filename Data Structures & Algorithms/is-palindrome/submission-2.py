class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for c in s:
            if c.isalnum():
                s_list.append(c.lower())
        return self.isValid(s_list)
    
    def isValid(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
