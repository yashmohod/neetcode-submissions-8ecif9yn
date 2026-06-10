class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        h={}
        for i in range(len(s)):
            h[s[i]] = i
        
        si = 0
        e = 0
        res = []

        for i in range(len(s)): 
            si+=1
            e = max(h[s[i]],e)
            if e ==i:
                res.append(si)
                si = 0

        return res
