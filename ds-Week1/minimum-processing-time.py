class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        temp = []
        c =0
       
        for i in range(0,len(tasks)-3,4):
            temp.append(processorTime[c]+tasks[i+3])
            
            c += 1

        return max(temp)
        
