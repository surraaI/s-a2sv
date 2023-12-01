class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}
        s = s[::-1]
        num = 0
        for i in range(len(s)):
            
            num+=d[s[i]]
            if i>0 and d[s[i]] < d[s[i-1]]:
                num -= 2*d[s[i]]
        return num


