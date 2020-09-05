class Solution:
	def subsets(self,arr):
		res = []
		self.dfs(arr,res,[])
		return res

	def dfs(self,arr,res,path):
		res.append(path)
		for i in range(len(arr)):
			self.dfs(arr[:i]+arr[i+1:],res,path+[arr[i]])

obj = Solution()
print(obj.subsets([1]))