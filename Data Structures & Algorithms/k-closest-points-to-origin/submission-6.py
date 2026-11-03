class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []

        for p in points:
            dist = p[0]**2 + p[1]**2
            heapq.heappush(q, (-dist, p))
            while len(q) > k:
                heapq.heappop(q)

        return [p for _, p in q]
