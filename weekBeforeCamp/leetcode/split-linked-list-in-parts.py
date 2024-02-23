# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        _ = head
        n = 0
        ans = []
        while _:
            _ = _.next
            n += 1
        curr = head
        i = 0
        rem = n%k
        m = 1
        print(n, rem)
        if n <= k:
            c = 0
            while curr:
                ans.append(curr)
                prev = curr
                curr = curr.next
                prev.next = None
                c += 1
        else:
            c = 0
            while curr:
                if rem == 0:
                        m = 0
                if c == 0:
                    ans.append(curr)
                    c += 1
                elif c == ((n//k)+m):
                    prev = curr
                    curr = curr.next
                    prev.next = None
                    c = 0
                    print('m',m)
                    if rem > 0:
                        rem -= 1
                    
                else: 
                    curr = curr.next
                    c += 1
        while len(ans) < k:
            ans.append(None)
        return ans
       