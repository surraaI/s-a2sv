# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head

        while (cur):
            cur = cur.next
            length += 1
        cur = head
        prev = head
        if n > length:
            return
        else:
            ind = 0
            while (cur) and ind < length - n:
                prev = cur
                cur = cur.next
                ind += 1
            prev.next = cur.next
        length -= 1
        if length - n + 1 == 0:
            head = prev.next
        return head
        
        
