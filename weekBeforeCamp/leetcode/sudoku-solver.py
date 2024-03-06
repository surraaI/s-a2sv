class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
       
        if not board:
            return False

    
        def is_valid(board, row, col, digit):
            # Check if the digit is already present in the same row
            for i in range(9):
                if board[row][i] == digit:
                    return False

            # Check if the digit is already present in the same column
            for i in range(9):
                if board[i][col] == digit:
                    return False

            # Check if the digit is already present in the same 3x3 subgrid
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == digit:
                        return False

            return True

        def solve(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for digit in '123456789':
                            if is_valid(board, row, col, digit):
                                board[row][col] = digit
                                if solve(board):
                                    return True
                                else:
                                    board[row][col] = '.'  # backtrack
                        return False
            return True

        solve(board)
        return board