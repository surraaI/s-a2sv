class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                while j < k:
                
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i] , nums[j] ,nums[k]]
                        ans.append([nums[i] , nums[j] ,nums[k]])
                        while j < k and nums[j]   == triplet[1]:
                            j += 1
                        while j < k and nums[k] == triplet[2]:
                            k -= 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    else:
                        k -= 1
        return ans
        
   