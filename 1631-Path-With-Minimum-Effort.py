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
        # Djikstra's Soln
        import heapq
        # Maintain a heap of type diff,x,y
        heap = [(0,0,0)]
        rows = len(heights)
        cols = len(heights[0])
        visited = set()
        res = -1
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        while heap:
            # Pop the smallest abs distance
            curr_diff,x,y = heapq.heappop(heap)
            res = max(res,curr_diff)
            if (x,y)==(rows-1,cols-1):
                return res
            visited.add((x,y))
            for dx,dy in dirs:
                nx = x+dx
                ny = y+dy
                if (0<=nx<rows and 0<=ny<cols and (nx,ny) not in visited):
                    hd = abs(heights[nx][ny]-heights[x][y])
                    heapq.heappush(heap, (hd,nx,ny))
        return res


        # rows = len(heights)
        # cols = len(heights[0])
        # edges = []
        
        # def find_diff(x1,y1,x2,y2):
        #     return abs(heights[x1][y1]-heights[x2][y2])
        
        # dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        # for i in range(rows):
        #     for j in range(cols):
        #         current = i*cols+j
        #         for di,dj in dirs:
        #             ni=i+di
        #             nj=j+dj
        #             if 0<=ni<rows and 0<=nj<cols:
        #                 nei = ni*cols+nj
        #                 edges.append((find_diff(i,j,ni,nj), current,nei))
        
        # edges.sort()
        # dsu = DSU(rows*cols)
        # for diff,x,y in edges:
        #     dsu.union(x,y)
        #     if dsu.find(0)==dsu.find(rows*cols-1):
        #         return diff
        # return 0

obj = Solution()
print(obj.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))