from ConstructTree import *
class Solution:
    def pruneTree(self, root):
        def helper(node):
            if not node:
                return False
            is_one_present_left = helper(node.left)
            is_one_present_right = helper(node.right)
            node.left = None if (not is_one_present_left) else node.left
            node.right = None if (not is_one_present_right) else node.right
            return is_one_present_left or is_one_present_right or node.val==1
        
        return None if not helper(root) else root

obj = Solution()
tc = [[1,None,0,0,1],[1,0,1,0,0,0,1]]
for arr in tc:
    root = BuildTree(arr)
    print(inOrder(obj.pruneTree(root)))