class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        progress = intervals[0][1]
        for i in range(1,len(intervals)):
            l,r = intervals[i]
            if l < progress:
               progress = min(r,progress)
               count += 1
            else:
                progress = r

        return count

