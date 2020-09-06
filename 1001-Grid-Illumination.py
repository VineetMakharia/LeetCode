class Solution:
	def GridIllumination(self, N, lamps, queries):
		from collections import defaultdict
		rows = defaultdict(int)
		cols = defaultdict(int)
		diag = defaultdict(int)
		anti = defaultdict(int)
		lamps_on = set()

		for x,y in lamps:
			lamps_on.add((x,y))
			rows[x]+=1
			cols[y]+=1
			diag[x+y]+=1
			anti[x-y]+=1

		res = []
		dirs = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

		for x,y in queries:
			res.append(1 if rows[x] or cols[x] or diag[x+y] or anti[x-y] else 0)

			for dx,dy in dirs:
				nx = x + dx
				ny = y + dy

				if (nx,ny) in lamps_on:
					lamps_on.remove((nx,ny))
					rows[nx]-=1
					cols[ny]-=1
					diag[nx+ny]-=1
					anti[nx-ny]+=1
		return res

obj = Solution()
print(obj.GridIllumination(5,[[0,0],[4,4]],[[1,1],[1,0]]))
print(obj.GridIllumination(5,[[0,0],[4,4]],[[1,1],[1,1]]))
print(obj.GridIllumination(5,[[0,0],[0,4]],[[0,4],[0,1],[1,4]])) 