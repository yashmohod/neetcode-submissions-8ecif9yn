class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0 

        for i in range(32):
            res += 1 if n&1 else 0
            n = n>>1
            if i < 31:
                res = res <<1
        return res
