class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        arr = [0] * n
        for a, b, c in  shifts:
            if c==1:
                arr[a] += 1
                if b+1<n:
                    arr[b+1] -= 1
            else:
                arr[a] -= 1
                if b+1<n:
                    arr[b+1] += 1
        prefix_sum = [0] * (n+1)
        for i in range(1,n+1):
            prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
        
        new_str = '' 
        for i in range(1, n+1):
            sh = ord(s[i-1])-ord('a')
            new_str += chr((sh + prefix_sum[i])%26 + ord('a'))
        return new_str
            