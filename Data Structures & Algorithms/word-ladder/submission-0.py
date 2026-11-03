class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        q = deque([beginWord])
        visited = set([beginWord])
        step = 1
        while q:
            sz = len(q)
            for i in range(sz):
                curWord = q.popleft()
                if curWord == endWord:
                    return step
                chars = list(curWord)
                for j in range(len(curWord)):
                    originChar = chars[j]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == originChar:
                            continue
                        chars[j] = c
                        newWord = ''.join(chars)
                        if newWord in wordSet and newWord not in visited:
                            if newWord == endWord:
                                return step + 1
                            q.append(newWord)
                            visited.add(newWord)
                    chars[j] = originChar
            step += 1
        return 0