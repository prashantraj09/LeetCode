# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        curr1 = dummy1
        curr2 = dummy2
        while head:
            if head.val < x:
                curr1.next = head
                curr1 = curr1.next
            else:
                curr2.next = head
                curr2 = curr2.next
            head = head.next
        curr2.next = None
        curr1.next = dummy2.next
        return dummy1.next