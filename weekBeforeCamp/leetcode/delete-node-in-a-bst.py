# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return
        def inOrderSuccessor(root):
            root = root.right
            while root and root.left:
                root = root.left
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and root.right:
                return root.right
            elif not root.right and root.left:
                return root.left
            elif not root.right and not root.left:
                return None
            else:
                temp = inOrderSuccessor(root)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
        return root
        

