class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) >0 and s[0]=="0":
            return 0
        res = 0

        p = ""

        for i in range(len(s)):
            
            if p == "1" and 0<=int(s[i])<10:
                res+=1
            elif p == "2" and 0<=int(s[i]) < 17:
                res+=1
            if s[i] in ["1","2"]:
                p = s[i]

        return res+1
