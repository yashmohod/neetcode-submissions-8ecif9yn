class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        aj = {i:[] for i in range(n)}

        for x,y in edges:
            aj[x].append(y)
            aj[y].append(x)

        rs= set()
        
        def dfs(c,p):
            if c in rs :
                return False
            
            rs.add(c)
            for i in aj[c]:
                if i == p:
                    continue
                if not dfs(i,c):
                    return False

            return True
        
        return dfs(0,-1) and  len(rs) == n
