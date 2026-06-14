class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N  = len(edges)+1
        aj = [i for i in range(N)]
        rank = [1]*N
        def find(x):
            if aj[x] != x:
                aj[x] = find(aj[x])
            return aj[x]
        
        def union(x,y):
            xf,yf = find(x),find(y)

            if xf == yf:
                return False

            if rank[xf] > rank[yf]:
                aj[yf] = xf
                rank[xf] += rank[yf]
            else:
                aj[xf] = yf
                rank[yf] += rank[xf]
            
            return True
        
        for x,y in edges:
            if not union(x,y):
                return [x,y]
            
        


        

       

