# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root) -> int:
        self.ans = float('-inf')
        def gain_on_node(node):
            if not node:
                return 0
            # Recursively find the greatest gain on the left side
            # if -ve then the entire subtree is useless so you don't want to select it
            # Similarly do the same for right subtree
            left_gain = max(0,gain_on_node(node.left))
            right_gain = max(0,gain_on_node(node.right))
            self.ans = max(self.ans, node.val+left_gain+right_gain)
            # you send the max found between the 2 children cause you can't choose both of them simultaneously
            return max(left_gain,right_gain) + node.val
        gain_on_node(root)
        return self.ans

root = Node(-10)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

obj = Solution()
print(obj.maxPathSum(root))