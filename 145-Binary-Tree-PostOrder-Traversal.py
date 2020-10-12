class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Node):
        # Post order is RLN
        if not root:
            return []
        return self.postorderTraversal(root.left) + \
            self.postorderTraversal(root.right) + [root.val]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

obj = Solution()
print(obj.postorderTraversal(root))