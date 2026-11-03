class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pac, atl = set(), set()

        res = []

        def dfs(i, j, coor_set, prevHeight):
            if (i, j) in coor_set or i < 0 or j < 0 or i == m or j == n or heights[i][j] < prevHeight:
                return
            coor_set.add((i,j))
            dfs(i+1, j, coor_set, heights[i][j])
            dfs(i-1, j, coor_set, heights[i][j])
            dfs(i, j-1, coor_set, heights[i][j])
            dfs(i, j+1, coor_set, heights[i][j])

        for c in range(n):
            dfs(0, c, pac, heights[0][c])
            dfs(m-1, c, atl, heights[m-1][c])
        
        for r in range(m):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, n-1, atl, heights[r][n-1])
        
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

        
