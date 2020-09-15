class Solution:
    def containsCycle(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        def dfs(x,y,parent):
            dirs = [(1,0),(0,1),(-1,0),(0,-1)]
            if (x,y) in visited:
                return True
            visited.add((x,y))
            for dx,dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==grid[x][y] and (nx,ny)!=parent:
                    if dfs(nx,ny,(x,y)):
                        return True
                    
        for i in range(rows):
            for j in range(cols):
                if (i,j) in visited:
                    continue
                if dfs(i,j,None):
                    return True
        return False

obj = Solution()
grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
grid1 = [["a","b","c"],["a","b","c"]]
print(obj.containsCycle(grid))
print(obj.containsCycle(grid1))
