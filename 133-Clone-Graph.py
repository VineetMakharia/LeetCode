# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
#         self.neighbors = neighbors if neighbors is not None else []
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Base Case - If graph is empty then return
        if not node:
            return
        # Need a data structure to store the results
        hash_map = dict()
        # Create a new node with the starting nodes value
        node_copy = Node(node.val)
        # Store the new node in the hash_map
        hash_map[node] = node_copy
        # Basic BFS traversal from the starting node
        queue = deque()
        queue.append((node))
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                for nei in curr.neighbors:
                    # ensuring that we don't gp back to the edge since undirected graph
                    if nei not in hash_map:
                        queue.append((nei))
                        # We found a new node not in our hash_map
                        hash_map[nei] = Node(nei.val)
                    # Add the corresponding nei to the neighbours array of the node we came from
                    hash_map[curr].neighbors.append(hash_map[nei])
        return hash_map[node]
