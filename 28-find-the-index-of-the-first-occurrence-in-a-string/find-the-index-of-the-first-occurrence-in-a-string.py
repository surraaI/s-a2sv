class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        base = 27
        MOD = 10**9 + 7
        n, k = len(haystack), len(needle)

        
        if k == 0:
            return 0

        if k > n:
            return -1

        needle_hash = 0
        window_hash = 0
        base_pow = 1  

        for i in range(k):
            needle_hash = (needle_hash * base + (ord(needle[i]) + 1)) % MOD
            window_hash = (window_hash * base + (ord(haystack[i]) + 1)) % MOD
            if i < k - 1:
                base_pow = (base_pow * base) % MOD

        if needle_hash == window_hash:
            return 0

        for i in range(k, n):
            window_hash = (window_hash - (ord(haystack[i - k]) + 1) * base_pow) % MOD
            window_hash = (window_hash * base + (ord(haystack[i]) + 1)) % MOD

            if window_hash == needle_hash:
                if haystack[i - k + 1:i + 1] == needle:
                    return i - k + 1

        return -1
