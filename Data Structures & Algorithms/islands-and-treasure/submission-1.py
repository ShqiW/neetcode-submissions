from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        
        # 步骤1: 找到所有宝藏，加入队列作为起点
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:  # 宝藏
                    queue.append((r, c))
        
        # 四个方向：上、下、左、右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # 步骤2: BFS 扩散
        while queue:
            r, c = queue.popleft()
            
            # 尝试四个方向
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # 检查是否在边界内
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                # 只处理陆地 (INF)
                if grid[nr][nc] != 2147483647:
                    continue
                
                # 更新距离 = 当前距离 + 1
                grid[nr][nc] = grid[r][c] + 1
                
                # 加入队列继续扩散
                queue.append((nr, nc))
