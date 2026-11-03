class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        seen = {}

        while r < len(s):
            while s[r] in seen and seen[s[r]] > 0:
                seen[s[l]] -= 1
                l += 1

            seen[s[r]] = seen.get(s[r], 0) + 1
            res = max(res, r-l+1)
            r += 1
        return res

        