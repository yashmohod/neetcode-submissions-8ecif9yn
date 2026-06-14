class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        l,r=1,1

        for i in range(n):
            l,r = r,l+r
        
        return l

