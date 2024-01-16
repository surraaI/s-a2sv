class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        fruit_map = collections.defaultdict(list)
        fruit_map[fruits[0]] = [0,0]
        current = 0
        max_length = 1

        for idx, fruit in enumerate(fruits[1:], start = 1):
            if (fruit in fruit_map):
                fruit_map[fruit][1] = idx
            elif len(fruit_map) < 2:
                fruit_map[fruit] = [idx, idx]
            else:
                to_remove = min(fruit_map.keys(), key = lambda x: fruit_map[x][1])
 #               print(idx, current, fruit, max_length, fruit_map, to_remove)
                max_length = max(max_length, idx - current)
                current = fruit_map[to_remove][1] + 1
 #               print('after:', current)
                del fruit_map[to_remove]
                fruit_map[fruit] = [idx, idx]

        
        return max(max_length, len(fruits) - current)


                
                
