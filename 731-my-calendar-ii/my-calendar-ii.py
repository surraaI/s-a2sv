class MyCalendarTwo:

    def __init__(self):
        self.events = []   
        self.overlaps = []  

    def book(self, start: int, end: int) -> bool:
        
        for overlap_start, overlap_end in self.overlaps:
            
            if max(start, overlap_start) < min(end, overlap_end):
                return False  

        for event_start, event_end in self.events:
           
            if max(start, event_start) < min(end, event_end):
                overlap_start = max(start, event_start)
                overlap_end = min(end, event_end)
                self.overlaps.append((overlap_start, overlap_end))

        self.events.append((start, end))
        return True