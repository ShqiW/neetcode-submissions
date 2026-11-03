class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False



class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if cur.children[i] is None:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.isWord = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):

            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children:
                        if child is not None and dfs(i+1, child):
                            return True
                    return False
                else:
                    idx = ord(c) - ord('a')
                    if not cur.children[idx]:
                        return False
                    cur = cur.children[idx]
            return cur.isWord

        return dfs(0, self.root)
                
        
