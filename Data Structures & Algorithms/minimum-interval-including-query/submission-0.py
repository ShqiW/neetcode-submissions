class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_query = sorted(enumerate(queries), key = lambda x:x[1])

        res = {}
        heap = [] #(size, right)
        i = 0

        for idx, q in sorted_query:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            
            # 移除 right < q 的过期 interval
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            # 堆顶就是答案
            res[idx] = heap[0][0] if heap else -1
        
        return [res[i] for i in range(len(queries))]