class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        aj = {i:[] for i in range(n)}

        for x,y in edges:
            aj[x].append(y)
            aj[y].append(x)
        for i in range(n):
            if len(aj[i]) == 0 :
                return False
            
        
        def dfs(c,v):
            v.add(c)
            cc = True
            for i in aj[c]:
                if i in v:
                    return False
                else:
                    cc = cc and dfs(i,v)
            v.remove(c)
            return True

        
        for i in range(n):
            if not dfs(i,set()):
                return False
        return True