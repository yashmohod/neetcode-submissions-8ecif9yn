class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirs = [[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(x,y,z):

            if z  == len(word)-1:
                return board[y][x] == word[z]
            if board[y][x] != word[z]:
                return False

            tmp = board[y][x]
            board[y][x] = '#'

            for dx,dy in dirs:
                if 0 <= x+dx <len(board[0]) and 0 <= y+dy < len(board)  and  dfs(x+dx,y+dy,z+1):
                    return True
            board[y][x] = tmp  
            return False
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and dfs(j,i,0):
                    return True
        return False






