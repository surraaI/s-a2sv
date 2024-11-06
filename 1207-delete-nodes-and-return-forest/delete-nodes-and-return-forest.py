# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete) 
        result = []

        def helper(node, parent_exists):
            if not node:
                return None

            node_to_delete = node.val in to_delete_set

            if not node_to_delete and not parent_exists:
                result.append(node)

            node.left = helper(node.left, not node_to_delete)
            node.right = helper(node.right, not node_to_delete)

            return None if node_to_delete else node

        
        helper(root, False)
        return result