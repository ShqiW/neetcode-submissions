class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(i):
            if i == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for j in range(n):
                if self.isSafe(board, i, j):
                    board[i][j] = "Q"
                    backtrack(i+1)
                    board[i][j] = "."
        
        backtrack(0)
        return res
    
    def isSafe(self, board, r, c):
        row = r - 1
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
        
        row, col = r-1, c-1
        while row >= 0 and col>=0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1
        
        row, col = r-1, c+1
        while row >= 0 and col <len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1
        return True
        