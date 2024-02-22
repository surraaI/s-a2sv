# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            newNode = TreeNode(val)
            root = newNode
        def insert(root, val):
            newNode = TreeNode(val)
            curr = root
            if val > curr.val and not curr.right:
                curr.right = newNode
                return 
            elif val > curr.val and curr.right:
                return insert(curr.right, val)
            if val < curr.val and not curr.left:
                curr.left = newNode
                return 
            elif val < curr.val and curr.left:
                return insert(curr.left, val)
        insert(root, val)
        return root
        
        
        