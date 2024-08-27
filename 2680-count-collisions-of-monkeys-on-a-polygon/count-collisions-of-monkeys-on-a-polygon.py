class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7
        total_moves = pow(2, n, MOD)  # Calculate 2^n % (10^9 + 7)
        result = (total_moves - 2) % MOD
        return result

        