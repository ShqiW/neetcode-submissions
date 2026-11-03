class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1,1,1,2,2,2,3,3,3
        # 4,4,4,5,5,5,6,6,6
        # row = i//3 * 3
        # col = col//3

        n = len(board)
        row = [[] for _ in range(n)]
        col = [[] for _ in range(n)]
        grid = [[] for _ in range(9)] 
        for i in range(n):
            for j in range(n):
                nums = board[i][j]
                if nums == '.':
                    continue
                if board[i][j] in row[i]:
                    return False
                
                if board[i][j] in col[j]:
                    return False
                if board[i][j] in grid[(i//3)*3 + j//3]:
                    return False
                
                row[i].append(nums)
                col[j].append(nums)
                grid[(i//3)*3 + j//3].append(nums)
        return True

        