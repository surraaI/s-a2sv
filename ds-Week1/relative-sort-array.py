class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cur = 0
        for j in range(len(arr2)):
            
            for i in range(len(arr1)):
                if arr1[i] == arr2[j]:
                    temp = arr1[cur]
                    arr1[cur] = arr1[i]
                    arr1[i] = temp
                    cur +=1 
        k = cur
        while k < len(arr1):
              minEl = arr1[k]
              n = k + 1
              while n < len(arr1):
                     if arr1[n] < minEl:
                            temp = minEl
                            minEl = arr1[n]
                            arr1[k] = minEl
                            arr1[n] = temp
                     n += 1
              k +=1
              
            

                
        return arr1

