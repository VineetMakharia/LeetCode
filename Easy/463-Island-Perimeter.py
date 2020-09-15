class Solution:
    def islandPerimeter(self, grid):
        if not grid:
            return 0            
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==1:
                    for dx,dy in dirs:
                        nx = x + dx
                        ny = y + dy
                        if nx == -1 or nx == rows or ny == -1 or ny == cols or grid[nx][ny]==0:
                            perimeter+=1
        return perimeter


obj = Solution()
print(obj.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))