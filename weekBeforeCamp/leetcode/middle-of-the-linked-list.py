# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        fast = head
        slow = head
        while fast:
            if fast.next:
                fast = fast.next.next 
                slow = slow.next
            else:
                break
        return slow 


        