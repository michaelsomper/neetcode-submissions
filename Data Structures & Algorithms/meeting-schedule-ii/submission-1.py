"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        intervals = sorted(intervals, key=lambda interval: interval.start)

        i = 0
        rooms = 1

        room_starts = []
        heapq.heappush(room_starts, 0)

        while i < len(intervals):
            start_time = heapq.heappop(room_starts)
            
            if start_time <= intervals[i].start:
                heapq.heappush(room_starts, intervals[i].end)
            else:
                heapq.heappush(room_starts, intervals[i].end)
                heapq.heappush(room_starts, start_time)
                rooms += 1
        
            i += 1
        
        return rooms

