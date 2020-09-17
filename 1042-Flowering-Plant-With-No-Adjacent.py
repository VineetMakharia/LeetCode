class Solution:
    def gardenNoAdj(self, N, paths):
        from collections import defaultdict
        if N==1:
            return [1]
        res = [1 for i in range(N)]
        graph = defaultdict(list)
        for e1,e2 in paths:
            graph[e1-1].append(e2-1)
            graph[e2-1].append(e1-1)
        
        for garden in graph:
            nei_colors = set()
            for nei in graph[garden]:
                nei_colors.add(res[nei])
            for clr in range(1,5):
                if clr not in nei_colors:
                    res[garden] = clr
                    break
        return res
            
            
obj = Solution()
print(obj.gardenNoAdj(3,[[1,2],[2,3],[3,1]]))