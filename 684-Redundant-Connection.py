class DSU:
	def __init__(self,n):
		self.parent = [i for i in range(n)]
		self.rank = [-1 for i in range(n)]

	def find(self,x):
		if x!=self.parent[x]:
			self.parent[x]=self.find(self.parent[x])
		return self.parent[x]

	def union(self,x,y):
		px = self.find(x)
		py = self.find(y)
		rx = self.rank[x]
		ry = self.rank[y]
		if px==py:
			return True
		if rx>ry:
			self.parent[py]=px
		elif ry>rx:
			self.parent[px]=py
		else:
			self.parent[py]=px
			self.rank[px]+=1


class Solution:
	def redundant(self,edges):
		dsu = DSU(len(edges))
		for e1,e2 in edges:
			if dsu.union(e1-1,e2-1):
				return [e1,e2]

obj = Solution()
print(obj.redundant([[1,2], [1,3], [2,3]]))
print(obj.redundant([[1,2], [2,3], [3,4], [1,4], [1,5]]))