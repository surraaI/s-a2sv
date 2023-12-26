class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)-1,-1,-1):
            for j in range(i):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1]  =  heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
         
        return names

