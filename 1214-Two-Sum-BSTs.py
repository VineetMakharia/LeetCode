# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self,node):
        if not node:
            return []
        return self.inorder(node.left)  +[node.val] + self.inorder(node.right)
    
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        arr1 = set(self.inorder(root1))
        arr2 = self.inorder(root2)
        for num in arr2:
            complement = target - num
            if complement in arr1:
                return True
        return False

root = TreeNode(1)
root.left = TreeNode(0)
root.left.right = TreeNode(3)
root.right = TreeNode(0)

obj = Solution()
print(obj.twoSumBSTs(root,root,4))
print(obj.twoSumBSTs(root,root,8))