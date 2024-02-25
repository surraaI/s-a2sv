# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.count = 0  #count of concurrent elements
        self.maxc = 0  #maximum count is stored
        self.val = -999  #value of element
        res = []  #resultant array

        def order(root):
            if not root:
                return
            order(root.left)
            if self.val == root.val:
                self.count += 1
            else:
                self.count = 0
                self.val = root.val
            if self.maxc < self.count:
                res.clear()
                res.append(root.val)
            elif self.maxc == self.count:
                res.append(root.val)
            self.maxc = max(self.maxc, self.count)
            order(root.right)

        order(root)
        return res
        
        