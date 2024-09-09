# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
       
        def helper(curr_head, curr_root):
            if not curr_head :
                return True
            if not curr_root:
                return False
            if curr_head.val == curr_root.val:
                return helper(curr_head.next,curr_root.left) or helper(curr_head.next,curr_root.right)
            else:
                return False

        if not root:
            return False

        return helper(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        
        