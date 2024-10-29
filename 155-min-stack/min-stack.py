class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        mini = val
        if self.minimums:
            mini = min(self.minimums[-1], val)
        
        self.minimums.append(mini)
        
        
    def pop(self) -> None:
        if self.stack:
            curr = self.stack.pop()
            self.minimums.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1
        

    def getMin(self) -> int:
        if self.minimums:
            return self.minimums[-1]

        return -1
            

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()