class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        m = ''
        while i < len(num) -2:
            if len(set(num[i:i+3])) == 1:
                if m == '':
                    m = num[i:i+3]

                elif int(m[0]) < int(num[i][0]):
                    m = num[i:i+3]
              
                
            i+=1
        return str(m)