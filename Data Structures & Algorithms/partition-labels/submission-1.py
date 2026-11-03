class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, v in enumerate(s):
            last[v] = i
        
        start = 0
        end = 0
        res = []
        for i, v in enumerate(s):
            end = max(end, last[v])
            if i == end:
                res.append((end - start + 1))
                start = end+1
        return res
        