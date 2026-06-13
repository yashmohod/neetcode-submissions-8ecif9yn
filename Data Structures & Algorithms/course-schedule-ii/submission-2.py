class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        aj = {i:[] for i in range(numCourses)}
        for c,p in prerequisites:
            aj[c].append(p)
        
        res = []

        def dfs(c,v):
            if c in v:
                return False
            if len(aj[c]) == 0:
                if c not in res:
                    res.append(c)
                return True
            
            v.add(c)
            cc = aj[c].copy()
            for i in cc:
                if dfs(i,v):
                    aj[c].remove(i)
                else:
                    return False
            v.remove(c)
            res.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i,set()):
                return []
        return res