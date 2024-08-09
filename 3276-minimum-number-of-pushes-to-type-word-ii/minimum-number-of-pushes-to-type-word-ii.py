class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for char in word:
            freq[char] = freq.get(char, 0) + 1
        
        if len(freq) <= 8:
            return len(word)
        
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        turn = 1
        c = 1
        count = 0
        
        for k, v in sorted_freq:
            count += v * turn
            c += 1
            if c > 8:
                turn += 1
                c = 1

        return count
