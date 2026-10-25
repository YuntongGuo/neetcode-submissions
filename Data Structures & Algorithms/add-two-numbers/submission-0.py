# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        start = new
        inc = 0
        while l1 and l2:
            d = l1.val + l2.val + inc
            curr = d % 10
            inc = d//10
            new.next = ListNode(val=curr)
            new = new.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            d = l1.val + inc
            curr = d % 10
            inc = d//10
            new.next = ListNode(val=curr)
            new = new.next
            l1 = l1.next

        while l2:
            d = l2.val + inc
            curr = d % 10
            inc = d//10
            new.next = ListNode(val=curr)
            new = new.next
            l2 = l2.next

        if inc != 0:
            new.next = ListNode(val = 1)

        return start.next






