class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [-1 for i in range(n)]
        self.count = n
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        rx = self.rank[x]
        ry = self.rank[y]
        if px!=py:
            self.count-=1
            if rx>ry:
                self.parent[py]=px
            elif ry>rx:
                self.parent[px]=py
            else:
                self.parent[py]=px
                self.rank[x]+=1    
        
class Solution:
    def findCircleNum(self, M):
        n = len(M)
        dsu = DSU(n)
        for i in range(n):
            for j in range(i+1,n):
                if M[i][j]==1:
                    dsu.union(i,j)
        return dsu.count
        
        
#         N = len(M)
#         count=0
#         visited = [False]*N
        
#         def dfs(i):
#             for j in range(N):
#                 if not visited[j] and M[i][j]==1:
#                     visited[j]=True
#                     dfs(j)
        
#         for i in range(N):
#             if not visited[i]:
#                 visited[i]=True
#                 count+=1
#                 dfs(i)
#         return count

obj = Solution()
print(obj.findCircleNum([[1,1,0],
                         [1,1,0],
                         [0,0,1]]))
print(obj.findCircleNum([[1,1,0],
                         [1,1,1],
                         [0,0,1]]))
print(obj.findCircleNum([[1,0,0],
                         [0,1,0],
                         [0,0,1]]))
