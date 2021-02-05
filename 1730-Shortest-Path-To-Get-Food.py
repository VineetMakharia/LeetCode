from typing import List
from collections import deque
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        # First task is to find my location
        rows = len(grid)
        cols = len(grid[0])
        x = -1
        y = -1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "*":
                    x = i
                    y = j
                    break
        
        # Start a BFS from the current location
        
        queue = deque()
        queue.append((x,y,0))
        
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        visited.add((x,y))
        
        while queue:
            curr_x, curr_y, curr_length = queue.popleft()
            if grid[curr_x][curr_y] == "#":
                return curr_length
            for dx,dy in dirs:
                nx = curr_x + dx
                ny = curr_y + dy
                if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]!="X" and (nx,ny) not in visited:
                    queue.append((nx,ny,curr_length+1))
                    visited.add((nx,ny))
        return -1

obj = Solution()
grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
print(obj.getFood(grid))