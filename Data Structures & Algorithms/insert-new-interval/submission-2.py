class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        intervals.append(newInterval)
        intervals.sort()

        for i in intervals:

            if res and res[-1][1] >= i[0]:
                x = res.pop()
                res.append([min(x+i),max(x+i)])
            else:
                res.append(i)
        
        return res