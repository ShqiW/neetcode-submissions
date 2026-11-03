class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        prev_start, prev_end = intervals[0][0], intervals[0][1]
        res =[]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i][0], intervals[i][1]
            if cur_start <= prev_end:
                prev_end = max(prev_end, cur_end)
            else:
                res.append([prev_start, prev_end])
                prev_start = cur_start  
                prev_end = cur_end
        res.append([prev_start, prev_end])
        return res