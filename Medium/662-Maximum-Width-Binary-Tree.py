class Node():
	def __init__(self,val=0,left=None,right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
    def widthOfBinaryTree(self, root):
        from collections import defaultdict, deque
        if not root:
            return 0
        width = 1
        queue = deque()
        queue.append([root,0])
        level = 0
        hash_map = defaultdict(list)
        while queue:
            level+=1
            for _ in range(len(queue)):
                node, index = queue.popleft()
                hash_map[level].append(index)
                if node.left:
                    queue.append([node.left, 2*index+1])
                if node.right:
                    queue.append([node.right, 2*index+2])
        # print(hash_map)
        for key,value in hash_map.items():
            if key>1:
                min_val = value[0]
                max_val = value[-1]
                width = max(width, max_val-min_val+1)
        return width


root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.right = Node(9)

res = Solution()
print(res.widthOfBinaryTree(root))
        