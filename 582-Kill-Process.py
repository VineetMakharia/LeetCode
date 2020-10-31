from typing import List
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        from collections import deque,defaultdict
        graph = defaultdict(list)
        for parent,child in zip(ppid,pid):
            graph[parent].append(child)
        queue = deque()
        queue.append((kill))
        res = [kill]
        while queue:
            current = queue.popleft()
            for children in graph[current]:
                res.append(children)
                queue.append((children))
        return res

obj = Solution()
print(obj.killProcess([1, 3, 10, 5],[3, 0, 5, 3], 5))