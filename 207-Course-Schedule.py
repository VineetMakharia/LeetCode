class Solution:
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict, deque
        # Build a directed graph
        graph = defaultdict(list)
        indegree = [0 for i in range(numCourses)]
        for from_,to in prerequisites:
            graph[from_].append(to)
            indegree[to]+=1
        
        # Topological sorting 
        # Starting node could be any node with indegree = 0
        # I am guaranteed to have a node with indegree 0 else there would be a cycle
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        number_of_courses_seen = 0
        while queue:
            node = queue.popleft()
            number_of_courses_seen +=1
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        return number_of_courses_seen == numCourses

obj = Solution()
print(obj.canFinish(2,[[1,0]]))
print(obj.canFinish(2,[[1,0],[0,1]]))