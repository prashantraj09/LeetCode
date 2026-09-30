# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        curr1 = dummy1
        curr2 = dummy2
        i = 1
        while(head != None):
            if (i % 2 == 0):
                curr2.next = head
                curr2 = curr2.next
            else:
                curr1.next = head
                curr1 = curr1.next
            i += 1
            head = head.next
        curr2.next = None
        curr1.next = dummy2.next
        return dummy1.next