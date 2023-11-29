class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3 == 1:
            return []
        else:
            if (num//3)-1 + (num//3) + (num//3)+1 == num:
                return [(num//3)-1, (num//3), (num//3)+1]
            else:
                return []