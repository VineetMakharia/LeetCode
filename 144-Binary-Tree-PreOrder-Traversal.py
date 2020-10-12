class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        # Preorder is NLR
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        
#         preorder = []
#         stack = [root]
        
#         while stack:
#             curr = stack.pop()
#             preorder.append(curr.val)
#             if curr.right:
#                 stack.append(curr.right)
#             if curr.left:
#                 stack.append(curr.left)
#         return preorder

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

obj = Solution()
print(obj.preorderTraversal(root))