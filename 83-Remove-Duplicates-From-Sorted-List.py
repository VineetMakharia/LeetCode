class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        current = head.next
        prev = head
        while current:
            if current.val == prev.val:
                prev.next = current.next
            else:
                prev = prev.next
            current = current.next
        return head

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)

def print_list(node):
    while node:
        print(node.val)
        node=node.next

obj = Solution()
print(print_list(obj.deleteDuplicates(head)))