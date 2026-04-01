class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        r = max(piles)
        def hr(rr):
            res = 0 
            for i in piles:
                res+= math.ceil(i/rr)
            return res
        p = 0 
        l=0
        while l<=r :
            m = (l+r)//2
            if m == 0:
                break
            if hr(m) <= h:
                p = m
                r = m-1
            else:
                l = m+1
            

        return p