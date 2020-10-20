from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_copy = [-1*num for num in nums]
        heapq.heapify(nums_copy)
        k-=1
        while k:
            heapq.heappop(nums_copy)
            k-=1
        return -1*heapq.heappop(nums_copy)


obj = Solution()
print(obj.findKthLargest([3,2,1,5,6,4],2))