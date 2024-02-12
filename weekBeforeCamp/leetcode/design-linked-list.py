class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0
    
    
        
    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        
        cur = self.head
        for i in range(0, index):
            cur = cur.next
        return cur.val
   
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
            

    def addAtTail(self, val: int) -> None:
        
        self.addAtIndex(self.length,val)

        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return 
    
        cur = self.head
        newNode = Node(val)
        if index <= 0:
            newNode.next = cur
            self.head = newNode
        else:
            for _ in range(index-1):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode
        self.length += 1

        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length or index<0:
            return
        
        cur = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                cur = cur.next
            cur.next = cur.next.next

        self.length -=1
        

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)