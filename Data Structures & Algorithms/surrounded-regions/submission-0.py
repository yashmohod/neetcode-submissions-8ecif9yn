class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(x,y):
            board[y][x] = "a"
            for dx,dy in dirs:
                xx,yy = dx+x, dy+y
                if 0<=xx<len(board[0]) and 0<=yy<len(board) and board[yy][xx] == "O":
                    dfs(xx,yy)
        
        for x in range(len(board[0])):
            if board[0][x] == "O":
                dfs(x,0)
            if board[len(board)-1][x] == "O":
                dfs(x,len(board)-1)

        for y in range(len(board)):
            if board[y][len(board[0])-1] == "O":
                dfs(len(board[0])-1,y)
            if board[y][0] == "O":
                dfs(0,y)

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "O":
                    board[y][x] = "X"
                if board[y][x] == "a":
                    board[y][x] = "O"