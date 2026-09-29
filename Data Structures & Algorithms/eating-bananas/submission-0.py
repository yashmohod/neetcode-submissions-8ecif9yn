class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        r = max(piles)
        def hr(rr):
            res = 0 
            for i in piles:
                res+= math.ceil(i/rr)
            return res
        p = 0 
        while hr(r) <= h:
            p = r
            r = r//2

        return p