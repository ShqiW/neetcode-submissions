class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.q = []
        for e in nums:
            heapq.heappush(self.q, e)
            if len(self.q) > k:
                heapq.heappop(self.q)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        if len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]
        
