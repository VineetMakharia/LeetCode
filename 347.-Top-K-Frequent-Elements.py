from typing import List
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = collections.Counter(nums)
        # hash_map = {1:3, 2:2, 3:1}
        # Basic idea is to maintain a heap of size K
        heap = []
        for key,freq in hash_map.items():
            if len(heap)<k:
                heapq.heappush(heap, (freq,key))
            else:
                heapq.heappushpop(heap, (freq,key))
        print(heap)
        return [key for freq,key in heap]
obj = Solution()
print(obj.topKFrequent([1,1,1,2,2,3],2))