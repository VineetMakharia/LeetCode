class Solution:
    def minReorder(self, n, connections):
        from collections import defaultdict,deque
        
        undirected_graph = defaultdict(list)
        actual_graph = defaultdict(set)

        for a,b in connections:
            undirected_graph[a].append(b)
            undirected_graph[b].append(a)
            actual_graph[a].add(b) 
        # queue = [(1,0),(4,0)]
        # queue structure is (node, destination)
        queue = deque()
        for node in undirected_graph[0]:
            queue.append((node,0))
        # print(queue)
        res = 0
        visited = set([0])
        
        while queue:
            current, destination_node = queue.popleft()
            visited.add(current)
            if (destination_node not in actual_graph[current]):
                print(f"Add edge b/w {current} and {destination_node}")
                res += 1
            for nei in undirected_graph[current]:
                if nei not in visited:
                    queue.append((nei, current))
        return res

obj = Solution()
print(obj.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]]))