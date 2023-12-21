class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = []
        clms = len(matrix[0])
        rows = len(matrix)
        for clm in range(clms):
            col = []
            for row in range(rows):
                col.append(matrix[row][clm])
            arr.append(col)
        return arr

        