from typing import List
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        right = 0
        longest = 0
        zeroes_seen = 0
        
        while right<len(A):
            if A[right] == 0:
                zeroes_seen+=1
            while zeroes_seen > K:
                if A[left]==0:
                    zeroes_seen-=1
                left+=1
            longest = max(longest,right-left+1)
            right+=1
        return longest

obj = Solution()
print(obj.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))