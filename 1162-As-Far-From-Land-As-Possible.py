class Solution:
    def maxDistance(self, grid):
        # Find all the land
        from collections import deque
        rows = len(grid)
        cols = len(grid[0])
        land_found = False
        water_found = False
        positions = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    positions.append((i,j,0))
                    land_found = True
                if grid[i][j]==0:
                    water_found = True
        if not land_found or not water_found:
            return -1
        dirs = [(1,0),(0,1),(0,-1),(-1,0)]
        max_ = -1
        while positions:
            for _ in range(len(positions)):
                x,y,nearest = positions.popleft()
                max_=max(max_,nearest)
                for dx,dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==0:
                        grid[nx][ny] = nearest+1
                        positions.append((nx,ny,nearest+1))         
        return max_

obj = Solution()
print(obj.maxDistance([[1,0,0],[0,0,0],[0,0,0]]))