# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length = 0
        tail = head
        while tail:
            length += 1
            prev = tail
            tail = tail.next
        mid = length//2
        curr = head
        prev = None
        while mid > 0:
            prev = curr
            curr = curr.next
            mid -=1
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        mid = length//2

        curr = prev
        while mid > 0 :
            if head.val != curr.val:
                return False
            curr = curr.next
            head = head.next
            mid -= 1
        return True
            




    