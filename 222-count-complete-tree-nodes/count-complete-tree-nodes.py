# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        que = deque()
        que.append(root)
        nodes = 1
        while que:
            curr = que.popleft()
            if curr.left:
                que.append(curr.left)
                nodes +=1
            if curr.right:
                que.append(curr.right)
                nodes +=1
        
        return nodes


            
        
        