class newNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self,node): 
        while (node): 
            print(node.val, end=" ") 
            node = node.next

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        temp = dummy = newNode(-1)
        while l1 or l2:
            v1 = l1.val if l1 else float('INF')
            v2 = l2.val if l2 else float('INF')
            if v1>=v2:
                temp.next = l2
                l2 = l2.next
            else:
                temp.next = l1
                l1 = l1.next
            temp = temp.next
        self.printList(dummy.next)

head1 = newNode(1)
head1.next = newNode(3) 
head1.next.next = newNode(5) 
   
head2 = newNode(0) 
head2.next = newNode(2) 
head2.next.next = newNode(4) 

res = Solution()
res.mergeTwoLists(head1,head2)
            
                
        
        