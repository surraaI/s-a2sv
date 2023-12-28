class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            for j in range(1,len(s)-i):
                if int(s[j][-1]) < int(s[j-1][-1]):
                    s[j],s[j-1] = s[j-1], s[j]
            s[len(s)-i-1] = s[len(s)-i-1][:-1]
        return ' '.join(s)
        

            

        