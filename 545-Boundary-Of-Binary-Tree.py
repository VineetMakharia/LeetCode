# Boundary of a binary tree
class Node:
	def __init__(self,val=0,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def BoundaryOfBT(self,root):
		ans = []
		# Base Cases
		if not root:
			return []
		if not root.left and not root.right:
			return [root.val]
		#Store all left side nodes
		temp = root.left
		left_nodes = []
		while temp.left:
			left_nodes.append(temp.val)
			temp = temp.left
		# left_nodes = left_nodes[1:]
		# Find all the leaf nodes
		from collections import deque
		queue = deque()
		queue.append((root))
		leaves = []
		while queue:
			node = queue.popleft()
			if not node.left and not node.right:
				leaves.append(node.val)
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		# Find all the right nodes
		temp = root.right
		right_nodes = []
		while temp.right:
			right_nodes.append(temp.val)
			temp = temp.right
		# right_nodes = right_nodes[:-1]
		ans.append(root.val)
		ans += left_nodes + leaves + right_nodes
		return ans


obj = Solution()
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

root = Node(20)
root.left = Node(8) 
root.right = Node(22)    
root.left.left = Node(4) 
root.left.right = Node(12) 
root.right.left = Node(10) 
root.right.right = Node(25) 
print(obj.BoundaryOfBT(root))