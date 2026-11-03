class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.decode(s) == self.decode(t)
    
    def decode(self, string):
        decode_list = [0] * 26
        for c in string:
            idx = ord(c) - ord('a')
            decode_list[idx] += 1
        return ''.join(str(num) for num in decode_list)