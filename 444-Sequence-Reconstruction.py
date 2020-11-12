from typing import List
import collections
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # Need to find all the unique values in the original sequence
        values = {x for seq in seqs for x in seq}
        graph = collections.defaultdict(list)
        indegrees = {x: 0 for x in values}
        for seq in seqs:
            for i in range(len(seq) - 1):
                s = seq[i]
                t = seq[i+1]
                graph[s].append(t)
                indegrees[t] += 1
        queue = collections.deque([node for node,val in indegrees.items() if val==0])
        res = []
        # Do topological sorting 
        # If at any point there are 2 or more nodes that we can start from, that means \
        # there are 2 choices, and we can't determine which one to start from
        while queue:
            if len(queue) != 1:
                return False
            source = queue.popleft()
            res.append(source)
            for target in graph[source]:
                indegrees[target] -= 1
                if indegrees[target] == 0:
                    queue.append(target)
        return len(res) == len(values) and res == org

obj = Solution()

print(obj.sequenceReconstruction([1,2,3],[[1,2],[1,3]]))
print(obj.sequenceReconstruction([1,2,3],[[1,2],[1,3],[2,3]]))