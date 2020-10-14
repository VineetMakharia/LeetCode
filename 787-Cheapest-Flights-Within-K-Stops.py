from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # Djikstra's algorithm
#         from collections import defaultdict
#         graph = defaultdict(list)
#         for source,dest,cost in flights:
#             graph[source].append((cost,dest))
        
#         heap = []
#         heap.append((0,src,K+1))
#         while heap:
#             current_cost,current_node,remaining_stops= heapq.heappop(heap)
#             if remaining_stops < 0: 
#                 continue
#             if current_node == dst: 
#                 return current_cost
#             for nc,nd in graph[current_node]: 
#                 heapq.heappush(heap,(nc+current_cost,nd,remaining_stops-1))
#         return -1
        
        # BFS
        from collections import defaultdict,deque
        graph = defaultdict(list)
        for source,dest,cost in flights:
            graph[source].append((cost,dest))
        queue = deque()
        queue.append((src,0,K+1))
        min_cost = float('inf')
        while queue:
            current_node,current_cost,remaining_stops = queue.popleft()
            if remaining_stops < 0:
                continue
            if current_node == dst:
                min_cost = min(min_cost,current_cost)
            for nc,nd in graph[current_node]:
                if current_cost + nc >= min_cost:
                    continue
                queue.append((nd,current_cost+nc,remaining_stops-1))
        
        return min_cost if min_cost!=float('inf') else -1
            
obj = Solution()
print(obj.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,1))
print(obj.findCheapestPrice(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0))