class Node:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root):
        from collections import deque
        queue = deque()
        queue.append((root))
        res = -1
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == 0:
                    res = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
                
root = Node(1)
root.left = Node(2)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(4)

obj = Solution()
print(obj.findBottomLeftValue(root))