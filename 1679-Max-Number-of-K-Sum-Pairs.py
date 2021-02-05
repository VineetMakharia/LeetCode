from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        hash_map = defaultdict(int)
        count = 0
        for num in nums:
            needs = k - num
            # print(needs,hash_map)
            # Case 1: If complement exists in the map and the frequency >0 then you could choose these
            if needs in hash_map and hash_map[needs]>0:
                count+=1
                hash_map[needs]-=1
            # Case 2: Does not exist, so add it to the map
            else:
                hash_map[num]+=1
        return count

obj = Solution()
print(obj.maxOperations([1,2,3,4],5))
print(obj.maxOperations([3,1,3,4,3],6))
