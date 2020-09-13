class Solution:
    def networkDelayTime(self, times, N, K):
        from collections import defaultdict
        from heapq import heappush, heappop
        graph = defaultdict(list)
        visited = dict()
        queue = [(0,K)]
        for u, v, w in times:
            graph[u].append([v, w])
        while queue:
            time, node = heappop(queue)
            if node not in visited:
                visited[node] = time
                for v, w in graph[node]:
                    heappush(queue, (time + w, v))
        return max(visited.values()) if len(visited) == N else -1

obj = Solution()
print(obj.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2))
print(obj.networkDelayTime([[1,2,1]],2,2))
