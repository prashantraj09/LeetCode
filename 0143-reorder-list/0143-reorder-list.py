# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        slow = head
        fast = head
        while((fast.next != None) and (fast.next.next != None)):
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None

        curr = fast
        prev = None
        fwd = None
        while curr:
            fwd = curr.next
            curr.next = prev
            prev = curr
            curr = fwd
        
        while prev:
            temp1 = head.next
            temp2 = prev.next
            head.next = prev
            prev.next = temp1
            head = temp1
            prev = temp2