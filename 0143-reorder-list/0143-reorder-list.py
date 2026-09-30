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
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        i, j = 0, len(arr) - 1
        while(i <= j):
            if i == j:
                head.val = arr[i]
                head.next = None
                break
            head.val = arr[i]
            head.next.val = arr[j]
            i += 1
            j -= 1
            head = head.next.next