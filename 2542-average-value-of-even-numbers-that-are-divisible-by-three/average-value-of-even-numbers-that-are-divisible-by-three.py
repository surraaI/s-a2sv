class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s = 0
        n = 0 
        for num in nums:
            if num%2 == 0 and num%3 == 0:
                s += num
                n += 1
        
        return s // n if n else 0

        