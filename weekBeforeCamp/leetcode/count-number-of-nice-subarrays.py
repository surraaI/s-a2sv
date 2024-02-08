class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        nice_subarrays = 0
        current_count = 0
     

        for right in range(len(nums)):
            
            if nums[right]%2 != 0:
                current_count += 1
                count = 0
            if current_count == k:
                
                while left < len(nums) and nums[left] % 2 ==0:
                    count+=1
                    left += 1
                
                count += 1
                current_count -= 1
                left += 1
            nice_subarrays += count
        return nice_subarrays
            
