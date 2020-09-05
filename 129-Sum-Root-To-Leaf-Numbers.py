class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):
        from collections import deque
        if not root:
            return 0
        queue = deque()
        queue.append([root, root.val])
        result = 0
        while queue:
            node, value = queue.popleft()
            if node:
                if not node.left and not node.right:
                    result+=value
                if node.left:
                    queue.append([node.left, value*10+node.left.val])
                if node.right:
                    queue.append([node.right, value*10+node.right.val])
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
# 125 + 13

result = Solution()
print(result.sumNumbers(root))
