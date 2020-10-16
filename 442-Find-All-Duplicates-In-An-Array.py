from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Doing it with hash_map is very easy
        # Trick is to use the array a hash map itself
        # Since we are given that 1<=a[i]<n
        n = len(nums)
        res = []
        for i in range(n):
            num = abs(nums[i])
            idx = num - 1
            if nums[idx]<0:
                res.append(num)
            else:
                nums[idx] = -nums[idx] 
        return res

obj = Solution()
print(obj.findDuplicates([4,3,2,7,8,2,3,1]))