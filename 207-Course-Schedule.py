class Solution:
    def canFinish(self, n, prerequisites):
        from collections import defaultdict, deque
        # Build a directed graph
        graph = defaultdict(list)
        indegree = [0 for i in range(n)]
        for from_,to in prerequisites:
            graph[from_].append(to)
            indegree[to]+=1
        
        # Topological sorting 
        # Starting node could be any node with indegree = 0
        # I am guaranteed to have a node with indegree 0 else there would be a cycle
        remaining = n
        start_courses = deque([idx for idx,x in enumerate(indegree) if x==0])
        
        while start_courses:
            sz = len(start_courses)
            remaining-=sz
            for _ in range(sz):
                current_node = start_courses.popleft()
                for nei in graph[current_node]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        start_courses.append(nei)        
        return (remaining==0)

obj = Solution()
print(obj.canFinish(2,[[1,0]]))
print(obj.canFinish(2,[[1,0],[0,1]]))