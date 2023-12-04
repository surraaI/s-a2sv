class Solution:
    def printVertically(self, s: str) -> List[str]:
        l = list(s.split(' '))
        i = 0
        ans = []
        for word in l:
            while i < len(word):
                s = ''
                for j in l:
                    if i < len(j):
                        s += j[i]
                    else:
                        s += ' '
                while s[-1] == ' ':
                    s = s[:-1]
                ans.append(s)
                i  += 1
        return ans

        
