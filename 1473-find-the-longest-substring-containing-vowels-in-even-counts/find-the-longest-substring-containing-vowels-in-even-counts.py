class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        
        
        seen = {0: -1}  
        
        bitmask = 0  
        max_len = 0  
        
        for i, char in enumerate(s):
        
            if char in vowels:
                bitmask ^= vowels[char]
            
            
            if bitmask in seen:
                max_len = max(max_len, i - seen[bitmask])
            else:
                seen[bitmask] = i
        
        return max_len
        