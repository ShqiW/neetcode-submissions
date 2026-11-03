class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] += 1
        for j in t:
            if j not in s_dict:
                return False
            s_dict[j] -= 1
            if s_dict[j] <0:
                return False
        for count in s_dict.values():
            if count != 0:
                return False
        return True
        
        
        