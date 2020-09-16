class Solution():
    def orangesRotting(self, grid):
        from collections import deque
        positions = deque()
        rows = len(grid)
        cols = len(grid[0])
        freshOranges = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    freshOranges+=1
                if grid[i][j]==2:
                    positions.append([i,j])
        if freshOranges==0:
            return 0
        time = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while positions and freshOranges>0:
            time+=1
            for _ in range(len(positions)):
                x,y = positions.popleft()
                for dx,dy in directions:
                    nx = x+dx
                    ny = y+dy
                    if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        freshOranges-=1
                        positions.append([nx,ny])
        return time if freshOranges==0 else -1

res = Solution()

print(res.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(res.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(res.orangesRotting([[0,2]]))

