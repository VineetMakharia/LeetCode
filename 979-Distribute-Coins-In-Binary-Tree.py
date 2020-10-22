# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0
        def helper(node):
            if not node:
                return 0
            left_needs = helper(node.left)
            right_needs = helper(node.right)
            self.moves += abs(left_needs) + abs(right_needs)
            excess = node.val + left_needs + right_needs - 1
            return excess
        helper(root)
        return self.moves

root = TreeNode(1)
root.left = TreeNode(0)
root.left.right = TreeNode(3)
root.right = TreeNode(0)

obj = Solution()
print(obj.distributeCoins(root))