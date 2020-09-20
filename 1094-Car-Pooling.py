class Solution:
    def carPooling(self, trips, capacity):
        arr = []
        for passengers, start, end in trips:
            arr.append((start,passengers))
            arr.append((end,-passengers))
        arr.sort()
        used = 0
        for time, current in arr:
            used += current
            if used>capacity:
                return False
        return True

obj = Solution()
print(obj.carPooling([[2,1,5],[3,3,7]], 4))
print(obj.carPooling([[2,1,5],[3,3,7]], 11))