from typing import List
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # Idea is to find 2 1s and then return the halved value
        prev_1_idx = -1
        ans = 0 
        n = len(seats)
        
        # Do it the same same as sliding window
        for cur_idx in range(n):
            # If we encounter a zero, we keep on increasing the window size
            if seats[cur_idx]==0:
                continue
            # We've seen a 1
            else:
                # We've seen a 1, we need to see if this is the first 1 we have seen or not
                # If it is the first 1, our answer would be the right pointer
                # For example, 00001
                # Here, there is only one person sitting, so we sit at the 0th idx, \
                # and our answer would be 4
                # This is for the case where are left sided is an unbounded sliding window
                if prev_1_idx == -1:
                    ans = max(ans,cur_idx)
                # If this is not the first 1 we encounter, our answer would be the difference \
                # between the cur_1_idx and the prev_1_idx divided by 2
                else:
                    ans = max(ans, (cur_idx-prev_1_idx)//2)
            # We now don't need the left one, so we update our left to right
                prev_1_idx = cur_idx
        
        # Edge case where 10000 (ending with 0 and only a single 1 is present in the list)
        # In this example, left = 0, so n-1-left = 5-1-0 = 4 
        # This is the case of an unbounded right hand side sliding window
        # The number of zeroes I have seen would be last_idx - prev_1_idx
        # Here we don't divide by 2 because we want the person to sit on the last idx 
        if seats[n-1]==0:
            ans = max(ans,n-1-prev_1_idx)
        
        return ans

tc = [[1,0,0,0,1,0,1], [1,0,0,0], [0,1]]
obj = Solution()
for t in tc:
    print(obj.maxDistToClosest(t))
            