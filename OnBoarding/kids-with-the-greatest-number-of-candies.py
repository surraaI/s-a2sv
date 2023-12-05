class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        boolean = [0] * n
        for i in range(n):
            if candies[i] + extraCandies >= max(candies):
                boolean[i] = True
            else:
                boolean[i] = False
        return boolean