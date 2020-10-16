from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Basic idea is to build a directed graph.
        from collections import defaultdict, deque
        graph = defaultdict(list)
        for i in range(len(equations)):
            x = equations[i][0]
            y = equations[i][1]
            val = values[i]
            graph[x].append((y,val))
            graph[y].append((x,1/val))
        # print(graph)
        
        def find_val(src,dst):
            # base case, if either the src or the dst don't exist, then can't /
            # find the product
            if src not in graph or dst not in graph:
                return -1.0
            # Start doing BFS from this node, if a path exists then it will return /
            # that the value and if we don't find anything then -1
            q = deque([(src, 1.0)])
            visited = set()
            while q:
                current_node, cur_product = q.popleft()
                if current_node == dst:
                    return cur_product
                visited.add(current_node)
                for neighbor, value in graph[current_node]:
                    if neighbor not in visited:
                        q.append((neighbor, cur_product*value))
            return -1.0
        return [find_val(x,y) for x,y in queries]

obj = Solution()
print(obj.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))