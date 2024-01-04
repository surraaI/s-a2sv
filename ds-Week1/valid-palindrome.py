class Solution:
    def isPalindrome(self, s: str) -> bool:
        res1 = "".join(re.split("[^a-zA-Z0-9]*", s)).lower()
       
        print(res1)
        return res1 == res1[::-1]

        