class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        for row in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[row][j] != matrix[row-1][j-1]:
                    return False
        return True

       
        


       

