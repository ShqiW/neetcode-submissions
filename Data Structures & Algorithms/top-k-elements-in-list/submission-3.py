class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_to_freq = Counter(nums)
        q = []
        for num, freq in val_to_freq.items():
            heapq.heappush(q, (freq, num))
            if len(q) > k:
                heapq.heappop(q)
        
        res = []
        while q:
            res.append(heapq.heappop(q)[1])
        return res
        