
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.total = 0
        
        def dfs(node):
            # If we see a null node, we don't need to cover it, so it will \
            # tell it's parent that I am covered
            if not node:
                return 'covered'
            # Recursively solve left and right
            left = dfs(node.left)
            right = dfs(node.right)

            # If left or right both don't have coverage, then I will have to \
            # place a camera at the node I am currently at.
            # Thus, this will return that it has a camera
            if left == 'notCovered' or right == 'notCovered':
                self.total+=1
                return 'has_camera'
            # If either the left or right subchild have a camera on them, that means \
            # that this node is covered, thus it returns covered.
            elif left == 'has_camera' or right == 'has_camera':
                return 'covered'
            # If the node's children are both covered, then this node will not have coverage \
            # due to the children, thus it will return not covered.
            return 'notCovered'
        
        # Special case, if the root is not covered, we will have to place an extra camera on it\
        # to provide coverage
        if dfs(root) == 'notCovered':
            self.total+=1
        return self.total


root = TreeNode(0)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(0)

obj = Solution()
print(obj.minCameraCover(root))