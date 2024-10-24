class Solution:
    def monkeyMove(self, n: int) -> int:
        MOD = 10**9 + 7
        total_moves = pow(2, n, MOD)
        result = (total_moves - 2) % MOD
        return result

        