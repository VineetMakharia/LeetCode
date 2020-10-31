from typing import List
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Idea is to find 2 1s and then return the halved value
        left = -1
        ans = 0 
        n = len(seats)
        
        for right in range(n):
            # If we encounter a zero, we keep on incrementing
            if seats[right]==0:
                continue
            else:
                # We've seen a 1, we need to see if this is the first 1 we have seen or not
                # If it is the first 1, our answer would be the right pointer
                # For example, 00001
                # Here, there is only one person sitting, so we sit at the 0th idx, \
                # and our answer would be 4
                if left == -1:
                    ans = max(ans,right)
                # If this is not the first 1 we encounter, our answer would be the difference \
                # right and left divided by 2
                else:
                    ans = max(ans, (right-left)//2)
            # We now don't need the left one, so we update our left to right
            left = right
        
        # Edge case where 10000 (ending with 0 and only a single 1 is present in the list)
        # In this example, left = 0, so n-1-left = 5-1-0 = 4 
        if seats[n-1]==0:
            ans = max(ans,n-1-left)
        
        return ans

tc = [[1,0,0,0,1,0,1], [1,0,0,0], [0,1]]
obj = Solution()
for t in tc:
    print(obj.maxDistToClosest(t))
            