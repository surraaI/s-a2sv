class Solution:
    def getLucky(self, s: str, k: int) -> int:
     
        
        s_toInt = ''
        for ch in s:
            s_toInt += str(ord(ch)-96)

        for _ in range(k):
            t = 0
            for n in s_toInt:
                t += int(n)
            s_toInt = str(t)

        return int(s_toInt)
        