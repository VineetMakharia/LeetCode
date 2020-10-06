from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0:
            return 0
        if len(intervals)==1:
            return 1
        meetings = []
        for start,end in intervals:
            meetings.append((start,1))
            meetings.append((end,-1))
        meetings.sort()
        rooms = 0
        ans = -1
        for _,val in meetings:
            rooms+=val
            ans = max(ans,rooms)
        return ans
obj = Solution()
print(obj.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))
print(obj.minMeetingRooms([[7,10],[2,4]]))