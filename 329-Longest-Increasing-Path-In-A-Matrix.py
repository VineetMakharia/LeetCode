from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Base Case
        if not matrix:
            return 0
        self.ans = 0
        self.hash_map = dict()
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Start a DFS from every point and compute a new increasing path
        # Maintain a track of the previous value that we are coming from
        for i in range(rows):
            for j in range(cols):
                self.dfs(i,j,matrix,float('-inf'))
        return self.ans
    
    def dfs(self,x,y,matrix,prev):
        if x<0 or x>=len(matrix) or y<0 or y>=len(matrix[0]) or prev>=matrix[x][y]:
            return 0
        # Recursive with memo 
        if (x,y) in self.hash_map:
            return self.hash_map[(x,y)]
        # recursively find the longest path from this position
        # You can only choose 1 path so it will be max from 4 directions
        total = 1 + max(self.dfs(x+1,y,matrix,matrix[x][y]),
                    self.dfs(x,y+1,matrix,matrix[x][y]),
                    self.dfs(x-1,y,matrix,matrix[x][y]),
                    self.dfs(x,y-1,matrix,matrix[x][y]))
        self.ans = max(self.ans,total)
        # Store the already computed so that you don't need to recompute everytime
        self.hash_map[(x,y)] = total
        return total

obj = Solution()
print(obj.longestIncreasingPath([
  [9,9,4],
  [6,6,8],
  [2,1,1]
] ))