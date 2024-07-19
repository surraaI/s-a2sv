# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [1]
            
            left_leaves = dfs(node.left)
            right_leaves = dfs(node.right)
            
            
            for l in left_leaves:
                for r in right_leaves:
                    if l + r <= distance:
                        count[0] += 1
            
            
            return [l + 1 for l in left_leaves] + [r + 1 for r in right_leaves]
        
        count = [0]
        dfs(root)
        return count[0]