class Solution:

    def encode(self, strs: List[str]) -> str:
        
        strs = [str(len(i))+"#"+i for i in strs]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        
        res = []
        l = 0

        while l < len(s):
            r = l
            while s[r] != "#":
                r +=1
            num = int(s[l:r])
            l = r +1
            r = l +num
            res.append(s[l:r])
            l = r
        return res