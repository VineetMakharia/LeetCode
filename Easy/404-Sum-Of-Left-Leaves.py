class Node:
    def __init__(self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        self.ans = 0
        def helper(root,isLeft):
            if not root.left and not root.right and isLeft:
                self.ans+=root.val
            if root.left:
                helper(root.left,True)
            if root.right:
                helper(root.right, False)
            return self.ans
        return helper(root,False)

root = Node(1)
root.left = Node(2)
root.left.left = Node(5)
root.right = Node(3)
root.right.left = Node(4)

obj = Solution()
print(obj.sumOfLeftLeaves(root))