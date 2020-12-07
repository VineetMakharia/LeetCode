class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findNearestRightNode(self, root: Node, u):
        if not root or not u:
            return None
        from collections import deque
        queue = deque()
        queue.append((root))
        
        while queue:
            sz = len(queue)
            temp = deque()
            for _ in range(sz):
                curr = queue.popleft()
                if curr.val == u:
                    return queue[0].val if queue else None
                if curr.left:
                    temp.append(curr.left)
                if curr.right:
                    temp.append(curr.right)
            queue = temp

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(6)

obj = Solution()
print(obj.findNearestRightNode(root,6))
print(obj.findNearestRightNode(root,2))