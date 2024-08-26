"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = []
        que = deque()
        que.append(root)
        # stack.append(root.val)

        while que:
            n = len(que)
            for i in range(n):
                curr = que.pop()
                stack.append(curr.val)
                for ch in curr.children:
                    que.append(ch)

        return stack[::-1]

            


       