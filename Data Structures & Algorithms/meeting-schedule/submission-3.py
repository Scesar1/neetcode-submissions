"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Base Cases:
        if len(intervals) <= 1:
            return True
        # Start by sorting the array by start times
        intervals.sort(key=lambda x:x.start)

        # Now we just need to check if the previous end time is after the next start time
        for i in range(1, len(intervals)):
            x1, x2 = intervals[i - 1], intervals[i]

            if x1.end > x2.start:
                return False

        
        # In the case of no conflicts, return True
        return True
