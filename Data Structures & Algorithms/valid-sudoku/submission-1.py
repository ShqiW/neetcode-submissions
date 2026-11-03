class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        grid = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                grid_idx = (i // 3) * 3 + (j // 3)
                if num == ".":
                    continue
                if num in row[i] or num in col[j] or num in grid[grid_idx]:
                    return False
                row[i].append(num)
                col[j].append(num)
                grid[grid_idx].append(num)
        return True
