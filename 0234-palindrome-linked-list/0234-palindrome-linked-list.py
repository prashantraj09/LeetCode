# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, fast):
        curr = fast
        prev = None
        fwd = None
        while(curr != None):
            fwd = curr.next
            curr.next = prev
            prev = curr
            curr = fwd
        return prev
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head
        while((fast.next != None) and (fast.next.next != None)):
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        prev = self.reverse(fast)
        while((head is not None) and (prev is not None)):
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True



        # arr = []
        # while head:
        #     arr.append(head.val)
        #     head = head.next


        # # low, high = 0, len(arr) - 1
        # # while(low < high):
        # #     if arr[low] != arr[high]:
        # #         return False
        # #     low += 1
        # #     high -= 1
        # # return True

        # return arr == arr[::-1]