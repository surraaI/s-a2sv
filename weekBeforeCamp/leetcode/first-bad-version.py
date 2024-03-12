# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        while l < r:
            version = l + (r-l)//2
            if isBadVersion(version):
                r = version
            else:
                l = version + 1
        return l