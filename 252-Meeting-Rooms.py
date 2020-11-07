from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #Sort by start times
        if not intervals:
            return True
        intervals.sort(key=lambda x:x[0])
        first_end = intervals[0][1]
        for start,end in intervals[1:]:
            if start < first_end:
                return False
            first_end = end
        return True

tc = [[[0,30],[5,10],[15,20]],[[7,10],[2,4]]]
obj = Solution()
for t in tc:
    print(obj.canAttendMeetings(t))
