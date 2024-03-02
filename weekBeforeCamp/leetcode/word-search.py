class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        traversed = set()
        
        def dfs(r, c, i):

            if i == len(word):
                return True
            
            if (min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                or (r, c) in traversed
                or board[r][c] != word[i]):
                return False
            
            traversed.add((r, c))
            found = (dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1))
            traversed.remove((r, c))
            return found
        
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
