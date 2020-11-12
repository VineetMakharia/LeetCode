class Solution:
    def permuteUnique(self, nums):
        from collections import Counter
        res = []
        self.dfs(nums,Counter(nums),res,[])
        return res

    def dfs(self,nums,count,res,path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for x in count:
            if count[x]>0:
                count[x]-=1
                path.append(x)
                self.dfs(nums,count,res,path)
                path.pop()
                count[x]+=1


    # Ineffcient approach because slicing takes O(n) time
    #     res = []
    #     nums.sort()
    #     self.dfs(nums,res,[])
    #     return res
    
    # def dfs(self,nums,res,path):
    #     if len(nums) == 0:
    #         res.append(path)
    #     for i in range(len(nums)):
    #         if i==0 or nums[i]!=nums[i-1]:
    #             self.dfs(nums[:i] + nums[i+1:],res,path+[nums[i]])

obj = Solution()
print(obj.permuteUnique([1,1,2]))