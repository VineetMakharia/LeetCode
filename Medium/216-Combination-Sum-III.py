class Solution:
    def combinationSum3(self, k, n):
        res = []
        nums = [i for i in range(1,10)]
        self.dfs(nums, k, n, [], res)
        return res
    
    def dfs(self, nums, k, n, path, res):
        if k < 0 or n < 0: 
            return 
        if k == 0 and n == 0: 
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], res)

obj = Solution()
print(obj.combinationSum3(3,7))
print(obj.combinationSum3(4,25))