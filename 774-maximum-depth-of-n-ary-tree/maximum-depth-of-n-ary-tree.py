"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        que = deque()
        visited = set()
        que.append(root)
        visited.add(root)
        c = 0

        while que:
            n = len(que)
            c += 1
            for _ in range(n):
                curr = que.popleft()
                for child in curr.children:
                    if child not in visited:
                        que.append(child)
                        visited.add(child)
        return c


        