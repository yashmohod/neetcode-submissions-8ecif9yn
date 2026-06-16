class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0 

        for i in range(len(s)):

            d = 0
            while i-d>-1 and i+d < len(s) and s[i+d] == s[i-d]:
                res+=1
                d+=1
            
            l,r = 0,1
            while i-l>-1 and i+r < len(s) and s[i-l] == s[i+r]:
                res +=1
                l+=1
                r+=1
        return res