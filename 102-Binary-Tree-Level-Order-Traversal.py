# Binary Tree Level Order Traversal

class Node:
	def __init__(self, val=0,left=None,right=None):
		self.val = val
		self.right = right
		self.left = left

class Solutions:
	def levelOrder(self, root):
		if not root:
			return []
		from collections import defaultdict, deque
		hash_map = defaultdict(list)
		queue = deque()
		level = 0
		queue.append([root,level])
		while queue:
			node, level = queue.popleft()
			hash_map[level].append(node.val)
			if node.left:
				queue.append([node.left, level+1])
			if node.right:
				queue.append([node.right,level+1])
		return list(hash_map.values())

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

res = Solutions()
print(res.levelOrder(root))


