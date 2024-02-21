class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """
        start = 0
        end = len(s)-1
        def swap(s, start, end):
            if start+1 == end:
                s[start] , s[end] = s[end], s[start]
                return s
            elif start == end:
                    return s
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            return swap(s, start, end)
            
        return swap(s, start, end)

        
        