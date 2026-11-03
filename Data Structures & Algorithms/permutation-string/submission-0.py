class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needed = {}
        for c in s1:
            needed[c] = needed.get(c,0) + 1

        l, r = 0, 0
        window = {}
        valid = 0
        while r < len(s2):
            c = s2[r]
            r += 1
            if c in needed:
                window[c] = window.get(c, 0) + 1
                if window[c] == needed[c]:
                    valid += 1
            while r - l >= len(s1):
                if valid == len(needed):
                    return True
                d = s2[l]
                l += 1
                if d in needed:
                    if window[d] == needed[d]:
                        valid -= 1
                    window[d] -= 1
        return False