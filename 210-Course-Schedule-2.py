class Solution:
    def findOrder(self, numCourses, prerequisites):
        from collections import defaultdict,deque
        hash_map = defaultdict(list)
        indegree = [0]*numCourses
        
        for course,pre in prerequisites:
            hash_map[pre].append(course)
            indegree[course]+=1
        
        ans = []
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nei in hash_map[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        return ans if len(ans)==numCourses else []

obj = Solution()
print(obj.findOrder(2,[[1,0]]))
print(obj.findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))