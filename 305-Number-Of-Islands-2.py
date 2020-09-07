class DSU:
	def __init__(self,n):
		self.parent = [i for i in range(n)]
		self.rank = [-1 for i in range(n)]
		self.count = 0
		self.isLand = [False for i in range(n)]

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
			return
		if rx>ry:
			self.parent[py]=px
		elif ry>rx:
			self.parent[px]=py
		else:
			self.parent[py]=px
			self.rank[px]+=1
		self.count-=1

	def addLand(self,x):
		self.isLand[x] = True
		self.count +=1


class Solution:
	def NOI2(self, rows, cols, positions):
		dsu = DSU(rows*cols)
		res = []
		dirs = [(1,0),(0,1),(-1,0),(0,-1)]
		for x,y in positions:
			current = x*cols + y
			dsu.addLand(current)
			for dx,dy in dirs:
				nx = x + dx
				ny = y + dy
				nei = nx*cols + ny
				if 0<=nx<rows and 0<=ny<cols and dsu.isLand[nei]:
					dsu.union(current,nei)
			res.append(dsu.count)

		return res

obj = Solution()
print(obj.NOI2(5,5,[[0,0],[1,1],[1,0],[3,3],[4,4],[3,4]]))