from typing import List
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        left = 0
        right = len(A)-1
        ans = -1
        while left<right:
            ln = A[left]
            rn = A[right]
            if ln+rn>=K:
                right-=1
            else:
                ans = max(ans,(ln+rn))
                left+=1
        
        return ans
                
obj = Solution()
print(obj.twoSumLessThanK([34,23,1,24,75,33,54,8],60))