class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque([])
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    q.append((x,y,0))
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        res = 0

        while q:
            x,y,z = q.popleft()
            res = max(res,z)

            for dx,dy in dirs:
                xx = dx+x
                yy = dy+y

                if 0<=xx< len(grid[0]) and 0<=yy<len(grid) and grid[yy][xx] == 1:
                    grid[yy][xx] = 2
                    q.append((xx,yy,z+1))
        
        for y in grid:
            if 1 in y:
                return -1
        return res