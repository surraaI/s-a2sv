# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        num = []
        def extractNumbers(root, arr):
            if not root:
                return 
            if root and not root.left and not root.right:
                num.append(root.val)
                arr.append(num.copy())
                num.pop()
            if root:
                num.append(root.val)
                if root.left:
                    extractNumbers(root.left,arr)
                    num.pop()
                if root.right:
                    extractNumbers(root.right,arr)
                    num.pop()
  
        extractNumbers(root,arr)
        s = 0
        for l in arr:
            n = 0
            for j in l:
                n = ((n*10) + j)
                print(n,l)
            s += n
        
        return s


            