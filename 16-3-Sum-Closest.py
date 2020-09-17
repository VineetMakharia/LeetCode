class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                current = nums[i]
                total = current + nums[left] + nums[right]
                if abs(target-total)<abs(min_diff):
                    min_diff = target-total
                if total < target:
                    left+=1
                else:
                    right-=1
            if min_diff==0:
                break
        return target-min_diff

obj = Solution()
print(obj.threeSumClosest([-1,2,1,-4],1))