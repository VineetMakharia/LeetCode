from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        # sort by starting time and if there is similar start time then choose the one ending first
        intervals.sort(key=lambda x: (x[0],-x[1]))
        earliest_start_time = intervals[0][0]
        latest_end_time = intervals[0][1]
        
        for start,end in intervals[1:]:
            if start > latest_end_time:
                res.append([earliest_start_time,latest_end_time])
                earliest_start_time = start
                latest_end_time = end
            else:
                latest_end_time = max(latest_end_time,end)
        res.append([earliest_start_time,latest_end_time])
        return res

obj = Solution()
print(obj.merge([[1,3],[2,6],[8,10],[15,18]]))