class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dic = defaultdict(list)
        for word in strs:
            dic_key = self.encode(word)
            res_dic[dic_key].append(word)
        res = []
        for r in res_dic.values():
            res.append(r)
        return res

    
    def encode(self, s):
        encode_list = [0] * 26
        for ch in s:
            idx = ord(ch) - ord("a")
            encode_list[idx] += 1
        return tuple(encode_list)