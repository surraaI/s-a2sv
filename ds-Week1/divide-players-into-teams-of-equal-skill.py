class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        print(skill)
        j = len(skill)-1
        teams = []
        for i in range(len(skill)//2):
            teams.append((skill[i],skill[j]))
            j -= 1
        s = teams[0][0] + teams[0][1]
        for i in range(1, len(teams)):
            if teams[i][0] + teams[i][1] != s:
                return -1
        p = 0
        for i in range(len(teams)):
            p += teams[i][0] * teams[i][1]
        return p

        