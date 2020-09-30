from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Given DAG
        # Expand using BFS (?)
        from collections import deque
        queue = deque()
        # queue is of the form node, path
        queue.append((0,[]))
        res = []
        N = len(graph)
        while queue:
            current_node, current_path = queue.popleft()
            if current_node == N-1:
                res.append(current_path + [N-1])
            for nei in graph[current_node]:
                queue.append((nei, current_path+[current_node]))
        return res

obj = Solution()
print(obj.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))