class Solution:
    def combinations(self,n,k):
        res = []
        arr = [i+1 for i in range(n)]
        self.dfs(arr,k,res,[])
        return res

    def dfs(self,arr,k,res,current):
        if len(current)==k:
            res.append(current)
        for i in range(len(arr)):
            self.dfs(arr[i+1:], k, res, current+[arr[i]])


obj = Solution()
print(obj.combinations(4,2))