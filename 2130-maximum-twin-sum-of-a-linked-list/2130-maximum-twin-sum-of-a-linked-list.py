# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        fast = head
        slow = head
        while fast.next.next != None:
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
        maxi = 0
        while(prev):
            maxi = max(maxi, prev.val + head.val)
            head = head.next
            prev = prev.next
        return maxi
            

        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next
        # maxi = 0
        # i, j = 0, len(arr) - 1
        # while(i < j):
        #     maxi = max(maxi, arr[i] + arr[j])
        #     i += 1
        #     j -= 1
        # return maxi