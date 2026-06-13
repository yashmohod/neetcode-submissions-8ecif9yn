class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        aj = {i:[] for i in range(n)}

        for x,y in edges:
            aj[x].append(y)
            aj[y].append(x)
        
        visited = set()

        def dfs(c,p):
            if c in visited:
                return
            visited.add(c)
            for i in aj[c]:
                if i == p:
                    continue
                dfs(i,c)
        res = 0
        for i in range(n):
            if i not in visited:
                res+=1
            dfs(i,-1)

        return res 
