"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        What's the maximum number of meetings that overlap? Each time a meeting overlaps, 
        we need another day.

        When would the answer be 0? If there are no meetings
        '''
        if not intervals:
            return 0
        
        '''
        When would the answer be 1? If there is only 1 meeting, or many meetings but none of
        them overlap
    
        How would we determine if a meeting overlaps? Same way we did in the previous problem
        We sort the array by the interval start times, and check if the previous end time overlaps
        with the next start time
        '''
        intervals.sort(key=lambda x:x.start)

        '''
        We need to store the meetings that are happening, and then remove them when they end.
        Heap data structure is a good choice for this, due to its self-ordering property.
        We store the meetings by ending time in the heap, which represents the amount of meeting rooms we need
        at the given moment. 
        '''
        heap = []

        #global max to keep a track of max heap length (this is our number of rooms)
        max_rooms = 0

        for interval in intervals:
            start, end = interval.start, interval.end
            '''
            When a new meeting starts, we check in the heap for all the meetings that have ended (start >= heap[0])
            remove the meetings at the top of the heap that have ended
            '''
            while heap and heap[0] <= start:
                heapq.heappop(heap)
        
            heapq.heappush(heap, end)
            '''
            keep a track of the max length of the heap, return the value at the end
            '''
            max_rooms = max(max_rooms, len(heap))
        
        return max_rooms