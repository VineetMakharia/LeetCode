class Node:
	def __init__(self,val=0,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right

class Solution:
	def delete(self,root,key):
		if not root:
			return None
		# Case 1: Root exists in the right subtree
		if key>root.val:
			root.right = self.delete(root.right,key)

		# Case 2: Root exists in the left subtree
		elif key<root.val:
			root.left = self.delete(root.left,key)

		# Case 3: key == root.val
		# We need to find the smallest value in the right subtree (if it exists)
		else:
			if not root.left:
				return root.right
			if not root.right:
				return root.left
			if root.left and root.right:
				temp = root.right
				while temp.left:
					temp = temp.left
				root.val = temp.val
				root.right = self.delete(root.right,temp.val)
		return root

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(7)

def inorder(node):
	if not node:
		return []
	return inorder(node.left) + [node.val] + inorder(node.right)

obj = Solution()
print(inorder(root))
print(inorder(obj.delete(root,3)))
print(inorder(obj.delete(root,6)))
print(inorder(obj.delete(root,5)))
print(inorder(obj.delete(root,2)))
print(inorder(obj.delete(root,4)))
print(inorder(obj.delete(root,7)))

