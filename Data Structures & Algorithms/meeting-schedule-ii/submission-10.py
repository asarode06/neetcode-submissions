"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i: i.start)
        rooms = []
        maxRooms = 0
        for i, interval in enumerate(intervals):
            while rooms and rooms[0][0] <= interval.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, (interval.end, i, interval))
            maxRooms = max(maxRooms, len(rooms))
        return maxRooms