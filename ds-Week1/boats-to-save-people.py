class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = 0
        people.sort()
        i = 0
        j = len(people)-1
        while i <= j:
            if people[i] + people[j] <= limit:
                m += 1
                i += 1
                j -= 1
            elif people[i] + people[j] > limit:
                m += 1
                j -= 1
            
        return m
            