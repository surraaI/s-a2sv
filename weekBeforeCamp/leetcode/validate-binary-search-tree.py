# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [None]
        def inorder(root, prev):
            if root:
                if not inorder(root.left,prev):
                    return False
                if prev[0] != None and root.val <= prev[0].val:
                    return False
                prev[0] = root
                return inorder(root.right,prev)
            return True
            
        return inorder(root,prev)
  
    
