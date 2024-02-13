# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1]*n for i in range(m) ]
        directions = [(0,1), (1,0),(0,-1), (-1,0)]
        currDir = 0
        rows = m
        cols = n
        row , col =0,0
        top = 0
        buttom = rows-1
        left = 0
        right = cols-1
        while head:
            print(row, col)
            matrix[row][col] = head.val
            row += directions[currDir][0]
            col += directions[currDir][1]
            if row > buttom:
                currDir = 2
                row -= 1
                col -= 1
                right -= 1
            elif row < top:
                currDir = 0
                row += 1
                col +=1
                left +=1
            elif col > right:
                currDir = 1
                col -= 1
                row += 1
                top += 1
            elif col < left:
                currDir = 3
                col += 1
                row -= 1
                buttom -= 1
            
            head = head.next
        return matrix





        