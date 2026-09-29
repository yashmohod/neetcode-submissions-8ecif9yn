class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        l,r=0,0
        lc=0

        while r<len(s):
            if s[l] == s[r]:
                r+=1
                lc = max(lc,r-l+1)
            else:
                l=r
        
        
        return lc+k if len(s)-lc >=k else len(s)
