class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == j:
                    s += mat[i][j]
        for i in range(len(mat)):
            for j in range(len(mat[0])-1,-1,-1):
                if i + j == len(mat[0])-1:
                    s += mat[i][j]
        return s - mat[len(mat)//2][len(mat[0])//2] if len(mat)%2 != 0 else s
