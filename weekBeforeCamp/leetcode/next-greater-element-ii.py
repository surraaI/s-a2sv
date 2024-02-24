class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] *n
        stack = []
        for i in range((2*n)-1, -1,-1):
            if not stack:
                stack.append(nums[i%n])
            else:
                if stack[-1] > nums[i%n]:
                    ans[i%n] = stack[-1]
                    stack.append(nums[i%n])
                else:
                    while stack and nums[i%n] >= stack[-1]:
                        stack.pop()
                    if stack:
                        ans[i%n] = stack[-1]
                    stack.append(nums[i%n])
           
        return ans
        