class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        while l <= r:
            if ord(letters[l]) > ord(target):
                return letters[l]
            mid = l + (r-l)//2
            if ord(letters[mid]) > ord(target):
                r = mid - 1
                if ord(letters[r]) <= ord(target):
                    return letters[mid]
            else:
                l = mid + 1
        return letters[0]


