class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirs = [[0,1],[0,-1],[-1,0],[1,0]]

        def dfs(x,y,z):

            if z  == len(word):
                return True
            if board[y][x] != word[z]:
                return False

            for dx,dy in dirs:
                if dfs(x+dx,y+dy,z+1):
                    return True
            
            return False
    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and dfs(j,i,0):
                    return True
        return False






