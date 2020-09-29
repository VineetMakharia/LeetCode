class Solution:
    def regionsBySlashes(self, grid):
        # build a new grid of original size*3 full of 0's
        rows = len(grid)
        cols = len(grid[0])
        grid1 = [[0 for i in range(cols*3)] for j in range(rows*3)]
        for i in range(rows):
            for j in range(cols):
                ni = i*3
                nj = j*3
                if grid[i][j]=="\\":
                    grid1[ni][nj] = 1
                    grid1[ni+1][nj+1] = 1
                    grid1[ni+2][nj+2] = 1
                if grid[i][j] == "/":
                    grid1[ni][nj+2] = 1
                    grid1[ni+1][nj+1] = 1
                    grid1[ni+2][nj] = 1
        
        # Upscaled grid is built
        new_rows = len(grid1)
        new_cols = len(grid1[0])
        count = 0
        for i in range(new_rows):
            for j in range(new_cols):
                if grid1[i][j] == 0:
                    self.dfs(i,j,grid1)
                    count+=1
        return count
                
    def dfs(self,x,y,grid):
        if x<0 or x>=len(grid) or y<0 or y>=len(grid[0]) or grid[x][y]==1:
            return
        grid[x][y] = 1
        self.dfs(x+1,y,grid)
        self.dfs(x-1,y,grid)
        self.dfs(x,y+1,grid)
        self.dfs(x,y-1,grid)
        
obj = Solution()
print(obj.regionsBySlashes([
  "/\\",
  "\\/"
]))
print(obj.regionsBySlashes([
  "//",
  "/ "
]
))
        
        
        
        
        
                