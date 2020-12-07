class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    

#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Node) -> int:
        ans = 0
        def helper(node):
            # If a node is null, then you return 0 to the parent stating that no edge is possible
            nonlocal ans
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)
            llocal = 0
            rlocal = 0
            # If node.left exists and node.left.val==node.val, then you need to update your local variable
            # Which will be passed to the parent
            if node.left and node.left.val==node.val:
                llocal = left+1
            if node.right and node.right.val==node.val:
                rlocal = right+1
            # let's say that there is no match, then llocal and rlocal will both be 0
            ans = max(ans,llocal+rlocal)
            # You want to send the maximum amongst your 2 children up the chain
            return max(llocal,rlocal)
    
        helper(root)
        return ans

root = Node(5)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(1)
root.right.right = Node(5)

obj = Solution()
print(obj.longestUnivaluePath(root))