class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        else:
            i = 0
            while i < len(arr)-1:
                if arr[i] < arr[i+1]:
                    i += 1
                elif arr[i] == arr[i+1]:
                    return False
                else:
                    if i == 0:
                        return False
                    else:
                        break
            if i == len(arr)-1:
                return False
            while i < len(arr)-1:
                if arr[i] > arr[i+1]:
                    i += 1
                else:
                    return False
            return True
                

            
            
                
        