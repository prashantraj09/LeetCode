# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next


        # low, high = 0, len(arr) - 1
        # while(low < high):
        #     if arr[low] != arr[high]:
        #         return False
        #     low += 1
        #     high -= 1
        # return True

        return arr == arr[::-1]