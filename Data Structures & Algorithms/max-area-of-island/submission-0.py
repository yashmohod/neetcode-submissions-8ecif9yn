class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = 0 

        dirs =[[1,0],[-1,0],[0,1],[0,-1]]
        def ara(x,y):
            som = 0
            print(x)
            for dx,dy in dirs:
                xx = x+dx
                yy = y+dy
                if 0<=xx<len(grid[0]) and 0<= yy <len(grid) and grid[yy][xx] :
                    grid[yy][xx] = 0
                    som += ara(xx,yy)
            return som+1
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x]:
                    grid[y][x] = 0
                    res = max(ara(x,y),res)
        
        return res