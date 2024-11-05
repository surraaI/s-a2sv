class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x and bottoms[i] == x:
                    rotations_top += 1
                elif bottoms[i] != x and tops[i] == x:
                    rotations_bottom += 1

            return min(rotations_top, rotations_bottom)

        s = set(tops)
        for n in bottoms:
            s.add(n)

        ans = float('inf')
        for n in s:
            rotations = check(n)
            if rotations != -1:
                ans = min(ans, rotations)
        
        return ans if ans != float('inf') else -1
