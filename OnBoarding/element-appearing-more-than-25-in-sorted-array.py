class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        x = Counter(arr)
        n = len(arr)/4
        for i in x:
            if x[i] > n:
                return i
