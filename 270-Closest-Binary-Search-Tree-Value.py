# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        # Assume that the closest value is the root value
        closest = root.val
        node = root
        while node:
            val = node.val
            # Update answer if the current value-target is smaller than the closest seen so far
            closest = val if abs(val-target) < abs(closest-target) else closest
            node = node.left if target<node.val else root.right
        return closest

obj = Solution()

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(obj.closestValue(root,3.714))