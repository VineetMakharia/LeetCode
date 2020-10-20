class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = Node(-1)
        head = dummy
        carry = 0
        while l1 or l2 or carry:
            vl1 = l1.val if l1 else 0
            vl2 = l2.val if l2 else 0
            add = vl1 + vl2 + carry
            carry = 1 if add>=10 else 0
            add = add % 10
            dummy.next = Node(add)
            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return self.printList(head.next)
    
    def printList(self,head):
        while head:
            print(head.val, end = " ")
            head = head.next
        print()

# Number is 342
list1 = Node(2)
list1.next = Node(4)
list1.next.next = Node(3)

# Number is 465
list2 = Node(5)
list2.next = Node(6)
list2.next.next = Node(4)


obj = Solution()
obj.addTwoNumbers(list1,list2)
obj.addTwoNumbers(list1,list1)
obj.addTwoNumbers(list2,list2)


