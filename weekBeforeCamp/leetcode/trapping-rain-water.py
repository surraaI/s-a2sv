class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ans = 0
        for  r, rightBound in enumerate(height):
            while stack and height[stack[-1]] < rightBound:
                b = height[stack.pop()]
                if stack:
                    l,leftBound = stack[-1], height[stack[-1]]
                    minBound = min(rightBound, leftBound)
                    ans += (r-l-1) * (minBound - b)
            stack.append(r)
        
        return ans

                

