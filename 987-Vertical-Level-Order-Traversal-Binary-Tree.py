from typing import List
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Node) -> List[List[int]]:
        if not root:
            return []
        from collections import defaultdict,deque
        hash_map = defaultdict(list)
        queue = deque()
        queue.append((root,0,0))
        
        while queue:
            node, hd, vd = queue.popleft()
            hash_map[hd].append((vd,node.val))
            if node.left:
                queue.append((node.left,hd-1,vd+1))
            if node.right:
                queue.append((node.right,hd+1,vd+1))
        # print(hash_map)
        res = []
        for key in sorted(hash_map):
            temp = []
            for x in sorted(hash_map[key]):
                temp.append(x[1])
            res.append(temp)
        return res

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)


obj = Solution()
print(obj.verticalTraversal(root))