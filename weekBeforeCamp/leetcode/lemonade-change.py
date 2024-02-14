class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5:0, 10:0, 20:0}
        for i in range(len(bills)):
            if bills[i] == 5:
                d[5] += 1
            elif bills[i] == 10:
                if d[5] == 0:
                    return False
                d[5] -= 1
                d[10] += 1
            elif bills[i] == 20:
                if d[5] < 1:
                    return False
                else:
                    if d[10] >= 1:
                        d[10] -= 1
                        d[5] -= 1
                        d[20] += 1
                    else:
                        if d[5] < 3:
                            return False
                        else:
                            d[5] -= 3
        return True
