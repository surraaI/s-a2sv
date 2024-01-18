class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest_sum = float('inf')
        closest_nums = []
    
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
        
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
            
                if current_sum == target:
                # If the sum is equal to the target, return the target
                    return target
            
                if abs(current_sum - target) < abs(closest_sum - target):
                # Update the closest sum and closest numbers if the current sum is closer to the target
                    closest_sum = current_sum
                    closest_nums = [nums[i], nums[left], nums[right]]
            
                if current_sum < target:
                # If the current sum is less than the target, move the left pointer to the right
                    left += 1
                else:
                # If the current sum is greater than the target, move the right pointer to the left
                    right -= 1
    
        return closest_sum


        