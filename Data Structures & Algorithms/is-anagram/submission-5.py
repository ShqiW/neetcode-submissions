class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_encode = self.encode(s)
        t_encode = self.encode(t)
        return s_encode == t_encode
    
    def encode(self, s):
        encode_list = [0] * 26
        for c in s:
            idx = ord(c) - ord("a")
            encode_list[idx] += 1
        return encode_list