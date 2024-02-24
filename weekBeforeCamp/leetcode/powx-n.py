class Solution:
    def myPow(self, x: float, n: int) -> float:
        def Pow(x,n):
            if n == 0:
                return 1.0
            half = Pow(x, n // 2)
            if n % 2 == 0:
                return half * half
            else:
                if n > 0:
                    return x * half * half
                else:
                    return (half * half) / x
        if n < 0:
            n = -n
            return 1/Pow(x,n)
        else:
            return Pow(x, n)


        