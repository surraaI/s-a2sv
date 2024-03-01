class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        current_permutation = []
        used = [False] * len(nums)
        
        def backtrack():
            if len(current_permutation) == len(nums):
                permutations.append(current_permutation[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current_permutation.append(nums[i])
                    backtrack()
                    used[i] = False
                    current_permutation.pop()
        
        backtrack()
        return permutations