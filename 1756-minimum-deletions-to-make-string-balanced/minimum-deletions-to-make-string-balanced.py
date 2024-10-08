class Solution:
    def minimumDeletions(self, s: str) -> int:
        count_b = 0 
        min_deletions = 0  
        
        for char in s:
            if char == 'b':
                count_b += 1
            elif char == 'a':
                min_deletions = min(min_deletions + 1, count_b)
        
        return min_deletions