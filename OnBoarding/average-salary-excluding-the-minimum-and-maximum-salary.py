class Solution:
    def average(self, salary: List[int]) -> float:
        s = salary.sort()
        s = sum(salary[1:-1])
        return s/(len(salary)-2)