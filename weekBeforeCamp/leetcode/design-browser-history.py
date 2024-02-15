class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.currentPage = self.head

        

    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.currentPage.next = newNode
        newNode.prev = self.currentPage
        self.currentPage = newNode
        
        
        
       


    def back(self, steps: int) -> str:
        curr = self.currentPage
        while steps > 0 and curr.prev:
            curr = curr.prev
            steps -= 1
        self.currentPage = curr
        return self.currentPage.val
        
        
        

    def forward(self, steps: int) -> str:
        curr = self.currentPage
        if not curr.next: 
            return self.currentPage.val
        while steps > 0 and curr.next:
            curr = curr.next
            steps -= 1
        self.currentPage = curr
        return self.currentPage.val

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)