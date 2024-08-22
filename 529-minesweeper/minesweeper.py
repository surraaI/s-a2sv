class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        m = len(board)
        n = len(board[0])
        q = deque()
        q.append(click)
        visited = set()
        visited.add(tuple(click))
        while q:
        
            for _ in range(len(q)):
                curr = q.popleft()
                x, y = curr[0], curr[1]
                
                
                count_mine = 0
                for a,b in [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,1),(1,-1)]:
                    nx, ny = x+a, y+b

                    if 0 <= nx < m and 0 <= ny < n:
                        if board[nx][ny] == 'M':
                            count_mine += 1
                if count_mine > 0:
                    board[x][y] = str(count_mine)
                else:
                    board[x][y] = 'B'
                    for a, b in [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1),(1,1),(1,-1)]:
                        nx, ny = x+a, y+b

                        if 0 <= nx < m and 0 <= ny < n and (nx,ny) not in visited:
                            q.append([nx,ny])
                            visited.add((nx,ny))
        return board