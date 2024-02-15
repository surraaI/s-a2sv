class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count = 0 
        covered = 0  
        flag = False                                
        if nums[0] != 1:
            count += 1
            covered = 1
        else:
            covered = 1
            flag = True
        
         
        for j in range(len(nums)):
            
           
            if j==0 and flag:
                continue
    
            if nums[j] <= covered+1:
                covered += nums[j]
            
            elif nums[j] > (covered + 1):
                 
                while covered < nums[j]-1:
                    covered += (covered + 1)
                    count += 1
                    if covered >= n:
                        break
                
                covered += nums[j]

            print(count)
            if covered >= n:
                break
            
        while covered < n:
            covered += (covered+1)
            count += 1

        return count
