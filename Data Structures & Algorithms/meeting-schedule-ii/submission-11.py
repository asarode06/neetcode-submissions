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
        ends = []
        maxRooms = 0
        for i, interval in enumerate(intervals):
            while ends and ends[0] <= interval.start:
                heapq.heappop(ends)
            heapq.heappush(ends, interval.end)
            maxRooms = max(maxRooms, len(ends))
        return maxRooms