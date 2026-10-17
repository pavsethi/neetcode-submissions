"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 1:
            return 1
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x: x.start)
        end_times = []
        for interval in intervals:
            if end_times and end_times[0] <= interval.start:
                heapq.heapreplace(end_times, interval.end)
            else:
                heapq.heappush(end_times, interval.end)
      
        return len(end_times)
                


