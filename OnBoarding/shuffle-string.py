class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        y = list(zip(s,indices))
        y.sort(key=lambda x:x[1])
        s = ''
        for i in range(len(y)):
            s+= y[i][0]
        return s