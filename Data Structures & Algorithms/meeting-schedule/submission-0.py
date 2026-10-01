"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sort_interval = sorted(intervals,key = lambda x: (x.start,x.end))
        last_j = -1
        for interval in sort_interval:
            i = interval.start
            j = interval.end
            if i < last_j:
                return False
            else:
                last_j = j
        return True