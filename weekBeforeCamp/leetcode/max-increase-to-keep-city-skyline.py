class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
            colMax = {}
            rowMax = {}
            rows = len(grid)
            cols = len(grid[0])
            for row in range(rows):
                for col in range(cols):
                    colMax[col] = max(colMax.get(col, 0), grid[row][col])
                    rowMax[row] = max(rowMax.get(row, 0), grid[row][col])
          
            change = 0
            for row in range(rows):
                for col in range(cols):
                    change += abs(grid[row][col]-min(colMax[col], rowMax[row]))
            return change
            