from typing import List
# Generic DSU template
class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        
    def find(self,x):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px = self.find(x)
        py = self.find(y)
        if px==py:
            return
        if self.rank[px]>=self.rank[py]:
            self.parent[py] = px
            self.rank[px]+=self.rank[py]
        else:
            self.parent[px] = py
            self.rank[py]+=self.rank[px]
        
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        dsu = DSU(n+1)
        # The hardest part of this question is how to build the graph
        # Starting at i=threshold+1 enusres that we are not choosing any divisors lesser than the threshold
        # And for every divisor we will only unionize starting from it's double since if j starts from i, our call would be union(i,i) which is redundant since everyone is their own parent anyway 
        # And every step would be incremented by i itself
        # Alternative : 
        # for i in range(threshold+1, n+1):
        #     m = 1
        #     while i*m<=n:
        #         # print(f'Unionizing {i} and {i*m}')
        #         dsu.union(i, i*m)
        #         m+=1
        
        for i in range(threshold+1, n+1):
            for j in range(i*2, n+1,i):
                dsu.union(i,j)
        
        return [dsu.find(x)==dsu.find(y) for x,y in queries]
        
        
test_cases = [[6,2,[[1,4],[2,5],[3,6]]], [6,0,[[1,4],[2,5],[3,6]]], [5,1,[[4,5],[4,5],[3,2],[2,3],[3,4]]]]
obj = Solution()
for tc in test_cases:
    print(obj.areConnected(*tc))