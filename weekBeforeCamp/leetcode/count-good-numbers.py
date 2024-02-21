class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        odd = n//2
        even = n//2 + n%2
        return (self.binaryExp(5, even)%mod *self.binaryExp(4, odd)%mod)%mod
    
    def binaryExp(self, x, n):
        mod = 1000000007
        if n==0:
            return 1
        if n < 0:
            return 1/self.binaryExp(x, -n)
        
        if n%2==0:
            return self.binaryExp((x*x)%mod, n//2)
        else:
            return x * self.binaryExp((x*x)%mod, (n-1)//2)
        

        
        