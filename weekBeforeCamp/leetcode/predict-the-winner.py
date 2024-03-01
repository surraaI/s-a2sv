class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def maxScore(score, left, right, isPlayer1Turn=True):
            if left == right:
                return score + nums[left] if isPlayer1Turn else score - nums[left]
            
            if isPlayer1Turn:
                return max(maxScore(score + nums[left], left+1, right, False),
                           maxScore(score + nums[right], left, right-1, False))
            else:
                return min(maxScore(score - nums[left], left+1, right, True),
                           maxScore(score - nums[right], left, right-1, True))
        
        return maxScore(0, 0, len(nums) - 1) >= 0