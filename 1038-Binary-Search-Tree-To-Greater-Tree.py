class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def __init__(self):
        self.total = 0


    def bstToGst(self, root):
        if root:
            self.bstToGst(root.right)
            self.total+=root.val
            root.val=self.total
            self.bstToGst(root.left)
        return root

        # def inorder(node):
        #     if not node:
        #         return []
        #     return inorder(node.left)+[node.val]+inorder(node.right)
        
        # def sum_right(val,arr):
        #     return sum([x for x in arr if x>=val])
        
        # if not root:
        #     return
        # arr = inorder(root)
        # from collections import deque
        # queue = deque()
        # queue.append((root))
        # while queue:
        #     current = queue.popleft()
        #     current.val = sum_right(current.val,arr)
        #     if current.left:
        #         queue.append((current.left))
        #     if current.right:
        #         queue.append((current.right))
        # return root

root = Node(10)
root.left = Node(9)
root.right = Node(12)

obj = Solution()
res = (obj.bstToGst(root))
print(res.left.val, res.val, res.right.val)