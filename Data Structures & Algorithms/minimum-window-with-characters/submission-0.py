class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            need[c] += 1

        left, right, valid = 0,0,0
        start = 0
        length = float('inf')

        while right < len(s):
            c = s[right]
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            right += 1

            while valid == len(need):
                if right - left < length:
                    length = right - left
                    start = left
                    
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if length == float('inf') else s[start: start+length]