class Node:
    def __init__(self,val=0,right=None,left=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self,root):
        if not root:
            return []
        return self.inorder(root.left)+[root.val]+self.inorder(root.right)
    
    def getAllElements(self, root1, root2):
        from collections import deque
        arr1 = self.inorder(root1)
        arr2 = self.inorder(root2)
        dq1 = deque(arr1)
        dq2 = deque(arr2)
        ans = []
        while dq1 or dq2:
            if not dq2:
                ans.append(dq1.popleft())
            elif not dq1:
                ans.append(dq2.popleft())
            else:
                ans.append(dq1.popleft() if dq1[0]<dq2[0] else dq2.popleft())
        return ans


root1 = Node(2)
root1.left = Node(1)
root1.right = Node(3)

root2 = Node(5)
root2.left = Node(0)
root2.right = Node(6)


obj = Solution()
print(obj.getAllElements(root1,root2))