class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        aj = {i:[] for i in range(n)}

        for x,y in edges:
            aj[x].append(y)
            aj[y].append(x)

        rs= set()
            
        cyc = False
        def dfs(c,v):
            rs.add(c)
            for i in aj[c]:
                if i!= v:
                    if i in rs : 
                        cyc = True
                        return 
                    else:
                        dfs(i,c)
        dfs(0,0)
        return len(rs) == n and not cyc
