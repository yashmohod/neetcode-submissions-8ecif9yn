class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pe = intervals[0][1]
        res = 0
        for s,e in intervals[1:]:

            if s >= pe:
                pe = e
            else:
                res +=1
                pe = min(pe,e)

        return res



