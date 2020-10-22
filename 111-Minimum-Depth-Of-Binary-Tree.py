class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        #classic BFS?
        if not root:
            return 0
        from collections import deque
        queue = deque()
        queue.append((root,1))
        while queue:
            sz = len(queue)
            for i in range(sz):
                current_node,depth = queue.popleft()
                if not current_node.left and not current_node.right:
                    return depth
                if current_node.left:
                    queue.append((current_node.left, depth+1))
                if current_node.right:
                    queue.append((current_node.right, depth+1))

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.minDepth(root))