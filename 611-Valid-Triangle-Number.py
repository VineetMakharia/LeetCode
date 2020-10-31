from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-1,1,-1):
            anchor = nums[i]
            low = 0
            high = i - 1
            while low < high:
                if nums[high]+nums[low] > anchor:
                    count += high-low
                    high -= 1
                else:
                    low += 1
        return count

obj = Solution()
tc = [[2,2,3,4], [1,2,3,4,5,6]]
for t in tc:
    print(obj.triangleNumber(t))
