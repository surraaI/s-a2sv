class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeats = -(-len(b) // len(a)) 
    
        repeated_a = a * min_repeats
        if b in repeated_a:
            return min_repeats
        
        # Check if b is a substring in one more repeat
        repeated_a += a
        if b in repeated_a:
            return min_repeats + 1
        
        # Check if b is a substring in two more repeats (very rare but possible)
        repeated_a += a
        if b in repeated_a:
            return min_repeats + 2
        
        # If none of the above contain b, it's impossible
        return -1