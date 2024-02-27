# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l =root.left
        r = root.right
        def same(l,r):
            if not l or not r:
                return l == r
            return (l.val==r.val) and same(l.left,r.right) and same(l.right,r.left)
        return same(root.left,root.right)

        