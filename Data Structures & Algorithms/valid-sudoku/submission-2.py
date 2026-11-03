class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        grid = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                g_i = (i//3) * 3 + (j//3)
                if num == ".":
                    continue
                if num in rows[i] or num in cols[j] or num in grid[g_i]:
                    return False
                rows[i].append(num)
                cols[j].append(num)
                grid[g_i].append(num)
        return True       