class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        num_row, num_col = len(heights), len(heights[0])

        pacific_q = deque()
        atlantic_q = deque()

        for i in range(num_row):
            pacific_q.append((i,0))
            atlantic_q.append((i,num_col - 1))
        for i in range(num_col):
            pacific_q.append((0,i))
            atlantic_q.append((num_row-1, i))
        
        def bfs(q):
            reachable = set()
            while q:
                row, col = q.popleft()
                reachable.add((row, col))
                dirs = [(-1, 0),(1, 0),(0,-1),(0,1)]
                for x, y in dirs:
                    new_row, new_col = row+x, col + y
                    if new_row < 0 or new_row >= num_row or new_col < 0 or new_col >= num_col:
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    if heights[new_row][new_col] < heights[row][col]:
                        continue
                    q.append((new_row, new_col))
            return reachable
            
        pacific_reachable = bfs(pacific_q)
        atlantic_reachable = bfs(atlantic_q)
        return list(pacific_reachable.intersection(atlantic_reachable))