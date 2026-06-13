class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        aj = {i:[] for i in range(numCourses)}

        for c,p in prerequisites:
            aj[c].append(p)

        def dfs(c,v):
            if c in v:
                return False
            if len(aj[c]) == 0 :
                return True
            v.add(c)
            cc = aj[c].copy()
            for i in cc:
                if dfs(i,v):
                    aj[c].remove(i)
                else:
                    return False
            v.remove(c)
            return True

        
        for i in range(numCourses):
            if not dfs(i,set()):
                return False
        return True