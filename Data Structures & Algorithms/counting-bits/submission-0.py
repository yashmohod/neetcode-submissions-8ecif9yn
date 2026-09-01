class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            c = i 
            count = 0 
            while c >0:
                count += 1 if c & 1 else 0 
                c = c>>1
            res.append(count)

        return res 
