class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        
        target_sum = nums_sum // k
        nums.sort(reverse=True)
        if nums[0] > target_sum:
            return False
        
        subset_sums = [0] * k
        
        def backtrack(index):
            if index == len(nums):
                return True
            for i in range(k):
                if subset_sums[i] + nums[index] <= target_sum:
                    subset_sums[i] += nums[index]
                    if backtrack(index+1):
                        return True
                    subset_sums[i] -= nums[index]
                if subset_sums[i] == 0:
                    break
            return False
        
        return backtrack(0)