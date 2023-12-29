class Solution:
    def smallestNumber(self, num: int) -> int:
        s = str(abs(num))
        print(s)
        if len(s) < 2:
            return num
        else:
            ls = [digit for digit in s]
            ls = sorted(ls, reverse= num<0)
            if ls[0] == '0':
                i = 0
                while i <len(ls) and ls[i] == '0':
                    i += 1
                ls[0], ls[i] = ls[i], ls[0]
        return int(''.join(ls)) if num>=0 else -1* int(''.join(ls))

