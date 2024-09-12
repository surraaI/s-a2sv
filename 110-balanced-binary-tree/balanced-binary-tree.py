# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0, True  
            
            left_height, left_balanced = check(node.left)
            right_height, right_balanced = check(node.right)
            
            balanced = (left_balanced and right_balanced and abs(left_height - right_height) <= 1)
            
            height = 1 + max(left_height, right_height)
            
            return height, balanced
        
        # We only need the balanced status from the root
        _, is_balanced = check(root)
        return is_balanced
