class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        need = {}
        for ch in s1:
            need[ch] = need.get(ch, 0) + 1
        
        count = {}
        valid = 0

        while r < len(s2):
            count[s2[r]] = count.get(s2[r], 0) + 1

            if s2[r] in need and count[s2[r]] == need[s2[r]]:
                valid += 1
            r += 1

            while r - l >= len(s1):
                if valid == len(need):
                    return True
                d = s2[l]
                l += 1
                if d in need and need[d] == count[d]:
                    valid -= 1
                count[d] -= 1

                

        return False