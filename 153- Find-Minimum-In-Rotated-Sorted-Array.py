from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # O(n) solution is very trivial
        # Start doing regular binary search
        left = 0
        right = len(nums)-1
        while left<right:
            mid = left + (right-left)//2
            # If the rightmost element is greater than the middle, then our smallest
            # will be between left and mid
            if nums[mid]<nums[right]:
                right = mid
            # If out middle is greater than the right, then the smallest will be between middle and right
            else:
                left = mid+1
        
        return nums[left]

obj = Solution()
print(obj.findMin([3,4,5,1,2]))
print(obj.findMin([4,5,6,7,0,1,2]))
            