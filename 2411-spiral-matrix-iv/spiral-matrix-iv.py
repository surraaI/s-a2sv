# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1] * n for _ in range(m)]
        top, bottom, left, right = 0, m-1, 0, n-1

        flag = True
        while head:
            for i in range(left,right+1):
                if head:
                    mat[top][i] = head.val
                    head = head.next
                else:
                    flag = False
                    break

            if not flag:
                break

            top += 1
            for i in range(top, bottom+1):
                if head:
                    mat[i][right] = head.val
                    head = head.next
                else:
                    flag = False

            if not flag:
                break
            
            right -= 1
            for i in range(right, left-1, -1):
                if head:
                    mat[bottom][i] = head.val
                    head = head.next
                else:
                    flag = False
                    break

            if not flag:
                break
            
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                if head:
                    mat[i][left] = head.val
                    head = head.next
                else:
                    flag = False
                    break
            
            left += 1

        return mat




        