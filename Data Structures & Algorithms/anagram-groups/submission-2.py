class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordToCount = defaultdict(list)
        for string in strs:
            label = tuple(sorted(string))
            wordToCount[label].append(string)
        return list(wordToCount.values())