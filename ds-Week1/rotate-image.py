class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
       

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i >= j:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        

        for row in range(len(matrix)):
            l,r = 0,len(matrix[0]) - 1
            while l <= r:

                matrix[row][l],matrix[row][r] = matrix[row][r],matrix[row][l]
                l+=1
                r-=1