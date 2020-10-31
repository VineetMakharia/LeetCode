from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        seen = defaultdict(int)
        ans = 0
        for num in nums:
            ans+=seen[num]
            seen[num]+=1
        return ans

obj = Solution()
print(obj.numIdenticalPairs([1,2,3,1,1,3]))