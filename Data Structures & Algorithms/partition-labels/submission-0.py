class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        h={}
        for i in range(len(s)):
            h[s[i]] = max(i,h.get(s[i],-1))
        
        si = 0
        e = 0
        res = []

        for i in range(len(s)):
            
            if si <= e :
                si+=1
            else:
                res.append(si)
                si = 0 
            
            e = h[s[i]]
        return res
