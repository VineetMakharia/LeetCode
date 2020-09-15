class Node():
	def __init__(self, val=0,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
        # if not root:
        #     return 0
        # from collections import deque
        # queue = deque()
        # queue.append([root, 1])
        # ans = 0
        # while queue:
        #     node, current_height = queue.popleft()
        #     if not node.left and not node.right:
        #         ans = max(ans, current_height)
        #         continue
        #     if node.left:
        #         queue.append([node.left, current_height+1])
        #     if node.right:
        #         queue.append([node.right, current_height+1])
        # return ans
        
#         self.ans = 0
#         def dfs(node,current_height):
#             if not node.left and not node.right:
#                 self.ans = max(self.ans,current_height)
#             if node.left:
#                 dfs(node.left, current_height+1)
#             if node.right:
#                 dfs(node.right,current_height+1)
#             return self.ans
        
#         return dfs(root,1)
# [3,9,20,null,null,15,7]
root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)


obj = Solution()
print(obj.maxDepth(root))