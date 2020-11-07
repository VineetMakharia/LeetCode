# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = (num<<1) | head.next.val
            # num = num*2 + head.next.val
            head = head.next
        return num

head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

obj = Solution()
print(obj.getDecimalValue(head))