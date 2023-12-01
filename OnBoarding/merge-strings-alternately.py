class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = 0
        w2 = 0
        s = ''
        while w1 < len(word1) and w2 < len(word2):
            s += word1[w1]
            s += word2[w2]
            w1 += 1
            w2 += 1
        
        while w1 < len(word1):
            s += word1[w1]
            w1 += 1
        while w2 < len(word2):
            s += word2[w2]
            w2 += 1
        return s
