class MyCalendar:
    
    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.bookings) == 0:
            self.bookings.append([startTime, endTime])
            return True
        for s, e in self.bookings:
            if not (e <= startTime or endTime <= s):
                return False
        self.bookings.append([startTime, endTime])
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)