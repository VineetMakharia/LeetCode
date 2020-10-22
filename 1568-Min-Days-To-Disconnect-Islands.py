class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

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
            return False
        if rx>ry:
            self.parent[py]=px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px]=py
            self.rank[py]+=self.rank[px]
        return True

class Solution:
    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        dsu = DSU(rows*cols)
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        initial_island_count=0
                    
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==1:
                    initial_island_count+=1
                    current = x*cols+y
                    for dx,dy in dirs:
                        nx = x + dx
                        ny = y + dy
                        nei = nx*cols + ny
                        if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                            if (dsu.union(current, nei)):
                                initial_island_count-=1
        return initial_island_count
    
    def minDays(self, grid):
        initial_island_count = self.numIslands(grid)
        # print(initial_island_count)
        if initial_island_count>1 or initial_island_count==0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    grid[i][j]=0
                    islands = self.numIslands(grid)
                    grid[i][j]=1
                    if islands>1 or islands==0:
                        return 1
        return 2

obj = Solution()
print(obj.minDays([[1,1,0,1,1],
               [1,1,1,1,1],
               [1,1,0,1,1],
               [1,1,0,1,1]]))
        
        