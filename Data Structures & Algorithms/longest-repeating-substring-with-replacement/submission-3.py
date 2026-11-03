class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        max_f = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1
            max_f = max(max_f, count[s[r]])
            while r-l+1 - max_f > k:
                count[s[l]] -= 1
                l += 1
            res = max(max_f, r-l+1)
        return res