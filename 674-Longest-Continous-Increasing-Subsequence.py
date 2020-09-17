class Solution:
    def findLengthOfLCIS(self, nums):
        left = 0
        right = 0
        if not nums:
            return 0
        window_size = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                right+=1
            else:
                left=right
            window_size=max(window_size,right-left+1)
        return window_size

obj = Solution()
print(obj.findLengthOfLCIS([1,3,5,7,4,6]))