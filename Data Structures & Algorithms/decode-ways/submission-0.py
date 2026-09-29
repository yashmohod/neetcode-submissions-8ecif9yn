class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        if s[0] == "0":
            return 0
        else:
            res = 1
        
        p = s[0]

        for i in range(1,len(s)):

            if int(s[i])>0 and int(s[i])<10:
                res +=1
            
            if s[i] == "0" and p in "12":
                res+=1
            p = s[i]
        
        return res
                