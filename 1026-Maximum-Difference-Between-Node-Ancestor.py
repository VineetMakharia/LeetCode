class Node:
	def __init__(self, val=0,left=None,right=None):
		self.val = val
		self.right = right
		self.left = left

class Solution:
    def maxAncestorDiff(self, root):
        self.ans = 0
        # Each node return it's smallest and largest values
        def helper(node):
            if not node:
                #smallest,largest
                return float('inf'),float('-inf')
            if not node.left and not node.right:
                return node.val,node.val
            sl,ll = helper(node.left)
            sr,lr = helper(node.right)
            new_small = min(node.val,sl,sr)
            new_large = max(node.val,ll,lr)
            self.ans = max(self.ans, abs(node.val-new_small),abs(node.val-new_large))
            return new_small,new_large
        helper(root)
        return self.ans

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

obj = Solution()
print(obj.maxAncestorDiff(root))