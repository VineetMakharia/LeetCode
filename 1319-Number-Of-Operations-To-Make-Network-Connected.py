class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [-1 for i in range(n)]
        self.count = n-1
        
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
            # If parent aren't same, then I need to connect x,y 
            # so number of connections decrease
            self.count-=1
            if rx>ry:
                self.parent[py]=px
            elif ry>rx:
                self.parent[px]=py
            else:
                self.parent[py]=px
                self.rank[x]+=1 
        
class Solution:
    def makeConnected(self, n, connections):
        current_connections = len(connections)
        if current_connections<(n-1):
            return -1
        dsu = DSU(n)
        for x,y in connections:
            dsu.union(x,y)
        return dsu.count

obj = Solution()
print(obj.makeConnected(4,[[0,1],[0,2],[1,2]]))
print(obj.makeConnected(6,[[0,1],[0,2],[0,3],[1,2],[1,3]]))
print(obj.makeConnected(6,[[0,1],[0,2],[0,3],[1,2]]))
print(obj.makeConnected(5,[[0,1],[0,2],[3,4],[2,3]]))

