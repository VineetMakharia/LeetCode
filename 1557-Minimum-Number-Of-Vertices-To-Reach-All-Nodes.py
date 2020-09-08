class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        indegree = [0 for _ in range(n)]
        for _,to in edges:
            indegree[to]+=1
        res = [idx for idx,x in enumerate(indegree) if x==0]
        return res

obj = Solution()
print(obj.findSmallestSetOfVertices(6,[[0,1],[0,2],[2,5],[3,4],[4,2]]))
print(obj.findSmallestSetOfVertices(5,[[0,1],[2,1],[3,1],[1,4],[2,4]]))
