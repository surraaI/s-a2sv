# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        length = 0
        prev = head

        while tail:
            prev = tail
            tail = tail.next
            length += 1
        tail = prev
        
        mid = (length//2)
        curr = head
        if length <= 2:
            return head
        while mid > 0 and curr:
            temp = curr.next
            curr.next = temp.next
            temp.next = None
            tail.next = temp
            tail = tail.next
            curr = curr.next
            
            mid -= 1
        return head


        