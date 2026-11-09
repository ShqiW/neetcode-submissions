class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        l, r = 0, 0
        n = len(s)
        memo = defaultdict(int)

        while r < n:
            while memo[s[r]] >= 1:
                memo[s[l]] -=1 
                l += 1



            memo[s[r]] += 1
            maxCount = max(maxCount, r-l+1)
            r += 1
        return maxCount
