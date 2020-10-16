# Definition for a binary tree node.
from typing import List
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root) -> List[List[int]]:
        if not root:
            return []
        res = []
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(temp)
        return res[::-1]

root = Node(-10)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

obj = Solution()
print(obj.levelOrderBottom(root))