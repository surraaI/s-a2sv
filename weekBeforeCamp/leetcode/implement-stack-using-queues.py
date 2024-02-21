class MyStack:

    def __init__(self):
        self.value = []
        

    def push(self, x: int) -> None:
        return self.value.append(x)
        

    def pop(self) -> int:
        if len(self.value) !=0:
            return self.value.pop()
        

        

    def top(self) -> int:
        return self.value[-1]
        

    def empty(self) -> bool:
        return len(self.value) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()