from ConstructTree import BuildTree
class Solution:
    def sumEvenGrandparent(self, root) -> int:
#         from collections import deque
#         queue = deque()
#         queue.append((root))
#         total = 0
        
#         while queue:
#             node = queue.popleft()
#             if node.left:
#                 queue.append((node.left))
#                 if node.val%2==0:
#                     if node.left.left:
#                         total+=node.left.left.val
#                     if node.left.right:
#                         total+=node.left.right.val
#             if node.right:
#                 queue.append((node.right))
#                 if node.val%2 == 0:
#                     if node.right.left:
#                         total+=node.right.left.val
#                     if node.right.right:
#                         total+=node.right.right.val
                        
#         return total
        
        
        def helper(node,parent,grandparent):
            total = 0
            if node == None:
                # print(f"RETURNING, parent = {parent.val}")
                return 0
            # print(node.val)
            if grandparent and (grandparent.val%2==0):
                total+=node.val
            total+=helper(node.left,node,parent)
            total+=helper(node.right,node,parent)
            return total
            
            
        return helper(root,None,None)

obj = Solution()
arr = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
n = len(arr)
root = None
root = BuildTree(arr, root, 0, n)
print(obj.sumEvenGrandparent(root))
