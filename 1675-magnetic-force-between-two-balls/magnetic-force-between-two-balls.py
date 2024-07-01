class Solution:
    def maxDistance(self, position, m):
        def canPlaceBalls(min_force):
            
            count = 1
            last_position = position[0]
            
            
            for i in range(1, len(position)):
                if position[i] - last_position >= min_force:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False

        
        position.sort()

        
        left = 1
        right = position[-1] - position[0]

        
        while left < right:
            mid = (left + right + 1) // 2
            if canPlaceBalls(mid):
                left = mid  
            else:
                right = mid - 1  
        
        return left
