class Node():
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def rightSideView(self, root):
		if not root:
			return []
		from collections import defaultdict, deque
		hash_map = defaultdict(list)
		queue = deque()
		queue.append([root,0])
		while queue:
			node, level = queue.popleft()
			hash_map[level].append(node.val)
			if node.left:
				queue.append([node.left, level+1])
			if node.right:
				queue.append([node.right, level+1])
		ans = []
		for key, value in hash_map.items():
			ans.append(value[-1])
		return ans

root = Node(1)
root.left = Node(2)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(4)

obj = Solution()
print(obj.rightSideView(root))


