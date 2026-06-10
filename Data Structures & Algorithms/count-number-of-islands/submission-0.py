class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0 
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        def setZ(x,y):  
            for dx,dy in dirs:
                xx = dx+x
                yy = dy+y

                if 0<=xx<len(grid[0]) and 0<=yy<len(grid) and grid[yy][xx] == "1":
                    grid[yy][xx] = "0"
                    setZ(xx,yy)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    res +=1
                    setZ(x,y)
        return res
        
        
            

