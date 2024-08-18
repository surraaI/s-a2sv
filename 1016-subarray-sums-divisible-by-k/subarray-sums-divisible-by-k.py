class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = defaultdict(int)
        remainders[0] = 1
        currSum = 0
        result = 0
        for num in nums:
            currSum += num
            if currSum % k in remainders:
                result += remainders[currSum % k]
            
            remainders[currSum%k] += 1
            
        return result