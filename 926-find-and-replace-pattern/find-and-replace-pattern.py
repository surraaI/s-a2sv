class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for i in range(len(words)):
            if len(words[i]) != len(pattern):
                continue
            
            px1 = {}
            px2 = {}
            n = len(pattern)
            flag = True
            for j in range(n):
                if pattern[j] in px1:
                    if px1[pattern[j]] != words[i][j]:
                        flag = False
                        break
                if words[i][j] in px2:
                    if px2[words[i][j]] != pattern[j]:
                        flag = False
                        break

                px1[pattern[j]] = words[i][j]
                px2[words[i][j]] = pattern[j]

            if flag:
                ans.append(words[i])

        return ans
                