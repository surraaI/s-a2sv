class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.prefix_sum = [[0]*(m+1) for i in range(n+1)]
        self.m = matrix
        # for i in range(n+1):
        #     t = []
        #     for j in range(m+1):
        #         t.append(0)
        #     self.prefix_sum.append(t)
        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         self.prefix_sum[i][j] = self.prefix_sum[i-1][j] + self.prefix_sum[i][j-1] - self.prefix_sum[i-1][j-1] + self.m[i-1][j-1]
        for i in range(len(matrix)):
            Sum=0
            for j in range(len(matrix[0])):
                up=self.prefix_sum[i][j+1]  
                Sum+= matrix[i][j]
                self.prefix_sum[i+1][j+1]=Sum +up
        print(self.prefix_sum)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row1][col2+1] - self.prefix_sum[row2+1][col1] + self.prefix_sum[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)