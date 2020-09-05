class Node:
    def __init__(self, val=0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Node, sum: int) -> bool:
        
        # Base Case:
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

        # if not root:
        #   return None
        # if not root and sum==0:
        #   return True
        # from collections import deque
        # queue = deque()
        # queue.append([root, sum-root.val])

        # while queue:
        #   node, remaining_sum = queue.popleft()
        #   if not node.left and not node.right and remaining_sum == 0:
        #       return True
        #   if node.left:
        #       queue.append([node.left, remaining_sum - node.left.val])
        #   if node.right:
        #       queue.append([node.right, remaining_sum  - node.right.val])
        # return False

root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)

obj = Solution()
print(obj.hasPathSum(root,21))
print(obj.hasPathSum(root,22))