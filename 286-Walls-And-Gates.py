class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # first task is to find all the gates 
        from collections import deque
        rows = len(rooms)
        cols = len(rooms[0])
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j]==0:
                    queue.append((i,j))
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        while queue:
            x,y = queue.popleft()
            for dx,dy in dirs:
                nx = x + dx
                ny = y + dy
                if 0<=nx<rows and 0<=ny<cols and rooms[nx][ny]==2147483647:
                    rooms[nx][ny] = rooms[x][y]+1
                    queue.append((nx,ny))
        return rooms
    
obj = Solution()
print(obj.wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
))