
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        
        dct = defaultdict(lambda: [float("inf"), float("inf"), -1, -1])
        for row in range(len(targetGrid)):
            for col in range(len(targetGrid[0])):
                dct[targetGrid[row][col]][0] = min(row, dct[targetGrid[row][col]][0])
                dct[targetGrid[row][col]][1] = min(col, dct[targetGrid[row][col]][1])
                dct[targetGrid[row][col]][2] = max(row, dct[targetGrid[row][col]][2])
                dct[targetGrid[row][col]][3] = max(col, dct[targetGrid[row][col]][3])
        dct2 = {}
        for key in dct:
            dct2[key] = set()
        for row in range(len(targetGrid)):
            for col in range(len(targetGrid[0])):
                guh = 0
                for key in dct:
                    if dct[key][0] <= row <= dct[key][2] and dct[key][1] <= col <= dct[key][3]:
                        if key != targetGrid[row][col]:
                            dct2[targetGrid[row][col]].add(key)
        def dfs(seen, key):
            if key in dct3:
                return dct3[key]
            elif dct2[key] == set():
                dct3[key] = 0
                return 0
            else:
                guh = 0
                for value in dct2[key]:
                    if key in seen and value in seen:
                        return -1
                    seen.add(key)
                    x = dfs(seen.copy(), value)
                    if x == -1:
                        return -1
                    guh = max(guh, x)

                dct3[key] = guh+1
                return dct3[key]
        dct3 = {}
        for key, value in dct2.items():
            if -1 == dfs(set(), key):
                return False
        return True
        