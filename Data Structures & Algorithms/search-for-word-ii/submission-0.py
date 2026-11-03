class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1
        self.refs = 0

    def addWord(self, word, i):
        cur = self
        cur.refs += 1
        for c in word:
            index = ord(c) - ord('a')
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
            cur.refs += 1
        cur.idx = i


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # ============ 第一步：构建 Trie ============
        root = TrieNode()
        for i in range(len(words)):
            root.addWord(words[i], i)

        ROWS, COLS = len(board), len(board[0])
        res = []  # 存储找到的单词

        # ============ 辅助函数：字符转索引 ============
        def getIndex(c):
            index = ord(c) - ord('a')
            return index

        # ============ 核心 DFS 函数 ============
        def dfs(r, c, node):
            # ---------- 剪枝条件 ----------
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or  # 越界
                board[r][c] == '*' or                          # 已访问（标记为'*'）
                not node.children[getIndex(board[r][c])]):     # Trie中没有这个字符
                return

            # ---------- 保存当前字符并标记为已访问 ----------
            tmp = board[r][c]     # 保存原字符，回溯时恢复
            board[r][c] = '*'     # 标记为已访问（避免重复使用）
            
            # ---------- 移动到 Trie 的下一个节点 ----------
            prev = node                              # 保存父节点（用于剪枝时删除子节点）
            node = node.children[getIndex(tmp)]      # 移动到当前字符对应的子节点
            
            # ---------- 检查是否找到完整单词 ----------
            if node.idx != -1:
                # 找到单词！idx 记录了单词在 words 中的索引
                res.append(words[node.idx])
                
                # --- 避免重复添加 ---
                node.idx = -1  # 标记为已找到
                
                # --- 动态剪枝：减少引用计数 ---
                node.refs -= 1
                
                # --- 激进剪枝：如果没有其他单词经过此节点，砍掉整个分支 ---
                if not node.refs:
                    prev.children[getIndex(tmp)] = None  # 从父节点断开
                    node = None                          # 释放当前节点
                    board[r][c] = tmp                    # 恢复棋盘
                    return                               # 提前返回（这条路走完了）

            # ---------- 递归搜索四个方向 ----------
            dfs(r + 1, c, node)  # 下
            dfs(r - 1, c, node)  # 上
            dfs(r, c + 1, node)  # 右
            dfs(r, c - 1, node)  # 左

            # ---------- 回溯：恢复棋盘状态 ----------
            board[r][c] = tmp

        # ============ 第二步：从每个格子开始 DFS ============
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)  # 从根节点开始匹配

        return res
        