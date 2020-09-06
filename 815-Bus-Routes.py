class Solution:
    def numBusesToDestination(self, routes, S, T):
        if S == T:
            return 0
        
        from collections import defaultdict,deque
        hash_map = defaultdict(set)
        for bus_no, stops in enumerate(routes):
            for stop in stops:
                hash_map[stop].add(bus_no)
        
        queue = deque()
        queue.append((S,0))
        
        seen_stops = set()
        seen_buses=set()
        
        while queue:
            current_stop, buses_taken = queue.popleft()
            if current_stop == T:
                return buses_taken
            for bus in hash_map[current_stop]:
                if bus not in seen_buses:
                    seen_buses.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop not in seen_stops:
                            seen_stops.add(next_stop)
                            queue.append((next_stop,buses_taken+1))
                            
        return -1

obj = Solution()
print(obj.numBusesToDestination([[1, 2, 7], [3, 6, 7]],1,6))
print(obj.numBusesToDestination([[1, 2, 7], [3, 6, 7]],1,1))
print(obj.numBusesToDestination([[1, 2, 7], [3, 6, 7]],1,7))
                    