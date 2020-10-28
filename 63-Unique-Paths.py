from typing import List
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # 1st base case would be if the grid does not exist
        if not grid:
            return 0
        # If source is obs or destination is obstacle then no ways possible
        if grid[0][0]!=0 or grid[-1][-1]!=0:
            return 0
        
        seen = {}
        dst = (len(grid)-1, len(grid[0])-1)
        return self.dfs(grid, 0, 0, dst, seen)

    def dfs(self, grid, i, j, dst, seen):
        # Boundary check and checking if the current point I am at is an obstacle
        if i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] == 1:
            seen[(i,j)] = 0
            return 0
        # If I reach the destination, that means there is a path
        if (i,j) == dst:
            return 1
        if (i,j) in seen:
            return seen[(i,j)]
        # Find the total number of paths going right and down
        total = self.dfs(grid, i+1, j, dst, seen) + self.dfs(grid, i, j+1, dst, seen) 
        seen[(i,j)] = total
        return total

obj = Solution()
print(obj.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))