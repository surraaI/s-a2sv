class Solution:
    def numSquares(self, n: int) -> int:
        # Initialize dp array
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        # Precompute all perfect squares less than or equal to n
        squares = []
        for i in range(1, int(n**0.5) + 1):
            squares.append(i * i)
        
        # Fill the dp array
        for i in range(1, n + 1):
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        
        return dp[n]