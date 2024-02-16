# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr and curr.val < x:
            prev = curr
            curr = curr.next
        pre = None
        
                    
        while curr and curr.next:
            pre = curr
            curr = curr.next
            if not prev and curr.val < x:
                pre.next = curr.next
                curr.next = head
                head = curr
                prev = curr

            elif curr.val < x and prev:
                t = curr.next
                pre.next = t
                temp = prev.next
                
                curr.next = temp
                prev.next = curr
                
                prev = prev.next
                print(prev)
            
        return head