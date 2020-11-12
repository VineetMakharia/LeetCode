class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self,root):
        if not root:
            return 0

        def helper(node):
            # A null node will send that if you choose me or my grandchildren, \
            # the max gain you can get is only 0,0
            if not node:
                return [0,0]
            # Recursively find what the gain would be by choosing left child and left grandchild
            left_child,left_grandchild = helper(node.left)
            right_child,right_grandchild = helper(node.right)
            # If I choose the current node, then I can only choose the grandchildren
            with_node = node.val + left_grandchild + right_grandchild
            # If I don't choose the node, then I am free to choose the maximum gain amongst leftchild and grandchild \
            # rightchild and grandchild cause they will never be directly connected
            without_node = max(left_child,left_grandchild) + max(right_child,right_grandchild)

            return [with_node,without_node]
        
        return max(helper(root))

root = Node(3)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(3)
root.right.right = Node(1)

obj = Solution()
print(obj.rob(root))