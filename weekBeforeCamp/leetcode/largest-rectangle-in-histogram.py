class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        m = 0
        ranges = {}
        for i in range(len(heights)):
            if not stack:
                stack.append([heights[i],i])
            elif stack and heights[i] >= stack[-1][0]:
                stack.append([heights[i],i])
            elif stack and heights[i] < stack[-1][0]:
                while stack and heights[i] < stack[-1][0]:
                    top = stack.pop()
                    ranges[top[1]] = i - top[1]

                stack.append([heights[i], i])
        while stack:
            top = stack.pop()
            ranges[top[1]] = len(heights) - top[1]
        
        for i in range(len(heights)-1, -1, -1):
            if not stack:
                stack.append([heights[i],i])
            elif stack and heights[i] >= stack[-1][0]:
                stack.append([heights[i],i])
            elif stack and heights[i] < stack[-1][0]:
                while stack and heights[i] < stack[-1][0]:
                    top = stack.pop()
                    ranges[top[1]] += top[1] - i -1
                stack.append([heights[i], i])
        top = stack.pop()
        while stack:
            curr = stack.pop()
            ranges[curr[1]] += curr[1]-top[1]
            
        for ind in ranges:
            m = max(m, heights[ind] * ranges[ind])
        print(ranges)
        return m
        


