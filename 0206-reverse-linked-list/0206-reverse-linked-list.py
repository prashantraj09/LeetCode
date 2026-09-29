# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if ((head is None) or (head.next is None)):
            return head
        a = head.next
        head.next = None
        b = self.reverseList(a)
        a.next = head
        return b



# class Solution:
#     def reverseList(self, head: ListNode | None) -> ListNode | None:
#         prev = None
#         forw = None
#         curr = head
#         while curr:
#             forw = curr.next
#             curr.next = prev
#             prev = curr
#             curr = forw
#         return prev



# class Solution:
#     def reverseList(self, head: ListNode | None) -> ListNode | None:
#         arr = []
#         curr = head
#         while curr:
#             arr.append(curr.val)
#             curr = curr.next
#         curr = head
#         for i in range(len(arr) - 1, -1, -1):
#             curr.val = arr[i]
#             curr = curr.next
#         return head