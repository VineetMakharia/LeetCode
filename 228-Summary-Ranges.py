from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        left = 0
        right = 1
        ans = []
        while right<len(nums):
            prev = nums[right-1]
            current = nums[right]
            if (current - prev) != 1:
                if (right-left)==1:
                    ans.append(str(nums[left]))
                else:
                    ans.append(str(nums[left])+"->"+str(nums[right-1]))
                left = right
            right+=1
            
        if (right-left)==1:
            ans.append(str(nums[left]))
        else:
            ans.append(str(nums[left])+"->"+str(nums[right-1]))
        return ans

tc = [[0,1,2,4,5,7], [0,2,3,4,6,8,9],[0]]
obj = Solution()
for t in tc:
    print(obj.summaryRanges(t))