# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

	
class Solution:
	def insertIntoBST(self, root, val):
		if not root:
			return TreeNode(val)
		elif val>root.val:
			root.right = self.insertIntoBST(root.right,val)
		else:
			root.left = self.insertIntoBST(root.left,val)
		return root
	
	def inorder(self,node):
		if not node:
			return []
		return self.inorder(node.left) + [node.val] + self.inorder(node.right)

root = TreeNode(2)
obj = Solution()
obj.insertIntoBST(root,1)
print(obj.inorder(root))
obj.insertIntoBST(root,3)
print(obj.inorder(root))
