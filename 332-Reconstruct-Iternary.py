class Solution:
    def findItinerary(self, tickets):
        from collections import defaultdict
        graph = defaultdict(list)
        # Build a basic graph
        for from_,to in tickets:
            graph[from_].append(to)
        # Sort based on the destinations you can go to
        for key in graph:
            graph[key] = sorted(graph[key], reverse = True)
        print(graph)
        
        stack = ["JFK"]
        res = []
        while stack:
            print(stack)
            current = stack[-1]
            if graph[current]:
                stack.append(graph[current].pop())
            else:
                res.append(stack.pop())
                print("res:",res)
        return res [::-1]

obj = Solution()
print(obj.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))