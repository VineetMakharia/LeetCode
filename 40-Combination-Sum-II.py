from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        self.dfs(candidates,res,target,[])
        return list(res)
    
    def dfs(self,candidates,res,target,path):
        if target < 0:
            return
        if target == 0:
            res.add(tuple(path))
        for i in range(len(candidates)):
            self.dfs(candidates[i+1:],res,target - candidates[i], path + [candidates[i]])

obj = Solution()
print(obj.combinationSum2([10,1,2,7,6,1,5],8))