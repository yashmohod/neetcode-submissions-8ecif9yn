"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) <1:
            return 0
        intervals.sort(key=lambda x:x.start)
        h = []
        res = 0

        for i in intervals:
            if h and h[0] <= i.start :
                heapq.heappop(h)
            heapq.heappush(h,i.end)
        return len(h)