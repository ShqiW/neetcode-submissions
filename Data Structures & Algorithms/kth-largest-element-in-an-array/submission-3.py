class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = 0
        pq = []
        for num in nums:
            heapq.heappush(pq, num)
            size += 1
            if size > k:
                heapq.heappop(pq)
        return pq[0]