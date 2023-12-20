class Bitset:

    def __init__(self, size: int):
        self.arr1 = ['0'] * size
        self.arr2 = ['1'] * size
        self.oneC1 = 0
        self.oneC2 = size
        self.size = size
        
        
    def fix(self, idx: int) -> None:
        if self.arr1[idx] == '0':
            self.oneC1 += 1
            self.oneC2 -= 1
        
        self.arr1[idx] = '1'
        self.arr2[idx] = '0'
        
        
             

    def unfix(self, idx: int) -> None:
        if self.arr1[idx] == '1':
            self.oneC1 -= 1
            self.oneC2 += 1
        
        self.arr1[idx] = '0'
        self.arr2[idx] = '1'
        

        

    def flip(self) -> None:
        self.arr1, self.arr2 = self.arr2, self.arr1
        self.oneC1, self.oneC2 = self.oneC2, self.oneC1
        
       
    def all(self) -> bool:
        return self.size == self.oneC1
       

    def one(self) -> bool:
        return self.oneC1 != 0
        
    def count(self) -> int:
        return self.oneC1
       

    def toString(self) -> str:
        return ''.join(self.arr1)
       
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()