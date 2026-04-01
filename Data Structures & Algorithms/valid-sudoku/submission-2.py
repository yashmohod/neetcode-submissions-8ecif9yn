class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen :
                    return False
                if board[i][j] != ".":
                    seen.add( board[i][j] ) 
        
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen :
                    return False
                if board[j][i] != ".":
                    seen.add( board[j][i] ) 
        
        for x in range(0,9,3):
            for y in range(0,9,3):
                print(x,y)
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[x+i][y+j] in seen:
                            return False
                        if board[x+i][y+j] != ".":
                            seen.add(board[x+i][y+j])
        
        return True