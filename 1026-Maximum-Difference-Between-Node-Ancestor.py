class Node:
	def __init__(self, val=0,left=None,right=None):
		self.val = val
		self.right = right
		self.left = left

class Solution:
    def maxAncestorDiff(self, root):
        def helper(node,mx,mn):
            if not node:
                return mx-mn
            mx = max(mx,node.val)
            mn = min(mn,node.val)
            return max(helper(node.left,mx,mn), helper(node.right,mx,mn))
            
        return helper(root,float('-inf'),float('inf'))

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

obj = Solution()
print(obj.maxAncestorDiff(root))