class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 
            
            dirs = [(-1, 0), (1, 0), (0, 1), (0,-1)]

            if board[r][c] != "O":
                return
                
            board[r][c] = "E"
            for dr, dc in dirs:
                nr, nc = r+ dr, c + dc
                dfs(nr, nc)

        for r in range(ROWS):
            if board[r][0]  == "O":
                dfs(r, 0)
            if board[r][COLS-1] == "O":
                dfs(r, COLS-1)

        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0, c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "E":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"