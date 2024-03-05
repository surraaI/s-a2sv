# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder_bts(self, root):
        if not root:
            return []
        return self.inorder_bts(root.left) + [root] + self.inorder_bts(root.right)
    
    def construct_bst(self, left, right, path):
        if left > right:
            return None
        middle = (left+right)//2
        path[middle].left = self.construct_bst(left, middle-1, path)
        path[middle].right = self.construct_bst(middle+1, right, path)
        return path[middle]
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        path = self.inorder_bts(root)
        return self.construct_bst(0, len(path)-1, path)