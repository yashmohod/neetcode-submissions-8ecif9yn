class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        l = 0
        res =""
        for i in range(len(s)):

            d = 0
            while i-d>-1 and i+d <len(s) and s[i+d] == s[i-d]:
                if l <= 2*d:
                    res = s[i-d:i+d+1]
                    l = 2*d
                d+=1
            d,dd=0,1
            while i-d>-1 and i+dd <len(s) and s[i-d] == s[i+dd]:
                if l <= d+dd:
                    res = s[i-d:i+dd+1]
                    l=d+dd
                d+=1
                dd+=1
        
        return res
            
