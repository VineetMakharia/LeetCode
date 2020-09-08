class Solution:
    def firstMissingPositive(self, nums):
        # Using the array itself as hash_map
        is_one_present = False
        for i in nums:
            if i==1:
                is_one_present=True
                break

        if not is_one_present:
            return 1

        for i in range(len(nums)):
            if nums[i]<=0:
                nums[i]=1

        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if idx<len(nums) and nums[idx]>0:
                nums[idx] = -nums[idx]
        
        for i in range(len(nums)):
            if nums[i]>0:
                return i+1
        return len(nums)+1    
        
        # O(n) space and time
#         from collections import Counter
#         hash_map = Counter(nums)
#         i = 1
#         while True:
#             if i not in hash_map:
#                 return i
#             i+=1

obj = Solution()
print(obj.firstMissingPositive([1,2,0]))
print(obj.firstMissingPositive([3,4,-1,1]))
print(obj.firstMissingPositive([7,8,9,11,12]))