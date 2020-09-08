class Solution:
	def generate(self,n):
		res = []
		stack = [("",0,0)]
		while stack:
			path,left,right = stack.pop()
			if len(path)==2*n:
				res.append(path)
			if left<n:
				stack.append((path+"(",left+1,right))
			if right<left:
				stack.append((path+")", left,right+1))
		return res
	# 	res = []
	# 	self.dfs(res,0,0,"",n)
	# 	return res

	# def dfs(self,res,left,right,path,n):
	# 	if len(path)==2*n:
	# 		res.append(path)
	# 		return
	# 	if left<n:
	# 		self.dfs(res,left+1,right,path+"(",n)
	# 	if right<left:
	# 		self.dfs(res,left,right+1,path+")",n)

obj = Solution()
res = obj.generate(3)
print(len(res),":",res)