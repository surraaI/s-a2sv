# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def add(root, low, high, ans):
            if not root:
                return 0
            if root.val <= high and root.val >= low:
                ans += root.val + add(root.left, low, high, ans) + add(root.right, low, high, ans)
            elif root.val < low:
                ans += add(root.right, low, high,ans)
            elif root.val > high:
                ans += add(root.left, low, high,ans)
            return ans
                
        return add(root, low, high, ans)