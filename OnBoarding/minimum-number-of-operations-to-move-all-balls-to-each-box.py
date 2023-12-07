class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans =[0] * len(boxes)
        for i in range(len(boxes)):
            a = 0
            for j in range(len(boxes)):
                if j == i:
                    continue
                else:
                    if boxes[j]=='1':
                        a += abs(j-i)
            ans[i] = a
        return ans


        