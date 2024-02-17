# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        sorted_head = ListNode(0)
        sorted_head.next = head
        curr = head.next
        sorted_tail = head
        
        while curr:
            
            if curr.val >= sorted_tail.val:
                sorted_tail = curr
                curr = curr.next
                
            else:
                sorted_tail.next = curr.next
                place = sorted_head
                while place.next.val < curr.val:
                    place = place.next
                curr.next = place.next
                place.next = curr
                curr = sorted_tail.next
             
        return sorted_head.next