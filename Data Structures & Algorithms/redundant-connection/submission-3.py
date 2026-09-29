class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        aj = {i+1:i+1 for i in range(len(edges))}



        for x,y in edges:
            if aj[x] == aj[y]:
                return [x,y]
            if x<y:
                aj[y]= aj[x]
            else:
                aj[y]= aj[x]

            
        return []

       

