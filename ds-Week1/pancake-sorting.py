class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        for i in range(len(arr)-1, 0,-1):
            m = arr[:i+1].index(max(arr[:i+1]))
            arr = arr[:m+1][::-1] + arr[m+1:]   
            arr = arr[:i+1][::-1] + arr[i+1:]
            ans.append(m+1)
            ans.append(i+1)
        return ans

            

            

