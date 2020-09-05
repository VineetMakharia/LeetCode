class Solution:
	def permutations(self,arr):
		res = []
		self.dfs(arr,len(arr),[],res)
		return res


	def dfs(self, arr, req_size, current, res):
		if len(current)==req_size:
			res.append(current)
			return
		for i in range(len(arr)):
			self.dfs(arr[:i]+arr[i+1:], req_size, current+[arr[i]], res)


obj = Solution()
print(obj.permutations([1,2,3]))