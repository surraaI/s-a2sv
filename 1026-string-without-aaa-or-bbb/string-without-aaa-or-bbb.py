class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        
        while a > 0 or b > 0:
            if a > b:
                if len(result) >= 2 and result[-1] == result[-2] == 'a':
                    result.append('b')
                    b -= 1
                else:
                    result.append('a')
                    a -= 1
            else:
                if len(result) >= 2 and result[-1] == result[-2] == 'b':
                    result.append('a')
                    a -= 1
                else:
                    result.append('b')
                    b -= 1

        
        return ''.join(result)