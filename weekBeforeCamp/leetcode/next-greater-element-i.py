class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        for i in range(len(nums2)-1,-1,-1):
            if not stack:
                d[nums2[i]] = -1
                stack.append(nums2[i])
            elif stack and stack[-1] < nums2[i]:
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                if stack:
                    d[nums2[i]] = stack[-1]
                else:
                    d[nums2[i]] = -1
                stack.append(nums2[i])   
            else:
                top = stack[-1]
                d[nums2[i]] = top
                stack.append(nums2[i])
          
        ans = []
            
        for i in nums1:
            ans.append(d[i])
        return ans

                
        