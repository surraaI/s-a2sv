class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(houses):
            prev_max = 0
            curr_max = 0
            for money in houses:
                new_max = max(curr_max, prev_max + money)
                prev_max = curr_max
                curr_max = new_max
            return curr_max

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))