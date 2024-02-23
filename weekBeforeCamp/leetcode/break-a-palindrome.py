class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        arr = [i for i in palindrome]
        if len(palindrome) <=1:
                return ''
            
             
        t = True
        for i in range(len(palindrome)//2):
            if palindrome[i] == 'a':
                continue
            else:
                arr[i] = 'a'
                t = False
                break
        if t:
            arr[-1] = 'b'
        return ''.join(arr)
        