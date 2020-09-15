class Node : 
    def __init__(self ,key): 
        self.key = key  
        self.children = [] 

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        # max_depth = 0
        # for child in root.children:
        #     max_depth=max(max_depth,self.maxDepth(child))
        # return 1+max_depth
        max_depth = 1
        from collections import deque
        queue = deque()
        queue.append((root,1))
        while queue:
            node, current_depth = queue.popleft()
            max_depth = max(max_depth, current_depth)
            for child in node.children:
                queue.append((child,current_depth+1))
        return max_depth

root = Node(10) 
root.children.append(Node(2)) 
root.children.append(Node(34)) 
root.children.append(Node(56)) 
root.children.append(Node(100)) 
root.children[2].children.append(Node(1)) 
root.children[3].children.append(Node(7)) 
root.children[3].children.append(Node(8)) 
root.children[3].children.append(Node(9))

obj = Solution()
print(obj.maxDepth(root))
