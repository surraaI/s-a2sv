class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([([root],[1])])
        ans = 1
        while queue:
            q,i = [],[]
            cur_level = queue.popleft()
            for cur,index in zip(cur_level[0],cur_level[1]):
                if cur.left:
                    q.append(cur.left)
                    i.append(2*index)
                if cur.right:
                    q.append(cur.right)
                    i.append(2*index+1)
            if q:
                ans = max(ans,i[-1]-i[0]+1)
                queue = deque([(q,i)])
                continue
            queue.clear()
        return ans