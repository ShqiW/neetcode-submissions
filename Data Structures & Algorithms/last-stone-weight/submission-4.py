class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            remain = first - second
            if remain > 0:
                heapq.heappush(stones, -remain)
        return 0 if len(stones) == 0 else -stones[0]