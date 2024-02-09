class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * n
        for i in range(n):
            if i == 0:
                prefix_sum[i] = nums[i]
            else:
                prefix_sum[i] = prefix_sum[i-1] + nums[i]
        print(prefix_sum)
        result = [0] * n
        for i in range(n):
            result[i] = ((nums[i]*i) - prefix_sum[i-1]) + (prefix_sum[n-1] - prefix_sum[i]- (nums[i]*(n-i-1))) if i != 0 else (prefix_sum[n-1] - prefix_sum[i]- (nums[i]*(n-i-1))) 
        return result

    