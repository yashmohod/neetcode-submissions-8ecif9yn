class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            l = str(len(i))
            res +=l+"#"+i

        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        cn = ""
        res = []
        p = 0

        while p < len(s):

            if not s[p] == "#":
                cn +=s[p]
                p+=1
            else:

                l = int(cn)
                print(l)
                res.append(s[p+1:p+1+l])
                p = p+l+1
                cn = ""
        
        return res
