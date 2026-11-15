"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        currEnd = None
        for interval in intervals:
            if currEnd and interval.start < currEnd:
                return False
            currEnd = interval.end
        return True