# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        ans = 0
        def helper(node):
            nonlocal ans
            if not node:
                return (True, 0 , float('inf'), float('-inf'))
            is_left_valid, left_largest_tree, left_smallest_val, left_largest_val = helper(node.left)
            is_right_valid, right_largest_tree, right_smallest_val, right_largest_val = helper(node.right)
            if is_left_valid and is_right_valid and left_largest_val<node.val<right_smallest_val:
                ans = max(ans,left_largest_tree+right_largest_tree+1)
                return (True, left_largest_tree+right_largest_tree+1, min(node.val,left_smallest_val), max(node.val,right_largest_val))
            else:
                return (False,0,0,0)
    
        helper(root)
        return ans

obj = Solution()

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(8)

print(obj.largestBSTSubtree(root))