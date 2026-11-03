class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])

        count = 1

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start < prev_end:
                pass
            else:
                count += 1
                prev_end =  end
        return len(intervals) - count
