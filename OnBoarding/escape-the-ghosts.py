class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        # If any of the ghosts reaches the targert before 
        # you, then you lose
        def time(x,y):
            a,b = target
            return max(x,a)-min(x,a) + max(y,b)-min(y,b)
        
        t_p = time(0,0)
        for a,b in ghosts:
            if time(a,b)<= t_p :
                return False 
        return True 