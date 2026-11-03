class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append([i, j])
        
        INF = 2**31-1
        while q:
            sz = len(q)


            for _ in range(sz):
                x, y = q.popleft()
                dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for dx, dy in dirs:
                    nx, ny = dx+x, dy+y
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny] == INF:
                        grid[nx][ny] = grid[x][y] + 1
                        q.append((nx, ny))
