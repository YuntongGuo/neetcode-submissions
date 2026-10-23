# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        # find middle
        s = head
        f = head
        last = None
        while f != None and f.next != None:
            f = f.next.next
            last = s
            s = s.next
        last.next = None
        middle = s
        # print(middle.val)
        # reverse
        last = None
        while middle:
            n = middle.next
            middle.next = last
            last = middle 
            middle = n
        middle = last
        # while last:
        #     print(last.val)
        #     last = last.next
        # merger
        starter = head
        while head and middle:
            next_head = head.next
            next_middle = middle.next 
            head.next = middle
            middle.next = next_head
            if not next_head:
                middle.next = next_middle
                break
            head = next_head
            middle = next_middle
            # print(head,middle    
        head = starter

