class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if n < k:
            return -1
        
        ans = 0
        for i in range(1, n+1 ,1):
            if n % i == 0:
                ans = i
                k -= 1
                if k == 0:
                    break
                
        return ans if k == 0 else -1
            

        