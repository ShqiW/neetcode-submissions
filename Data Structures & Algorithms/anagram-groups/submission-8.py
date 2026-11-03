class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)

        for string in strs:
            k = self.encode(string)
            dic[k].append(string)
        
        res = []
        for value in dic.values():
            res.append(value)
        return res

    
    def encode(self, string:str):
        idx = [0] * 26
        for c in string:
            i = ord(c) - ord("a")
            idx[i] += 1
        return "#".join(map(str,idx))
        