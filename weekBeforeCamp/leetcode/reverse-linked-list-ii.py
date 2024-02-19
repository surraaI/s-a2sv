# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        n = 0
        dummy_node = ListNode(0)
        dummy_node.next = head
        curr = head
        prev = dummy_node
        leftNode = rightNode = head
        bef_leftNode = after_rightNode = head
        
        while curr:
            prevv = prev
            prev = curr
            n += 1
            curr = curr.next
            if n == left:
                bef_leftNode = prevv
                leftNode = prev
            elif n == right:
                rightNode = prev
                after_rightNode = prev.next
        if n<=1 or right == left:
            return head
        curr = leftNode.next
        prev = leftNode
        leftNode.next = after_rightNode
        bef_leftNode.next = rightNode
        for i in range(right-left):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return dummy_node.next

             
        

        