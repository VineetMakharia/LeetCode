class Node():
	def __init__(self, val=0, left=None,right=None):
		self.val = val
		self.right = right
		self.left = left

class Solution():
	def isSymmetric(self, root):
		# Base cases - If there is no node or if there is only a single node
		if not root or (not root.left and not root.right):
			return True
		
#         def helper(node1, node2):
#             if node1==None and node2==None:
#                 return True
#             if node1==None or node2==None:
#                 return False
#             return (node1.val == node2.val and helper(node1.left, node2.right) and helper(node1.right, node2.left))
		
#         return helper(root.left,root.right)
		from collections import deque
		queue = deque()
		queue.append((root.left))
		queue.append((root.right))
		while queue:
			node1 = queue.popleft()
			node2 = queue.popleft()
			if not node1 and not node2:
				continue
			if not node1 or not node2:
				return False
			if node1.val!=node2.val:
				return False
			queue.append(node1.left)
			queue.append(node2.right)
			queue.append(node1.right)
			queue.append(node2.left)
			
		return True


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(2)
root1.left.left = Node(3)
root1.left.right = Node(4)
root1.right.left = Node(4)


obj = Solution()
print(obj.isSymmetric(root))
print(obj.isSymmetric(root1))