class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_value = max(nums)
        
        longest = 0
        current_length = 0
        
        for num in nums:
            if num == max_value:
                current_length += 1
                longest = max(longest, current_length)
            else:
                current_length = 0
        
        return longest

            

            