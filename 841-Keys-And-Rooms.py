from typing import List
class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.count=n
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px==py:
            return
        self.count-=1
        if self.rank[px]>self.rank[py]:
            self.parent[py] = px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px]=py
            self.rank[py]+=self.rank[px]
            
            
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 1st idea is that if all nodes have an indegree > 0 then they can be reached
        # Won't work because 1-->2-->3 and 4-->5
                           # ^-------|     ^---|
        # In the above case, all nodes have indegree>0 
        
        # 2nd idea is to use a disjoint set
#         N = len(rooms)
#         dsu = DSU(N)
#         indegree = [0 for i in range(N)]
#         for i in range(N):
#             for connection in rooms[i]:
#                 dsu.union(i,connection)
#                 indegree[connection]+=1
        
#         for i in range(1,N):
#             if indegree[i]==0:
#                 return False
#         return dsu.count==1
    
        # 3rd and easiest solution is to just to a DFS
        N = len(rooms)
        visited = [False for i in range(N)]
        
        def dfs(node):
            if not visited[node]:
                visited[node]=True
                for nei in rooms[node]:
                    dfs(nei)
        dfs(0)
        return all(visited)
        
obj = Solution()
tc = [[[1],[2],[3],[]],[[1,3],[3,0,1],[2],[0]]]
for t in tc:
    print(obj.canVisitAllRooms(t))
        
        
        
        
        
        
        
        
        
        
        
        