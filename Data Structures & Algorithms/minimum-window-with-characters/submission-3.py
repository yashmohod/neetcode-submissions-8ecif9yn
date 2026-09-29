class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        td = {}
        for i in t :
            td[i] = td.get(i,0)+1
        sd = {}
        for i in s :
            sd[i] = sd.get(i,0)+1   

        l,r=0,len(s)-1
        while l < len(s):
            if s[l] in td:
                if sd[s[l]]>td[s[l]]:
                    sd[s[l]] = sd.get(s[l]) -1
                else:
                    break
            l+=1
        while r>-1:
            if s[r] in td:
                if sd[s[r]]>td[s[r]]:
                    sd[s[r]] = sd.get(s[r]) -1
                else:
                    break
            r-=1
        print(l,r)
        for i in td.keys():
            if i not in sd or td[i] > sd[i]:
                return ""
        return s[l:r+1]
                
        