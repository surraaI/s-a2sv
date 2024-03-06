class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, queens, diagonals, anti_diagonals, cols):
            if row == n:
                result.append(queens)
                return
            for col in range(n):
                diagonal = row - col
                anti_diagonal = row + col
                if col in cols or diagonal in diagonals or anti_diagonal in anti_diagonals:
                    continue
                backtrack(row + 1, queens + [col], diagonals | {diagonal}, anti_diagonals | {anti_diagonal}, cols | {col})

        result = []
        backtrack(0, [], set(), set(), set())
        return len(result)