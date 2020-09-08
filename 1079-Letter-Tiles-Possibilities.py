class Solution:
    def numTilePossibilities(self, tiles):
        res = set()
        self.dfs(tiles,res,"")
        return len(res)
    
    def dfs(self,tiles,res,path):
        if path:
            res.add(path)
        for i in range(len(tiles)):
            self.dfs(tiles[:i]+tiles[i+1:],res,path+tiles[i])

obj = Solution()
print(obj.numTilePossibilities("AAB"))
print(obj.numTilePossibilities("AAABBC"))
print(obj.numTilePossibilities("V"))