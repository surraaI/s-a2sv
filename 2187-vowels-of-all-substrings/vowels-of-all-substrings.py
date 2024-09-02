class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        total_sum = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        for i, char in enumerate(word):
            if char in vowels:
                total_sum += (i + 1) * (n - i)
        
        return total_sum    