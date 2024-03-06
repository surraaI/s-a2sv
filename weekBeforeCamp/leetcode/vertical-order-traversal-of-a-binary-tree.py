# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0, 0)])
        d = {}

        while queue:
            (node, row, col) = queue.popleft()
            if node == None:
                continue
            if col not in d:
                d[col] = [(node.val, row)]
            else:
                (prevnodeval, prevnoderow) = d[col][-1]
                d[col].append((node.val, row))

                ix = 0
                while ix < len(d[col]) and d[col][-1 - ix][1] == row:
                    ix += 1
                
                if ix > 1:
                    self.sort_subarray(d[col], len(d[col]) - ix, len(d[col]) - 1)

            queue.append((node.left, row + 1, col - 1))
            queue.append((node.right, row + 1, col + 1))

        result = []

        for key in sorted(d.keys()):
            result.append(map(lambda x: x[0], d[key]))

        return result

    def sort_subarray(self, arr, i, j):
        if i < 0 or j >= len(arr) or i > j:
            return

        arr[i:j+1] = sorted(arr[i:j+1])