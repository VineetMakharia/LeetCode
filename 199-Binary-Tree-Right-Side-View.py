class Node():
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        ans = []
        from collections import deque
        queue = deque()
        queue.append((root))
    
        while queue:
            sz = len(queue)
            ans.append(queue[-1].val)
            for _ in range(sz):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return ans

root = Node(1)
root.left = Node(2)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(4)

obj = Solution()
print(obj.rightSideView(root))


