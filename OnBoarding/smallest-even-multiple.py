class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2==0:
            return n
        else:
            c = n
            while c %2!= 0 or c%n!= 0 :
                c+=1
            return c