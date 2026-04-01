class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        t ={}
        l = 0
        res = 0 
        for r in range(len(s)):

            if s[r] in t:
                t[s[r]] +=1
                while t[s[r]] >1:
                    t[s[l]] -=1
                    l+=1
            else:
                t[s[r]] = 1
            res = max(res,r-l)

        return res +1 if len(s) >0 else 0