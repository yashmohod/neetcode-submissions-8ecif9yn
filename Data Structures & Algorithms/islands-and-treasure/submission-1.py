class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque([])

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    q.append((x,y,0))

        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        while q :
            x,y,z = q.popleft()
            if grid[y][x] != 0:
                grid[y][x] = min(z,grid[y][x])
            for dx,dy in dirs:
                xx = x+dx
                yy = y+dy
                if 0<=xx<len(grid[0]) and 0<=yy<len(grid) and grid[yy][xx] !=-1 and  grid[yy][xx] !=0 and grid[yy][xx] > z+1:
                    q.append((xx,yy,z+1))
        
            
       