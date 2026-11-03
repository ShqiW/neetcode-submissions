class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n-1

        while left <= right:
            mid = (left+right)//2
            num = self.getNum(matrix, mid)
            if num == target:
                return True
            elif num > target:
                right = mid -1
            else:
                left = mid + 1
        return False
    

    def getNum(self, matrix, idx):
        m, n = len(matrix), len(matrix[0])
        i = idx // n
        j = idx % n
        return  matrix[i][j]
        