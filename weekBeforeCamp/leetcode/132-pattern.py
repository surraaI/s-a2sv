class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = []
        mini2 = float('-inf')

        for i in range(n-1,-1,-1):
            if i == n-1:
                stack.append(nums[i])
            if nums[i] < mini2 :
                return True
            if nums[i] < stack[-1] :
                stack.append(nums[i])
            elif nums[i] > stack[-1] :
                c = 0
                while stack and nums[i] > stack[-1]:
                    mini2 = stack[-1]
                    stack.pop()                    
                stack.append(nums[i])

        return False