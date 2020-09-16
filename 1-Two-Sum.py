class Solution:
	def twoSum(self,nums,target):
		hash_map = dict()
		for idx,num in enumerate(nums):
			complement = target - num
			if complement in hash_map:
				return [hash_map[complement],idx]
			hash_map[num]=idx

		return -1

obj = Solution()
print(obj.twoSum([2,7,11,15],9))
print(obj.twoSum([3,2,4],6))
print(obj.twoSum([3,3],6))
print(obj.twoSum([2,7,11,15],19))
