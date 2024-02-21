# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        curr = dummyNode
        def merge(curr, dummyNode,list1, list2):
            if list1 and list2 and list1.val <= list2.val:
                temp = list1.next
                list1.next = None
                curr.next = list1
                list1 = temp
                curr = curr.next
                print(dummyNode.next)
            elif list1 and list2 and list1.val > list2.val:
                temp = list2.next
                list2.next = None
                curr.next = list2
                list2 = temp
                curr = curr.next
            if list1 and list2:
                return merge(curr, dummyNode,list1, list2)
            elif list1 and not list2:
                curr.next = list1
                return dummyNode.next
            elif list2 and not list1:
                curr.next = list2
                return dummyNode.next
            elif not list1 and not list2:
                return dummyNode.next
        return merge(curr, dummyNode,list1, list2)

        
        