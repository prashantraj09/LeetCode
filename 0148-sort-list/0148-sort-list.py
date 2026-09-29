# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy
        while((list1 != None) and (list2 != None)):
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 is None:
            current.next = list2
        else:
            current.next = list1
        return dummy.next
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if((head is None) or (head.next is None)):
            return head
        slow = head
        fast = head
        while((fast.next != None) and (fast.next.next != None)):
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        list1 = self.sortList(head)
        list2 = self.sortList(head2)
        return self.merge(list1, list2)