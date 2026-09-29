class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ss = {}
        tt = {}

        for i in s:
            ss[i] = ss.get(i,0)
        for i in t:
            tt[i] = tt.get(i,0)
        
        for key,val in tt.items():
            if ss[key] != val:
                return False
        for key,val in ss.items():
            if tt[key] != val:
                return False

        return True