import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.ind ={}

        

    def insert(self, val: int) -> bool:
        if val not in self.arr:
            self.arr.append(val)
            self.ind[val] = len(self.arr)-1
            return True
        else:
            return False


    def remove(self, val: int) -> bool:
        if val in self.arr:
            ti = self.ind[val]
            self.ind[self.arr[len(self.arr)-1]] = self.ind[val]
            self.arr[ti], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1],self.arr[ti]
            self.arr.pop()
            del self.ind[val]
            return True
        else:
            return False

        
        

    def getRandom(self) -> int:
        return random.choice(self.arr)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()