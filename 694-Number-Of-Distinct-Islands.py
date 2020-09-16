class Solution:
	def NODI(self, grid):
		if not grid:
			return 0
		rows = len(grid)
		cols = len(grid[0])
		
		def dfs(grid,x,y,baseX,baseY,shape):
			if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y]==0:
				return
			shape.add(str(x - baseX) + str(y - baseY))
			grid[x][y] = 0
			dfs(grid, x + 1, y, baseX, baseY, shape)
			dfs(grid, x - 1, y, baseX, baseY, shape)
			dfs(grid, x, y - 1, baseX, baseY, shape)
			dfs(grid, x, y + 1, baseX, baseY, shape)
			

		res = set()
		for i in range(rows):
			for j in range(cols):
				if grid[i][j]==1:
					shape = set()
					dfs(grid,i,j,i,j,shape)
					# print(shape)
					res.add(str(shape))
					
		return len(res)

obj = Solution()
print(obj.NODI([[1,1,0,0,0],
				[1,1,0,0,0],
				[0,0,1,1,0],
				[0,0,1,1,0],
				[0,0,0,0,0]]))

print(obj.NODI([[1,1,0,0,1],
				[1,1,0,0,0],
				[0,0,1,1,0],
				[0,0,1,1,0],
				[0,0,0,0,1]]))

print(obj.NODI([[1,0,0,0,0],
				[1,1,0,0,0],
				[0,0,1,0,0],
				[0,0,0,1,1],
				[0,0,0,0,1]]))