class Node:
	def __init__(self,val=0,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right


class Solution:
    def sumRootToLeaf(self, root):
        if not root:
            return 0
        self.total=0
        
        def helper(node,cur_sum):
            if not node.left and not node.right:
                self.total+=cur_sum
            if node.left:
                helper(node.left, cur_sum*2+node.left.val)
            if node.right:
                helper(node.right, cur_sum*2+node.right.val)
        
        helper(root,root.val)
        return self.total
        
        #BFS
        # from collections import deque
        # queue = deque()
        # queue.append([root,root.val])
        # total = 0
        # while queue:
        #     node, current_val = queue.popleft()
        #     if not node.left and not node.right:
        #         total+=current_val
        #     if node.left:
        #         queue.append([node.left, 2*current_val+node.left.val])
        #     if node.right:
        #         queue.append([node.right, 2*current_val+node.right.val])
        # return total

root = Node(1)
root.left = Node(0)
root.right = Node(1)
root.left.left = Node(0)
root.left.right = Node(1)
root.right.left = Node(0)
root.right.right = Node(1)

obj = Solution()
print(obj.sumRootToLeaf(root))