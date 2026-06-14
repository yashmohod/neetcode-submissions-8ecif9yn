class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        l,r=1,1

        for _ in range(n):
            l,r = r,l+r
        
        return l

