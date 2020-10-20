from typing import List

class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        self.count = n

    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)

        if px==py:
            return False
        
        self.count-=1
        if self.rank[px]>self.rank[py]:
            self.parent[py] = px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py]+=self.rank[px]
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dsu = DSU(n)
        for x,y in edges:
            if not dsu.union(x,y):
                return False
        return (dsu.count==1)


obj = Solution()
print(obj.validTree(5,[[0,1],[0,2],[0,3],[1,4]]))
print(obj.validTree(5,[[0,1], [1,2], [2,3], [1,3], [1,4]]))