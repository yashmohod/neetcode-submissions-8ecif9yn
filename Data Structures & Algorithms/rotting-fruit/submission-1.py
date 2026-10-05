class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    q.append((x,y,0))
        dirs = [[0,1],[0,-1],[-1,0],[1,0]]
        res = -1
        while q:
            x,y,a = q.popleft()
            res = max(a,res)
            if grid[y][x] == 2:
                for dx,dy in dirs:
                    xx = x+dx
                    yy = y+dy

                    if 0<= yy < len(grid) and 0<= xx <len(grid[0]) and grid[yy][xx] == 1:
                        grid[yy][xx] = 2
                        q.append((xx,yy,a+1))
        
        return res if res>0 else -1