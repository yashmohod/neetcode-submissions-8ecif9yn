class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ss = {}
        tt = {}

        for i in s:
            ss[i] = ss.get(i,0) +1
        for i in t:
            tt[i] = tt.get(i,0) +1

        for i in s:
            if ss.get(i) != tt.get(i):
                return False
        
        for i in t:
            if ss.get(i) != tt.get(i):
                return False
        
        return True
        
