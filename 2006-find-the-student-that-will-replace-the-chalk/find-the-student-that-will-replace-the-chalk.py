class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        if len(chalk) == 1:
            return 0
        
        k -= ((k//(sum(chalk))) * sum(chalk))

        while True:
            for i in range(len(chalk)):
                k -= chalk[i]
                if k < 0:
                    return i
            
        