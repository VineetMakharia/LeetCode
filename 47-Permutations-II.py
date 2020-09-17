class Solution:
    def permuteUnique(self, nums):
        res = []
        nums.sort()
        self.dfs(nums,res,[])
        return res
    
    def dfs(self,nums,res,path):
        if len(nums) == 0:
            res.append(path)
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                self.dfs(nums[:i] + nums[i+1:],res,path+[nums[i]])

obj = Solution()
print(obj.permuteUnique([1,1,2]))