class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [[] for _ in range(n)]
        cols = [[] for _ in range(n)]
        boxes = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                idx = (i//3)*3+j//3

                num = board[i][j]
                if num == ".":
                    continue
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                if num in boxes[idx]:
                    return False

                rows[i].append(num)
                cols[j].append(num)
                boxes[idx].append(num)
        
        return True
