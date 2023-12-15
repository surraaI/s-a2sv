class FrequencyTracker:

    def __init__(self):
      
       
        self.numsfreq = {}
        self.frqfreq = {}

    def add(self, number: int) -> None:
        
        if number in self.numsfreq:
            self.frqfreq[self.numsfreq[number]] -= 1
            if self.frqfreq[self.numsfreq[number]] == 0:
                del self.frqfreq[self.numsfreq[number]]
            self.numsfreq[number] = self.numsfreq.get(number, 0) + 1
            self.frqfreq[self.numsfreq[number]]  = self.frqfreq.get(self.numsfreq[number], 0) + 1
        else:
            self.numsfreq[number] = self.numsfreq.get(number, 0) + 1
            self.frqfreq[self.numsfreq[number]]  = self.frqfreq.get(self.numsfreq[number], 0) + 1
     

        

    def deleteOne(self, number: int) -> None:
      
        if number not in self.numsfreq:
            return
        else:
            self.frqfreq[self.numsfreq[number]] -= 1

            
            if self.frqfreq[self.numsfreq[number]] == 0:

                del self.frqfreq[self.numsfreq[number]]
            self.frqfreq[self.numsfreq[number]-1] = self.frqfreq.get(self.numsfreq[number]-1,0) +1
            self.numsfreq[number] -= 1
            if self.numsfreq[number] == 0:
                del self.numsfreq[number]
            
        
   

    def hasFrequency(self, frequency: int) -> bool:
        if frequency in self.frqfreq:
            return True
        else:
            return False
        
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)