# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        total = 0
        def helper(node):
            nonlocal total
            if not node:
                return 0
            sum_left = helper(node.left)
            sum_right = helper(node.right)
            total+=abs(sum_left-sum_right)
            return node.val + sum_left + sum_right
        
        helper(root)
        return total

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

obj = Solution()
print(obj.findTilt(root))