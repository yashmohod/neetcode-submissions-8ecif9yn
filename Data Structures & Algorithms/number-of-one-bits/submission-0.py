class Solution:
    def hammingWeight(self, n: int) -> int:
        
        count = 0 

        while n >0:
            a = n&1
            count += 1 if a else 0
            n = n >> 1
        return count