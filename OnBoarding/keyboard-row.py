class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        ans = []
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        for i in words:
            if i[0].lower() in r1:
                cur = r1
            elif i[0].lower() in r2:
                cur = r2
            elif i[0].lower() in r3:
                cur = r3
            flag = True
            for j in i.lower():

                if j not in cur:
                    flag = False
                    print(j, cur)

            if flag:
                ans.append(i)
        return ans