"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        h = []
        res = 0

        for i in intervals:
            heapq.heappush(h,i.end)
            while h[0] <= i.start :
                heapq.heappop(h)
            res = max(res,len(h))

        return res