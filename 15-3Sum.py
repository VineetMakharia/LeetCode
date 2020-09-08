class Solution:
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            left = i + 1
            right = n - 1
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                current = nums[left]+nums[right]+nums[i]
                if current==0:
                    res.append([nums[i],nums[left],nums[right]])
                    while right>left and nums[right]==nums[right-1]:
                        right-=1
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    left+=1
                    right-=1
                if current > 0:
                    right-=1
                if current < 0:
                    left+=1     
        return res

obj = Solution()
print(obj.threeSum([-1,0,1,2,-1,-4]))
print(obj.threeSum([]))
print(obj.threeSum([0]))
