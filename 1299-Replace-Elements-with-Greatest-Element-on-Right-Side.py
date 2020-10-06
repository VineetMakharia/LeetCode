from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = mx
            mx = max(temp, mx)
        return arr

obj = Solution()
print(obj.replaceElements([17,18,5,4,6,1]))