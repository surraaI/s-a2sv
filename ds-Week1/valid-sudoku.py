class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = 9
        cols = 9
        for row in range(rows):
            d = {}
            for col in range(cols):
                if board[row][col] != '.':
                    d[board[row][col]] = d.get(board[row][col],0) + 1
                    if d[board[row][col]]>1:
                        return False
        for col in range(cols):
            d = {}
            for row in range(rows):
                if board[row][col] != '.':
                    d[board[row][col]] = d.get(board[row][col],0) + 1
                    if d[board[row][col]]>1:
                        return False
        for row in range(0, rows, 3):
            for col in range(0, cols,3):
                d = {}
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j] != '.':
                            d[board[i][j]] = d.get(board[i][j],0) + 1
                            if d[board[i][j]] > 1:
                                return False
        
              
                
        return True
                
        

        