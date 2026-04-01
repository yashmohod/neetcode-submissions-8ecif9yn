class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()

        pr = 0

        l,r=0,0

        while r<len(s):

            while s[r] in seen:
                seen.remove(s[l])
                l+=1

            seen.add(s[r])
            pr = max(r-l+1,pr)
            r+=1
        
        return pr


