class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        mf = 0
        d = {} 
        res = 0 
        for r in range(len(s)):

            d[s[r]] = d.get(s[r],0)+1
            mf = max(d[s[r]],mf)

            while (r-l+1) - mf >k:
                d[s[l]] -=1
                l+=1
        
            res = max(res,r-l+1)
        return res

