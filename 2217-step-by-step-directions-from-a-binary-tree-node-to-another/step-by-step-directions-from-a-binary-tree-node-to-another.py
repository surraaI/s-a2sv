# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLCA(self, root: TreeNode, p: int, q: int) -> TreeNode:
        if not root or root.val == p or root.val == q:
            return root
        left = self.findLCA(root.left, p, q)
        right = self.findLCA(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    def findPath(self, root: TreeNode, value: int, path: list) -> bool:
        if not root:
            return False
        if root.val == value:
            return True
        path.append('L')
        if self.findPath(root.left, value, path):
            return True
        path.pop()
        path.append('R')
        if self.findPath(root.right, value, path):
            return True
        path.pop()
        return False

    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        lca = self.findLCA(root, startValue, destValue)
        
       
        path_to_start = []
        self.findPath(lca, startValue, path_to_start)
        
        
        path_to_dest = []
        self.findPath(lca, destValue, path_to_dest)
        
        
        path_up = ['U'] * len(path_to_start)
        return ''.join(path_up + path_to_dest)