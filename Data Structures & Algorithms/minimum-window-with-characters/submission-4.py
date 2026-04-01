class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        td = {}
        for i in t :
            td[i] = td.get(i,0)+1
        sd = {}
        have = 0
        need = len(td.keys())
        l=0
        resS = float('inf')
        res = ""
        for r in range(len(s)):
            sd[s[r]] = sd.get(s[r],0)+1
            if s[r] in td and sd[s[r]] == td[s[r]]:
                have +=1
            
            while need == have:
                sd[s[l]] = sd.get(s[l])-1
                if s[l] in td and sd[s[l]] < td[s[l]]:
                    have -=1
                if resS > r-l:
                    res = s[l:r+1]
                    resS = r-l
                l+=1

        return res


