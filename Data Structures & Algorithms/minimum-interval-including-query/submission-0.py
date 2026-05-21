class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        qq = {}

        for s,e in intervals:
            i = e-s+1
            for r in range(s,e+1):
                qq[r] = min(i,qq.get(r,float('inf')))
        
        res = [qq.get(i,-1) for i in queries]

        return res

