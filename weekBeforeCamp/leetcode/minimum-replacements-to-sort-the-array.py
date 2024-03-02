class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        n = len(nums)
        last = nums[-1]

        c = 0
        for i in range(n-2,-1,-1):
            if nums[i] > last:
                t = nums[i] // last
                if nums[i] % last:
                    t += 1
                last = nums[i]//t
                c += t - 1
            else:
                last = nums[i]
            
                
        return c


