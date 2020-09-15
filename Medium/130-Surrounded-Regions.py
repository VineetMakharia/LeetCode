class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)] #25
        self.rank = [0 for i in range(n+1)] #25
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        xp = self.find(x)
        yp = self.find(y)
        if xp==yp:
            return
        elif self.rank[xp]<self.rank[yp]:
            self.parent[xp]=yp
        elif self.rank[yp]<self.rank[xp]:
            self.parent[yp]=xp
        else:
            self.parent[yp]=xp
            self.rank[xp]+=1
            
class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        rows = len(board) #4
        cols = len(board[0]) #6
        dummy = rows*cols #24
        obj = DSU(dummy)
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for x in range(rows):
            for y in range(cols):
                if board[x][y]=="O":
                    current = x*cols+y
                    if x==0 or x==rows-1 or y==0 or y==cols-1:
                        obj.union(current,dummy)
                        continue
                    for dx,dy in dirs:
                        nx = x + dx
                        ny = y + dy
                        if nx>=0 and nx<rows and ny>=0 and ny<cols and board[nx][ny]=="O":
                            newcurrent = nx*cols+ny
                            obj.union(newcurrent,current)
        
        for x in range(rows):
            for y in range(cols):
                if board[x][y]=="O" and (obj.find(x*cols+y)!=obj.find(dummy)):
                    board[x][y]="X"
        return board
                
#         if not board:
#             return board
#         def dfs(x,y,board):
#             if x<0 or x>=len(board) or y<0 or y>=len(board[0]) or board[x][y]!="O":
#                 return
#             board[x][y]="#"
#             dfs(x+1,y,board)
#             dfs(x,y+1,board)
#             dfs(x-1,y,board)
#             dfs(x,y-1,board)
            
#         rows = len(board)
#         cols = len(board[0])
#         for i in range(rows):
#             for j in range(cols):
#                 if board[i][j]=="O" and (i==0 or i==rows-1 or j==0 or j==cols-1):
#                     dfs(i,j,board)
                    
#         for i in range(rows):
#             for j in range(cols):
#                 if board[i][j]=="O":
#                     board[i][j]="X"
#                 elif board[i][j]=="#":
#                     board[i][j]="O"
#         return board
                
obj = Solution()
grid = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(obj.solve(grid))
