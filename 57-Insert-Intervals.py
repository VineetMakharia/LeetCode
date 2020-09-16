class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i, n = 0, len(intervals)
        # Case 1: Traverse until no conflict
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        mI = newInterval
        # Case 2: Conflict --> Find min and max until the next intervals x is not greater than the new Intervals y
        while i < n and intervals[i][0] <= newInterval[1]:
            mI[0] = min(mI[0], intervals[i][0])
            mI[1] = max(mI[1], intervals[i][1])
            i += 1
        result.append(mI)
        # Case 3: No conflict, keep on appending
        while i < n:
            result.append(intervals[i])
            i += 1
        return result

obj = Solution()
print(obj.insert([[1,3],[6,9]],[2,5]))
print(obj.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
        