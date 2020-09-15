class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Basic Idea is to use the array itself as hash_map
        for i in range(len(nums)):
            current_num = abs(nums[i]) - 1 # 0 indexed
            if nums[current_num] > 0:
                nums[current_num]*=-1
        return [idx+1 for idx,val in enumerate(nums) if val>0]

obj = Solution()
print(obj.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
