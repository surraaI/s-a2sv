class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex  ==  0:
            return [1]
        elif rowIndex ==1:
            return [1,1]
        rowBefore = self.getRow(rowIndex-1)
        row = [1]
        for i in range(1, rowIndex):
            row.append(rowBefore[i-1]+rowBefore[i])
        row.append(1)
        return row

        