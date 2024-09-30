class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0
        
        window_set = set()
        window_sum = 0
        max_sum = 0
        start = 0

        for end in range(n):
            while nums[end] in window_set:
                window_set.remove(nums[start])
                window_sum -= nums[start]
                start += 1
            
            window_set.add(nums[end])
            window_sum += nums[end]
            
            if end - start + 1 == k:
                max_sum = max(max_sum, window_sum)
                window_set.remove(nums[start])
                window_sum -= nums[start]
                start += 1
        
        return max_sum