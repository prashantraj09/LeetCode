# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        maxi = 0
        i, j = 0, len(arr) - 1
        while(i < j):
            maxi = max(maxi, arr[i] + arr[j])
            i += 1
            j -= 1
        return maxi