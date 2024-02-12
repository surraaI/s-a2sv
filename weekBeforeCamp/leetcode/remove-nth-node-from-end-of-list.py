# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy_node = ListNode(0)
        dummy_node.next = head
        right = dummy_node
        left = dummy_node
        c = 0
        while (right.next) and c < n:
            right = right.next
            c += 1
        while (right.next):
            right = right.next
            left = left.next  
        temp = left.next.next if left.next else None
        left.next = temp

       
        return dummy_node.next

        
        
