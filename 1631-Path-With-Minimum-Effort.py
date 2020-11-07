from typing import List
class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px==py:
            return
        if self.rank[px]>self.rank[py]:
            self.parent[py]=px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py] += self.rank[px]
            
            
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        edge_list = []
        
        def find_diff(x1,y1,x2,y2):
            return abs(heights[x1][y1]-heights[x2][y2])
        
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                current = i*cols+j
                for di,dj in dirs:
                    ni=i+di
                    nj=j+dj
                    if 0<=ni<rows and 0<=nj<cols:
                        nei = ni*cols+nj
                        edge_list.append((find_diff(i,j,ni,nj), current,nei))
        
        edge_list.sort()
        dsu = DSU(rows*cols)
        for diff,x,y in edge_list:
            dsu.union(x,y)
            if dsu.find(0)==dsu.find(rows*cols-1):
                return diff
        return 0

obj = Solution()
print(obj.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))