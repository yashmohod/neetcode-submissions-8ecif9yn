class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        aj = {i+1:i+1 for i in range(len(edges)+1)}



        for x,y in edges:
            if aj[x] == aj[y]:
                return [x,y]

            if aj[x] != x and aj[y] != y:
                aj[x] = min(aj[x],aj[y])
                aj[y] = min(aj[x],aj[y])
            elif aj[x] == x and aj[y] !=y:
                aj[x] = aj[y]
            elif aj[y] == y  and aj[x] != x:
                aj[y] = aj[x]
            else:
                aj[y] = x
        print(aj)
        return []

       

