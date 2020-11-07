class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def throw_into_stack(node):
            stack = []
            while node:
                stack.append(node.val)
                node = node.next
            return stack
        
        s1 = throw_into_stack(l1)
        s2 = throw_into_stack(l2)
        
        head = None
        carry = 0
        
        while s1 or s2 or carry:
            vl1 = s1.pop() if s1 else 0
            vl2 = s2.pop() if s2 else 0
            total = vl1 + vl2 + carry
            carry = 1 if total>9 else 0
            total = total%10
            curr = ListNode(total)
            curr.next = head
            head = curr
        return self.print_LL(head)

    def print_LL(self,node):
        while node:
            print(f'{node.val} -->',end="")
            node = node.next
obj = Solution()
head = ListNode(7)
head.next = ListNode(7)
head.next.next = ListNode(7)

print(obj.addTwoNumbers(head,head))