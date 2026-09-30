# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if((head is None) or (head.next is None)):
            return head
        slow = head
        fast = head.next
        prev = None
        while fast:
            temp = fast.next
            fast.next = slow
            slow.next = temp
            if prev:
                prev.next = fast
            else:
                head = fast
            prev = slow
            slow = temp
            if slow is None or slow.next is None:
                break
            fast = slow.next
        return head