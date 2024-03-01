from typing import Optional
from collections import deque

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        
        def isValid(root):
            if not root:
                return (True, float('inf'), float('-inf'), 0)
            
            left_valid, left_min, left_max, left_sum = isValid(root.left)
            right_valid, right_min, right_max, right_sum = isValid(root.right)
            
            if left_valid and right_valid and left_max < root.val < right_min:
                curr_sum = left_sum + right_sum + root.val
                ans[0] = max(ans[0], curr_sum)
                return (True, min(left_min, root.val), max(right_max, root.val), curr_sum)
            
            return (False, 0, 0, 0)
        
        isValid(root)
        return ans[0]