class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res = []
        intervals.sort()
        for i in intervals:
            if res and res[-1][1] >= i[0]:
                z = res.pop()
                res.append([min(z+i),max(z+i)])
            else:
                res.append(i)
        
        return res