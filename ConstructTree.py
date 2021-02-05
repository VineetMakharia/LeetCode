class Node:
	def __init__(self,val=0,left=None,right=None):
		self.val=val
		self.left=left
		self.right=right
  
def BuildTree(arr,root=None,i=0): 
    if i < len(arr) and arr[i]!=None: 
        temp = Node(arr[i])  
        root = temp  
        root.left = BuildTree(arr, root.left, 
                                     2 * i + 1)  
        root.right = BuildTree(arr, root.right, 
                                      2 * i + 2) 
    return root 
  
def inOrder(root): 
    if root:
        inOrder(root.left)
        print(root.val,end=" ")
        inOrder(root.right)
  
if __name__ == '__main__': 
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6] 
    root = BuildTree(arr)  
    print(inOrder(root)) 
      
