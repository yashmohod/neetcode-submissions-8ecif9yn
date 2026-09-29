class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res = []
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def reach(x,y,visited):
            p = y == 0 or x == 0 
            a =  y == len(heights)-1 or x == len(heights[0])-1
            
            for dx,dy in dirs:
                xx = dx+x
                yy = dy+y

                if 0<=xx<len(heights[0]) and 0<=yy<len(heights) and (xx,yy) not in visited and heights[yy][xx] <=heights[y][x]:
                    visited.add((xx,yy))
                    pp,aa = reach(xx,yy,visited)
                    visited.remove((xx,yy))
                    p = p or pp
                    a = a or aa
                if p and a :
                    return p,a
            return p,a



        for y in range(len(heights)):
            for x in range(len(heights[0])): 
                p,a = reach(x,y,set())
                if p and a:
                    res.append([y,x])


        return res