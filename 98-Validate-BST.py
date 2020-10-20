# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # def helper(node,lower,upper):
        #     if not node:
        #         return True
        #     if node.val <= lower or node.val>=upper:
        #         return False
        #     if not helper(node.left,lower,node.val):
        #         return False
        #     if not helper(node.right,node.val,upper):
        #         return False
        #     return True
        # return helper(root,float('-inf'),float('inf'))
        inorder = self.inorder_traversal(root)
        for i in range(1,len(inorder)):
            if inorder[i-1] >= inorder[i]:
                return False
        return True
    
    def inorder_traversal(self,node):
        if not node:
            return []
        return self.inorder_traversal(node.left) + [node.val] + self.inorder_traversal(node.right)

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

obj = Solution()
print(obj.isValidBST(root))
print(obj.isValidBST(root1))