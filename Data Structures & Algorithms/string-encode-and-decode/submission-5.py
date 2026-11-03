class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for string in strs:
            length = len(string)
            res.append(str(length))
            res.append("#")
            res.append(string)
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
