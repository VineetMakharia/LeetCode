class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root):
        if not root:
            return 0
        from collections import deque
        queue = deque()
        queue.append((root,1))
        level_of_max = -1
        max_sum = float('-inf')
        while queue:
            level_sum=0
            for _ in range(len(queue)):
                node,current_level = queue.popleft()
                level_sum+=node.val
                if node.left:
                    queue.append((node.left,current_level+1))
                if node.right:
                    queue.append((node.right, current_level+1))
            if level_sum>max_sum:
                max_sum=level_sum
                level_of_max = current_level
        return level_of_max

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
obj = Solution()
print(obj.maxLevelSum(root))