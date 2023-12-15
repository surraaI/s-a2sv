class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        if str(n)[0] == '-':
            return False
        visited = []
        while n != 1:
            s = str(n)
            tn = 0
            for i in s:
                tn += int(i) **2
            if tn != 1 and tn not in visited:
                visited.append(tn)
            elif tn != 1 and tn  in visited:
                return False
            n = tn
        return True





