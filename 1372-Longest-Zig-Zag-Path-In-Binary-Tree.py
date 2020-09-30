# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        # 1st idea --> BFS
        # Base Condition
        if not root or (not root.left and not root.right):
            return 0
        
        from collections import deque
        queue = deque()
        # Build a queue with history whether we're coming from left or right
        if root.left:
            queue.append((root.left,1,'left'))
        if root.right:
            queue.append((root.right,1,'right'))
        max_path = -1
        while queue:
            current, path, direction = queue.popleft()
            max_path = max(max_path,path)
            if current.left:
                if direction == 'right':
                    queue.append((current.left,path+1,'left'))
                else:
                    queue.append((current.left,1,'left'))
            if current.right:
                if direction == 'left':
                    queue.append((current.right,path+1,'right'))
                else:
                    queue.append((current.right,1,'right'))
        return max_path