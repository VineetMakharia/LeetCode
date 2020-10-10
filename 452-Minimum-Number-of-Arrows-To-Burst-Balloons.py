from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 1st idea is to sort based on end points
        # if the next start is greater than the \
        # current end point, we would need an additonal arrow
        if not points:
            return 0
        points.sort(key = lambda x: x[1])
        arrows_needed = 1
        first_end_point = points[0][1]
        for start,end in points:
            if first_end_point < start:
                arrows_needed+=1
                first_end_point = end
        return arrows_needed

obj = Solution()
print(obj.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(obj.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))