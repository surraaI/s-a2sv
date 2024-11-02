class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        base = 27
        MOD = 10**9 + 7
        n = len(needle)
        m = len(haystack)

        if m < n:
            return -1
        
        def convert(char):
            return ord(char) - 96

            
        def add_last(Hash, char):
            return  (Hash * base + convert(char)) % MOD


        def poll_last(Hash, char, base_power):
            return (Hash - convert(char) * base_power) % MOD

        base_powers = [1] * (n + 1)
        for i in range(1, n+1):
            base_powers[i] = (base_powers[i - 1] * base) % MOD


        target = window_hash = 0
        for i in range(n):
            target = add_last(target, needle[i])
        
        for i in range(n):
            window_hash = add_last(window_hash, haystack[i])
        
        if target == window_hash:
            if haystack[:n] == needle:
                return 0
        

        for right in range(n, m):
            left = right - n
            window_hash = add_last(window_hash, haystack[right])
            window_hash = poll_last(window_hash, haystack[left], base_powers[n])

            if window_hash == target:
                if haystack[left+1:right+1] == needle:
                    return right - n + 1

        
        return -1




        
       