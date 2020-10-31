# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        if not root:
            return 0
        ans = 0
        def helper(node):
            nonlocal ans
            if not node:
                return (0, 0.0)
            number_of_nodes_left, sum_left = helper(node.left)
            number_of_nodes_right, sum_right = helper(node.right)
            number_of_nodes_at_level = number_of_nodes_left + number_of_nodes_right + 1
            sum_of_nodes_at_level = sum_left + sum_right + node.val
            ans = max(ans, sum_of_nodes_at_level/number_of_nodes_at_level)
            return (number_of_nodes_at_level,sum_of_nodes_at_level)
        
        helper(root)
        return ans

obj = Solution()
root = TreeNode(5)
root.left = TreeNode(6)
root.right = TreeNode(1)

print(obj.maximumAverageSubtree(root))