class DSU:
	def __init__(self,n):
		self.parent = [i for i in range(n)]
		self.rank = [0 for i in range(n)]

	def find(self,x):
		if x!=self.parent[x]:
			self.parent[x]=self.find(self.parent[x])
		return self.parent[x]

	def union(self,x,y):
		xp = self.find(x)
		yp = self.find(y)
		if xp==yp:
			return False
		elif self.rank[xp]<self.rank[yp]:
			self.parent[xp]=yp
		elif self.rank[yp]<self.rank[xp]:
			self.parent[yp]=xp
		else:
			self.parent[yp]=xp
			self.rank[xp]+=1
		return True

class Solution:
	def ConnectedComponents(self,n,edges):
		dsu = DSU(n)
		count = n
		for e1,e2 in edges:
			if dsu.union(e1,e2):
				count-=1
		return count


obj = Solution()
print(obj.ConnectedComponents(5, [[0, 1], [1, 2], [2, 3],[3,4]]))
print(obj.ConnectedComponents(5, [[0, 1], [1, 2], [3, 4]]))

