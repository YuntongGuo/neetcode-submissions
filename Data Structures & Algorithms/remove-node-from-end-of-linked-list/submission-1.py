# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        node = head
        while node:
            node = node.next
            count += 1
        if count <=1:
            return None
        # go to n
        target = count - n
        last = None
        node = head
        nth = 0
        while nth < target:
            last = node
            node= node.next
            nth += 1
        if last is None:
            return head.next
        last.next = node.next
        return head