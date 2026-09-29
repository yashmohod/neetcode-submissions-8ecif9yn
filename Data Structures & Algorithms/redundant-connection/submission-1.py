class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        aj = {}
        for x,y in edges:
            if x not in aj:
                aj[x] = []
            if y not in aj:
                aj[y] = []
            aj[x].append(y)
            aj[y].append(x)
        
        visited = set()

        def dfs(c,p):
            if c in visited:
                return [[p,c]]
            visited.add(c)
            for i in aj[c]:
                if i == p:
                    continue
                cc = dfs(i,c)
                if cc != None:
                    cc.append([p,c])
                    return cc
        
        cc = dfs(1,-1)

        for i in range(len(edges)-1,-1,-1):
            if edges[i] in cc:
                return edges[i]

