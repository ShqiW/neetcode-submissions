class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROW, COL = len(grid), len(grid[0])

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        dirs = [(-1, 0), (1,0), (0,-1), (0,1)]

        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                point = q.popleft()
                for dir in dirs:
                    x, y = point[0]+dir[0], point[1]+dir[1]
                    if 0 <= x < ROW and 0<=y<COL and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x,y))
            step += 1
        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return -1
        
        return step -1 if step else 0