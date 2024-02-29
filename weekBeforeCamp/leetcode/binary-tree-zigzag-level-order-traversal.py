# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        ans = []
        if root:
            queue.append(root)
            ans.append([root.val])
        
        while queue:
            temp = []
            n = len(queue)
            i = 0
            while i < n:
                curr = queue.popleft()
                if curr and curr.left:
                    temp.append(curr.left.val)
                    queue.append(curr.left)
                if curr and curr.right:
                    temp.append(curr.right.val)
                    queue.append(curr.right)
                i += 1
            if len(ans)%2 == 0 and temp:
                ans.append(temp)
            elif len(ans)%2 != 0 and temp:
                ans.append(temp[::-1])
        return ans
        
                

        


