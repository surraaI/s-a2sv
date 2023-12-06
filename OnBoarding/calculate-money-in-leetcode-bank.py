class Solution:
    def totalMoney(self, n: int) -> int:
        w = n//7
        r = n%7
        
        sw = (w/2) *((2*28)+((w-1)*7))
        print(w)
        sr = (r/2) * ((2*(w+1))+(r-1))
        return int(sr +sw)
        