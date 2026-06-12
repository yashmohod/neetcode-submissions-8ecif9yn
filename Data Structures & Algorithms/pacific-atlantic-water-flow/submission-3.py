class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p = set()
        a = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def reach(x,y,ocean):
            ocean.add((y,x))
            for dx,dy in dirs:
                xx,yy = x+dx,y+dy

                if 0<=xx<len(heights[0]) and 0<=yy<len(heights) and (yy,xx) not in ocean and heights[yy][xx] >= heights[y][x]:
                    reach(xx,yy,ocean)
            
        for y in range(len(heights)):
            reach(0,y,p)
            reach(len(heights[0])-1,y,a)
        for x in range(len(heights[0])):
            reach(x,0,p)
            reach(x,len(heights)-1,a)

        r = [list(c) for c in (a&p)]
        return r
