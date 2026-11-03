class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = [0] * 26
        max_count = 0
        res = 0

        # expand window
        while r < len(s):
            idx = ord(s[r]) - ord('A')
            count[idx] += 1
            max_count = max(max_count, count[idx])
            r += 1


            # narrow window
            # right - left - max_count > k
            while r - l - max_count > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
            

        # update res
        res = max(res, r-l)
        return res

        