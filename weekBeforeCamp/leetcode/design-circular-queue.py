class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = deque()
        

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue.append(value)
            return True
        return False
        
        
        

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.queue.popleft()
            return True
        return False 

        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[0]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[-1]
        

    def isEmpty(self) -> bool:
        if len(self.queue)==0:
            return True
        return False

        

    def isFull(self) -> bool:
        if len(self.queue)== self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()