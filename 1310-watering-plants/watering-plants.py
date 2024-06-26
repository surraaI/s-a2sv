class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        can = capacity
        water = -1
        i = 0
        step = 0
        while i < len(plants):
            if plants[i] <= can:
                can -= plants[i]
                i += 1
                step += 1
            else:
                step += i
                can = capacity
                step += i+1
                can -= plants[i]
                i +=1
            print(step)
        return step