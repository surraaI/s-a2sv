
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        dummy = ListNode(0)
        current = dummy
        curr_sum = 0
        node = head.next
        
        while node:
            if node.val != 0:
                curr_sum += node.val
            else:
                current.next = ListNode(curr_sum)
                current = current.next
                curr_sum = 0
            node = node.next
        
        return dummy.next
