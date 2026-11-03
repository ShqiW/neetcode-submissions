class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap: [(distance, x, y)]
        distance_list = []
        res = []
        for point in points:
            distance = point[0]*point[0] + point[1]*point[1]
            distance_list.append((distance, point[0], point[1]))
        heapq.heapify(distance_list)

        while k > 0:
            _,x,y= heapq.heappop(distance_list)


            res.append([x, y])
            k -= 1
        return res