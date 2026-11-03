class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l+r)//2
            mid_num = self.get_num(matrix, mid)
            if mid_num == target:
                return True
            elif mid_num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

    
    def get_num(self, matrix, mid):
        i = mid // len(matrix[0])
        j = mid % len(matrix[0])
        return matrix[i][j]