class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [n]
        elif n == 1:
            return [0, 1]

        ans = [0] * (n+1)
        ans[1] = 1
        
        for i in range(2, n+1):
            if i%2 == 0:
                ans[i] = ans[i//2]
            else:
                ans[i] = ans[i//2] + 1
        
        return ans
       